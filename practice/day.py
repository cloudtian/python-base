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
#config.py
#config_default.py
#config_override.py

#Day 7 - 编写MVC
#ORM框架，Web框架和配置已就绪，可以开始编写一个最简单的MVC，把它们全部启动起来
#handlers.py

#Day 8 - 构建前端
#引入uikit框架的样式
#添加__base__.html, blogs.html

#Day 9 - 编写API
#REST(Representational State Transfer)风格的软件架构模式
#REST是一种设计API的模式。最常用的数据格式是JSON.由于JSON能直接被JavaScript读取，所以，以JSON格式编写的REST风格的API具有简单，易读，易用的特点。
#由于API就是把Web App的功能全部封装了，所以通过API操作数据，可以极大地前后端代码分离，使得后端代码易于测试，前端代码编写更简单。
#一个API也是一个URL的处理函数，通过@api把函数变成JSON格式的REST API
#handlers.py  /api/users

#Day 10 - 用户注册和登录
#注意用户口令是客户端传递的经过SHA1计算后的40位Hash字符串，所以服务器端并不知道用户的原始口令
#用户注册register.html
#用户登录比用户注册复杂。由于HTTP协议是一种无状态协议，而服务器要跟踪用户状态，就只能通过cookie实现。
#大多数的Web框架提供了Session功能来封装保存用户状态的cookie
#Session的优点是简单易用，可以直接从Session中取出用户登录信息。

#Session的缺点是服务器需要在内存中维护一个映射表来存储用户登录信息，如果有两台以上服务器，就需要对Session做集群，因此，使用Session的Web App很难扩展
#我们采用直接读取cookie的方式来验证用户登录，每次用户访问任意URL，都会对cookie进行验证，这种方式的好处是保证服务器处理任意的URL都是无状态的，可以扩展到多台服务器
#由于登录成功后是由服务器生成一个cookie发送给浏览器，所以，要保证这个cookie不会被客户端伪造出来.
#实现防伪造cookie的关键是通过一个单向算法（例如SHA1），举例如下:
#当用户输入了正确的口令登录成功后，服务器可以从数据库取到用户的id，并按照如下方式计算出一个字符串：
#"用户id" + "过期时间" + SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")
#当浏览器发送cookie到服务器端后，服务器可以拿到的信息包括：用户id,过期时间，SHA1值
#如果未到过期时间，服务器就根据用户id查找用户口令，并计算：
#SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")
#并与浏览器cookie中的MD5进行比较，如果相等，则说明用户已登录，否则，cookie就是伪造的。
#这个算法的关键在于SHA1是一种单向算法，即可以通过原始字符串计算出SHA1结果，但无法通过SHA1结果反推出原始字符串。


