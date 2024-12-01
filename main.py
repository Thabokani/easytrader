import easytrader
user = easytrader.use('universal_client')

# 在这个文件里填入账号密码
user.prepare('client_config.json')

print(user.balance)
user.buy('000001', price=11.00, amount=100)
