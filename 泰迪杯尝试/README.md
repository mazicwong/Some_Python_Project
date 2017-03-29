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


HOW TO SOLVE
- 如何主页爬取到相似URL？
    1. 爬取主页所有url，然后进行遍历，用随机数(may be it can accelerate the proceed..who knows..)
    2. DFS遍历，但是最多深入到三层
    3. 判断方法：在当前url对html进行匹配，看看有没有最初的url，
    有的话就找到标签，然后用bs4的find("",xx.next_siblings)找到兄弟标签，
    接着获取url进行判断，就用正则匹配下是否两个url只有数字不同