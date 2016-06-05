#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import proxy_pool
import re


partten = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}:\d+$'

class TestCollector(unittest.TestCase):
	def setUp(self):
		self.collector = proxy_pool.Collector()

	def test_collect_proxies(self):
		proxy_pool = self.collector.collect_proxies()
		for proxy in proxy_pool:
			self.assertIsNotNone(re.search(partten, proxy[1]))

	def test_get_one_proxy(self):
		proxy = self.collector.get_one_proxy()
		self.assertIsNotNone(re.search(partten, proxy))

if __name__ =='__main__': 
  unittest.main()