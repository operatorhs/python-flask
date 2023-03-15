# 环境变量
- 系统级别
- /etc/envirtonment
- /etc/profile

# 用户级别
- ~/.bashrc

# 临时级
- 在窗口中直接export

# 公司开发环境
- 开发环境
  开发人员使用
- 测试环境
  测试人员使用

- 演示环境
  产品经理查看
  做演习， 彩排

- 生产环境、线上环境
  真是环境
  给用户看的

odoo

converter

# Flask 四大内置对象
- Request
    - request
- Session
    - session
-G
    g
- Config
    模版中 config
    python 对象中 app.config


- Request
 - args 请求参数
    query_params
    query_string
    get请求参数
    他并不是get 专属，所有请求都能获得这个参数
 - form 
    表单数据
    post 请求参数
     - 直接支持put patch
 都是 ImmutableMultiDict
 
 @app.errorhandler
 
 # Flask-session
   - 实现了服务端 session
   - 将数据存储在服务端， 将数据对应的key存储在cookie中
   - flask-session sesion 存储时间为31天


# 模型继承
    - 默认继承并不会报错
    需要 __abstract__

# Flask-RESTful

## 输出
- 默认输出字典， 可以直接进行序列化
- 如果包含对象
    - 默认会抛出异常， 对象不可JSON序列化
- 使用格式化工具
    - marshal 函数
    - marshal_with 装饰器
    - 条件
        - 格式
            - 字典geshi
            - 允许嵌套
            - value 是fields.xxx
        - 数据
            - 允许任何格式
        - 如果格式和数据完全对应， 数据就是预期格式
        - 如果比格式化字段多，程序依然正常运行， 不存在的字段是默认值
        - 如果格式化比数据中的字段少，程序正常执行， 少的字段不会显示
            

