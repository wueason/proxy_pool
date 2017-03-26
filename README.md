# proxy_pool
A proxy pool which you can get an avaiable proxy http server.

When we run a crawler for data collecting purpose, we always get blocked. This module may help you get out of the trouble.  

```python
start_page = 'http://www.xicidaili.com/nt/'
target_parttern = r'href=\&quot;(\/nt\/\d+)\&quot;\&gt;'
ip_parttern = r'\&lt;td\&gt;(\d+\.\d+\.\d+\.\d+)\&lt;\/td\&gt;'
port_parttern = r'\&lt;td\&gt;(\d{2,5})\&lt;\/td\&gt;'

collector = Collector(start_page=start_page,
					target_parttern=target_parttern,
					regex_obj={
						"IP": ip_parttern,
						"PORT": port_parttern
					})
collector = proxy_pool.Collector()
collector.collect_proxies() # init or update proxy info
collector.get_one_proxy() # get the proxy
```
