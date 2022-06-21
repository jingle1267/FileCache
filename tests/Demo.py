# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2022/6/21 10:28
@desc：  : 
"""
from FileCache import FileCache


def test_hit_callback(**args):
	print("test_hit_callback")
	print('a', args['a'])
	print(type(args), args)


def test_miss_callback(**args):
	print("test_miss_callback", args)
	print('a', args['a'])
	return True


if __name__ == '__main__':
	FileCache.CACHE_DIR = './tests'
	FileCache.CACHE_FILE_SECTION_COUNT = 2
	FileCache.easy_cache('test_cache_file.json', 'cache_key', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'cache_key1', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'cache_key2', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'cache_key3', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'abc123', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'abc111', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'abc222', test_hit_callback, test_miss_callback, a=1, b='c')
	FileCache.easy_cache('test_cache_file.json', 'abc333', test_hit_callback, test_miss_callback, a=1, b='c')