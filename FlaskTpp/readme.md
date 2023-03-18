# 客户端
= 用户字段
- 字段
- username
- password
- phone
- email
- is_delete
- permission
= 权限设计
- 类似于linux 权限设计
    - 1 2 4 精髓 一个字段可以代表多种全线
    - 多表设计权限设计
        - 用户表
        - 权限表
        - 角色表


# jwt 实现过程
- 用户提交用户名和密码给服务端，如果登录成功，使用jwt创建一个token,并给用户返回
```python
"""
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
"""
```
### jwt 生成的token 是由三段字符串组成， 并且用.连接起来
- 第一段字符串 HEADER, 内部包含算法/token 类型 json字符串然后通过base64 url加密 + 用_替代， /用替换， 加密替换
```python
{
    'alg': 'hs256',
    'typ': 'JWT'
}
```
- 第二段 PAYLOAD,  定义的值同第一段 加密方式
```python
{
    'id': '123324',
    'name': 'zhangsan',
    'exp': 12534324
}
```
- 第三段 第一段密文和第二段的密文用点拼接起来 对结果进行 HS256加密 + 加盐 生成hs256的密文然后在进行base64加密

# 校验 
- 获取token
- 第一步对token 进行切割成三部分
- 把第二段进行 base64url解密 并获取payload 信息检测是否超时 
- 第三步 把第二段和第一段在进行 hs256加密  然后把第三段进行base64解密对比 相同则没有改过token


