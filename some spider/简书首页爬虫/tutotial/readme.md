无聊复习下爬虫,用scrapy爬取了简书的热门文章,后面可以继续添加内容

`scrapy startproject tutotial`之后，要用到的就是进sina里面修改了  
其中文件:
- items.py: 修改为需要获得的数据
- pipelines.py: 不管
- settings.py: 设置了获取数据储存的地方,修改`robots`,`user_agent`等
- middlewares.py: 
- spiders/: 真正爬虫代码,可以用xpath,selector等处理,记得放入item中


`scrapy crawl example.py`,spiders文件夹中爬虫代码

Some Problem:
1. 一开始运行完空白,看到debug中返回403,然后到settings.py里修改`user_agent`就好了
2. 然后运行完还是爬不到,在settings把robots.txt修改为False就好了
3. 第三个错误就是xpath写错的原因了,以后注意就行
