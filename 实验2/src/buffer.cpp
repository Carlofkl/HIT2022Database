/**
 * @author See Contributors.txt for code contributors and overview of BadgerDB.
 *
 * @section LICENSE
 * Copyright (c) 2012 Database Group, Computer Sciences Department, University of Wisconsin-Madison.
 */

#include <memory>
#include <iostream>
#include "buffer.h"
#include "exceptions/buffer_exceeded_exception.h"
#include "exceptions/page_not_pinned_exception.h"
#include "exceptions/page_pinned_exception.h"
#include "exceptions/bad_buffer_exception.h"
#include "exceptions/hash_not_found_exception.h"

namespace badgerdb
{

	BufMgr::BufMgr(std::uint32_t bufs)
		: numBufs(bufs)
	{
		bufDescTable = new BufDesc[bufs];

		for (FrameId i = 0; i < bufs; i++)
		{
			bufDescTable[i].frameNo = i;
			bufDescTable[i].valid = false;
		}

		bufPool = new Page[bufs];

		int htsize = ((((int)(bufs * 1.2)) * 2) / 2) + 1;
		hashTable = new BufHashTbl(htsize); // allocate the buffer hash table

		clockHand = bufs - 1;
	}

	BufMgr::~BufMgr()
	{
		for (FrameId i = 0; i < numBufs; i++)
		{
			if (bufDescTable[i].dirty)
			{
				bufDescTable[i].file->writePage(bufPool[i]);
			}
		}
		delete[] bufPool;
		delete[] bufDescTable;
		delete hashTable;
	}

	void BufMgr::advanceClock()
	{
		clockHand = (clockHand + 1) % numBufs;
	}

	void BufMgr::allocBuf(FrameId &frame)
	{
		bool flag = true;
		for (uint32_t i = 0; i < numBufs || !flag; ++i)
		{
			advanceClock();
			if (!bufDescTable[clockHand].valid)
			{
				frame = clockHand;
				return ;
			}
			if (bufDescTable[clockHand].pinCnt)
				continue;
			flag = false;
			if (bufDescTable[clockHand].refbit)
			{
				bufDescTable[clockHand].refbit = false;
				continue;
			}
			if (bufDescTable[clockHand].dirty)
			{
				bufDescTable[clockHand].file->writePage(bufPool[clockHand]);
				bufDescTable[clockHand].dirty = false;
			}
			hashTable->remove(bufDescTable[clockHand].file,
				bufDescTable[clockHand].pageNo);
			bufDescTable[clockHand].Clear();
			frame = clockHand;
			return ;
		}
		throw BufferExceededException();
	}

	void BufMgr::readPage(File *file, const PageId pageNo, Page *&page)
	{
		FrameId frame;
		try
		{
			hashTable->lookup(file, pageNo, frame);
			bufDescTable[frame].refbit = true;
			bufDescTable[frame].pinCnt++;
		}
		catch(HashNotFoundException&)  // 页面不在缓冲池
		{ 
			allocBuf(frame);  // 分配一个新的空闲页框
			bufPool[frame] = file->readPage(pageNo);  // 从磁盘读入到这个页框
			hashTable->insert(file, pageNo, frame);  // 该页面插入哈希表
			bufDescTable[frame].Set(file, pageNo);  // 设置页框状态
		}
		page = bufPool + frame;  // 通过pege返回指向该页框的指针
	}

	void BufMgr::unPinPage(File *file, const PageId pageNo, const bool dirty)
	{
		FrameId frame;
		try
		{
			hashTable->lookup(file, pageNo, frame);  // 找到(file,PageNo)所在页框
			if (!bufDescTable[frame].pinCnt)
				throw PageNotPinnedException(file->filename(),
					pageNo, frame);
			bufDescTable[frame].pinCnt--;  //表示页面所在的页框的pinCnt减一
			if (dirty)
				bufDescTable[frame].dirty = dirty;  // 将页框的dirty设置true
		}
		catch(HashNotFoundException&)
		{
		}
	}

	void BufMgr::flushFile(const File *file)
	{
		for (uint32_t i = 0; i < numBufs; ++i)  // 扫描所有文件
		{
			if (bufDescTable[i].file == file)  // 属于file的页面
			{
				if (!bufDescTable[i].valid)  // 无效页
					throw BadBufferException(i, bufDescTable[i].dirty,
						bufDescTable[i].valid, bufDescTable[i].refbit);
				if (bufDescTable[i].pinCnt)  // 被固定
					throw PagePinnedException(file->filename(),
						bufDescTable[i].pageNo, i);
				if (bufDescTable[i].dirty)  // 如果页面是脏的，则写回磁盘
					bufDescTable[i].file->writePage(bufPool[i]);
				bufDescTable[i].dirty = false;
				hashTable->remove(file, bufDescTable[i].pageNo);
				bufDescTable[i].Clear();
			}
		}
	}

	void BufMgr::allocPage(File *file, PageId &pageNo, Page *&page)
	{
		FrameId frame;
		allocBuf(frame);  // 分配一个新的页框
		bufPool[frame] = file->allocatePage(); // 返回一个空闲页面
		pageNo = bufPool[frame].page_number(); // 
		hashTable->insert(file, pageNo, frame); // 哈希表中插入该页面
		bufDescTable[frame].Set(file, pageNo);  // 设置页框状态
		page = bufPool + frame;  // 通过page参数返回指向缓冲池中包含该页面的页框的指针
	}

	void BufMgr::disposePage(File *file, const PageId PageNo)
	{
		FrameId frame;
		try
		{
			hashTable->lookup(file, PageNo, frame); // 如果页面在缓冲池中
			hashTable->remove(file, PageNo);  // 将页框清空并从哈希表中删除页面
			bufDescTable[frame].Clear();  
		}
		catch(HashNotFoundException&)
		{
		}
		file->deletePage(PageNo);  // 删除也好为PageNo的页面
	}

	void BufMgr::printSelf(void)
	{
		BufDesc *tmpbuf;
		int validFrames = 0;

		for (std::uint32_t i = 0; i < numBufs; i++)
		{
			tmpbuf = &(bufDescTable[i]);
			std::cout << "FrameNo:" << i << " ";
			tmpbuf->Print();

			if (tmpbuf->valid == true)
				validFrames++;
		}

		std::cout << "Total Number of Valid Frames:" << validFrames << "\n";
	}

}
