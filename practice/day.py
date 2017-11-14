#Day 1 - 搭建开发环境

#确认系统安装的Python版本是3.5.x
#python --version

#用pip安装开发web app需要的第三方库
#异步框架aiohttp: pip install aiohttp
#前端模版引擎jinja2: pip install jinja2
#MySQL 5.x数据库
#MySQL的Python异步驱动程序aiomysql

#项目结构
#backup/：备份目录
#conf/：配置文件
#dist/：打包目录
#www/：web目录，存放.py文件
#iso/：存放iOS App工程
#LICENSE：代码LICENSE

#Day 2 - 编写Web App骨架
#由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py

#Day 3 - 编写ORM
#由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型
#aiomysql为MySQL数据库提供了异步IO驱动
#orm.py

