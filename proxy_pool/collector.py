#!/usr/bin/env python
 
from random import randrange
import urllib
import urllib2
import cPickle as pickle
import re
import os
import sys
import gevent
import gevent.monkey
gevent.monkey.patch_socket()

class Collector(object):

	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
				(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
	request_interval = 5
	jump_url = 'http://s.tool.chinaz.com/tools/pagecode.aspx'
	proxy_pool = set()
	local_store = '.proxy_pool.pkl'
	default_start_page = 'http://www.kuaidaili.com/proxylist/1/'
	default_target_parttern = r'href=\&quot;(/proxylist\/\d+\/)\&quot;'
	default_ip_parttern = r'data-title=\&quot;IP\&quot;\&gt;([\d\.]+?)\&lt;\/td\&gt;'
	default_port_parttern = r'data-title=\&quot;PORT\&quot;\&gt;(\d+?)\&lt;\/td\&gt;'

	def __init__(self, start_page=None, target_parttern=None, regex_obj={}):
		self.start_page = start_page if start_page else \
								self.default_start_page
		self.base_path = os.path.abspath('.')
		self.local_store = self.base_path + '/' + self.local_store
		self.target_url_base = '/'.join(self.start_page.split('/')[0:3])
		self.target_domain = self.start_page.split('/')[2]
		self.target_parttern = target_parttern if target_parttern else \
								self.default_target_parttern
		self.ip_parttern = self.default_ip_parttern if 'IP' not in \
								regex_obj.keys() else regex_obj['IP']
		self.port_parttern = self.default_port_parttern if 'PORT' not in \
							regex_obj.keys() else regex_obj['PORT']
	
	def _get_content(self, url):
		postdata=urllib.urlencode(dict(searchMode=0, q=url, codecolor=0))
		req = urllib2.Request(self.jump_url, postdata, headers={
			'User-Agent': self.user_agent,
			'Referer': self.target_url_base})
		try:
			res = urllib2.urlopen(req)
			print 'get content: {}'.format(url)
			return res.read()
		except HTTPError, e:
		    print 'The server couldn\'t fulfill the request.'
		    print 'Error code: ', e.code 
		except URLError, e: 
		    print 'We failed to reach a server.' 
		    print 'Reason: ', e.reason

	def _store_in_local(self):
		pickle.dump(self.proxy_pool, open(self.local_store, 'wb'))


	def _get_proxy(self, target):
		gevent.sleep(randrange(1,5))
		content = self._get_content(target)
		targets = re.compile(self.target_parttern).findall(content)
		ips = re.compile(self.ip_parttern).findall(content)
		ports = re.compile(self.port_parttern).findall(content)
		proxy_list = []
		for i in range(len(ips)):
			proxy_list.append(ips[i] + ':' + str(ports[i]))
		return targets, proxy_list


	def collect_proxies(self):
		targets = [] 
		tgs, pl = self._get_proxy(self.start_page)
		self.proxy_pool.update(set(pl))
		count = 1
		tgs = tgs[1:]

		jobs = [gevent.spawn(self._get_proxy, self.target_url_base + tg) for tg in tgs]
		gevent.joinall(jobs)
		pls = [job.value for job in jobs]
		for pl in pls:
			self.proxy_pool.update(set(pl[1]))
		self._store_in_local()
		return self.proxy_pool

	def get_one_proxy(self):
		if not self.proxy_pool:
			if os.path.exists(self.local_store):
				self.proxy_pool = pickle.load(open(self.local_store, 'rb'))
			else:
				self.collect_proxies()
		return list(self.proxy_pool)[randrange(0, len(self.proxy_pool))]

