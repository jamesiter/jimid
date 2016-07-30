# 账号
--

## 注册
---
> 用户注册接口

``` http
POST http://$domain
  /auth/_sign_up
{
    "login_name": "james",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|login_name|Y|String|登录名|
|password|Y|String|登录密码|

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    },
    "data": {
        "mobile_phone": "",
        "mobile_phone_verified": 0,
        "email_verified": 0,
        "enabled": 1,
        "email": "",
        "create_time": 1469902398631608,
        "id": 529,
        "login_name": "james"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|Long|账号ID|
|login_name|Y|String|用户登录名|
|mobile_phone|Y|String|用户手机号码|
|mobile_phone_verified|Y|Boolean|经校验的用户手机号码|
|email|Y|String|用户电子邮箱地址|
|email_verified|Y|Boolean|经校验的用户电子邮箱地址|
|create_time|Y|Long|账号创建时间，单位`微秒`|

## 登录
## 登出
## 验证
## 获取用户信息
## 更改用户密码
## 获取用户列表
