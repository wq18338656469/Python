"""
登录验证

"""
username = input('请输入用户的姓名：')
password = input('请输入密码：')
# 用户名是abc且密码是123456则身份验证成功否则身份验证失败
if username == 'abc' and password == '123456':
    print('successful')
else:
    print('false')
