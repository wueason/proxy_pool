# proxy_pool
A proxy pool which you can get an avaiable proxy http server.

When we run a crawler for data collecting purpose, we always get blocked. This module may help you get out of the trouble.  

```python
collector = proxy_pool.Collector()
collector.collect_proxies() # init or update proxy info
collector.get_one_proxy() # get the proxy
```