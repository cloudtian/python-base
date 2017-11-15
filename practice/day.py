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

#Day 4 - 编写Model
#model.py

#Day 5 - 编写Web框架
#Web框架的设计是完全从使用者出发，目的是让使用者编写尽可能少的代码。
#RequestHandler来封装一个URL处理函数，目的是从URL函数中分析其需要接收的参数，从request中获取必要的参数，调用URL函数
#然后把结果转换为web.Response对象，这样就完全符合aiohttp框架的要求
#add_route函数用来注册一个URL处理函数
#middleware是一种拦截器，一个URL在被某个函数处理前，可以经过一系列的middleware的处理
#coroweb.py
#apis.py
#app.py
#handlers.py

#Day 6 - 编写配置文件
#通常，一个Web App在运行时都需要读取配置文件，比如数据库的用户名、口令等，在不同的环境中运行时，Web App可以通过读取不同的配置文件来获得正确的配置
#config_defalut.py作为开发环境的标准配置，把config_override.py作为生产环境的标准配置，就可以既方便地在本地开发，又可以随时把应用部署到服务器上。
#应用程序读取配置文件需要有限从config_override.py读取。为了简化读取配置文件，可以把所有配置读取到统一的config.py中
