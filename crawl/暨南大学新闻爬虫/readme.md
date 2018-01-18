
### JNU学生荟萃板块爬虫
    *采用scrapy*
	URL : https://news.jnu.edu.cn/xshc/ll

#### 使用方式
    `scrapy startproject jnuxshc`之后，要用到的就是进sina里面修改了  
    `scrapy crawl mazic.py`,spiders中爬虫代码,这里用`main.py`来执行了  
    *最终接口*,调用`python3 main.py`,会得到一个`jnu.csv`的文件

#### 需要修改的文件:
	- items.py: 修改为需要获得的数据
	- pipelines.py: 暂时不管
	- settings.py: 数据存储的地方和格式,修改`robots`,`user_agent`
	- middlewares.py: 暂时不管
	- spiders/***.py: 真正爬虫代码,可以用xpath,selector等处理,记得放入item中


#### Some Problem:
	1. 一开始运行完空白,看到debug中返回403,然后到settings.py里修改`user_agent`就好了
	2. 然后运行完还是爬不到,在settings把robots.txt修改为False就好了
	3. 第三个错误就是xpath写错的原因了,以后注意就行
	4. 由于输出到csv的列是无序的,所以在spiders/中加了`csv_item_exporter.py`,在`settings.py`中添加了`FEED_EXPORTERS`和`FIELDS_TO_EXPORT`

