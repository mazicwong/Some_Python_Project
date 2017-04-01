# explanation about
### in Python 3.5
- **数据爬取  未去标签**
    - saveFile
    - saveFail
    - getHtml
    - getUrl
    
- **数据爬取  去除标签**
    - replaceCharEntity
    - repalce
    - saveFile
    - get_localfile

- **爬取相邻url用于去重**
    - 考虑添加功能=>判断html总长与原来文本进行对比，避免爬到死链
        - 长度相差大于70%？
    - getHtml
        - RETURN  True/False AND url_data
    - getSimilarHtml
        - FIND the root_url AND get other url among it AND compare it with the previous one


Get the similar URL
- 如何主页爬取到相似URL？
    1. 爬取主页所有url，然后进行遍历，用随机数(may be it can accelerate the proceed..who knows..)
    2. DFS遍历，但是最多深入到三层
    3. 判断方法：在当前url对html进行匹配，看看有没有最初的url，
    有的话就找到标签，然后用bs4的find("",xx.next_siblings)找到兄弟标签，
    接着获取url进行判断，就用正则匹配下是否两个url只有数字不同
    
- A new method?
    1. try guessing the regular expression of the existing URL,
    and then get the root_html from the root_url,so that I can match what I want,
    which means its format are familiar with the exist one,
    from the html source I have already had.
- 最终实现方式
    1. 根据已有的URL获得主页的html
    2. 然后由URL推导出相同格式的正则表达式
    3. 在主页的html中匹配我的正则表达式，获得相似URL
- 几个坑
    1. 反向推导正则的时候，因为最终是得到string类型的pattern，
    所以要用p1 = p1.encode(encoding="utf-8")转换为bytes类型，
    2. 在推导正则时，如果用p1=r'http://www.baidu.com/\d\d[a-z]',
    接下来在做编码的时候，\d会变成\\d，且由于加了r取消掉转义字符，
    会导致匹配结果错误，还有一点就是最后有一个换行，用str=str[:-1]删掉，以后应该注意
    3. 判断字符串的每个字符，不能用isalpha和isnum，因为全都是字符
    4. 添加功能：已经存在且不为0的文档就不重复爬取