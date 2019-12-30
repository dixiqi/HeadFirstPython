from url_utils import gen_from_urls

urls = ('http://www.oreilly.com', 'http://baidu.com','http://music.163.com')

for resp_len, status, url, in gen_from_urls(urls):         #在一个for循环中使用这个生成器函数
    print(resp_len, '->', status, '->', url)
