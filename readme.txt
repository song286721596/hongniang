1.本案例是抓取www.hongniang.com上的女性用户的一些信息
2.运行本案例前提：本机安装Mongodb，mysql，redis
3.打开本地redis服务， redis-server redis-windows.conf
4.运行程序步骤：进入hongniang\hongniang\spiders目录下，启动命令：scrapy runspider hn.py
5.在redis下键入命令：redis-cli，然后键入：lpush hn:start_urls https://www.hongniang.com/index/search?&sex=2&starage=2&page=1
6.这时回到第4步的窗口下，能看到在抓取相关信息的日志
7.这时候使用RedisDesktopManager登录本地redis中，可以查看到抓取的信息（hn:items）
8.将redis中的信息写入到mongodb中，可以进入hongniang目录下，启动程序：python process_item_for_mongodb.py，执行后能看到写入到mongodb数据库中
9.将redis中的信息写入到mysql中，可以进入hongniang目录下，启动程序：python process_item_for_mysql.py，执行后能看到写入到mysql数据库中