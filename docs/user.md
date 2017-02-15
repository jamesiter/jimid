# 用户

## 注册
### 通过登录名注册接口。

``` http
POST https://$domain
  /api/user/_sign_up
{
    "login_name": "james",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|login_name|Y|String|登录名|
|password|Y|String|登录密码|

### 通过手机号码注册接口。

``` http
POST https://$domain
  /api/user/_sign_up_by_mobile_phone
{
    "mobile_phone": "15600000000",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|mobile_phone|Y|String|手机号码|
|password|Y|String|登录密码|

### 通过E-Mail注册接口。

``` http
POST https://$domain
  /api/user/_sign_up_by_email
{
    "email": "james.iter.cn@gmail.com",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|email|Y|String|邮箱地址|
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
        "manager": 0,
        "create_time": 1487054665671808,
        "id": 369,
        "role_id": 0,
        "login_name": "jamesi"
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
|enabled|Y|Boolean|账号是否被启用|
|manager|Y|Boolean|账号是否是管理员|
|role_id|Y|Long|用户角色id|
|create_time|Y|Long|账号创建时间，单位`微秒`|


## 登录
### 用户通过用户名登录。
``` http
POST https://$domain
  /api/user/_sign_in
{
    "login_name": "james",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|login_name|Y|String|登录名|
|password|Y|String|登录密码|

### 用户通过手机号码登录。
``` http
POST https://$domain
  /api/user/_sign_up_by_mobile_phone
{
    "mobile_phone": "15600000000",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|mobile_phone|Y|String|绑定的手机号码|
|password|Y|String|登录密码|

### 用户通过E-Mail登录。
``` http
POST https://$domain
  /api/user/_sign_up_by_email
{
    "email": "james.iter.cn@gmail.com",
    "password": "pswd"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|email|Y|String|绑定的邮箱地址|
|password|Y|String|登录密码|

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```


## 登出
> 用户安全退出。服务器端将删除，该用户在服务器端生成的session文件，并返回一个让客户端浏览器，清除存放自己session id的cookie响应。

``` http
GET https://$domain
  /api/user/_sign_out
Header:
Cookie='cookie'
```

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```


## 验证
> 通过session id自我验证。该接口可用在，客户端已经登录，并获得session id后，需再次验证的情况下。

集成本应用的资源服务器，会通过浏览器获取用户session id。然后资源服务器拿着获取到的用户session id，去JimID服务器验证该用户的合法性。这里用到的验证接口就是该接口。
``` http
GET https://$domain
  /api/user/_auth
Header:
Cookie='cookie'
```

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```


## 获取用户信息
> 获取自己的用户信息

``` http
GET https://$domain
  /api/user
Header:
# 用户session id在cookie里存放着
Cookie='cookie'
```

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
        "manager": 0,
        "create_time": 1487054665671808,
        "id": 369,
        "role_id": 0,
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
|enabled|Y|Boolean|账号是否被启用|
|manager|Y|Boolean|账号是否是管理员|
|role_id|Y|Long|用户角色id|
|create_time|Y|Long|账号创建时间，单位`微秒`|


## 更改用户密码
> 更改自己的登录密码

``` http
PATCH https://$domain
  /api/user/_change_password
Header:
Cookie='cookie'
{
    "password": "new_pswd"
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|password|Y|String|新密码|

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```


## 获取用户应用
> 获取用户所拥有的应用列表

``` http
GET https://$domain
  /api/user/_app_list
Header:
# 用户session id在cookie里存放着
Cookie='cookie'
```

响应示例
``` json
{
    "state": {
        "code": "200",
        "zh-cn": "成功",
        "en-us": "OK"
    },
    "data": [{
        "remark": "Zabbix监控系统",
        "name": "监控系统",
        "home_page": "http://zabbix.iit.im",
        "create_time": 1484623643693070,
        "id": "0I5jpQVYsJ0QNk3f"
    }, {
          ...
    }, {
        "remark": "虚拟化平台",
        "name": "JimV",
        "home_page": "http://v.iit.im",
        "create_time": 1484741145208302,
        "id": "UuAsvSbVTsyHpqvF"
    }]
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|String|应用ID|
|name|Y|String|应用名称|
|home_page|Y|String|应用入口|
|remark|Y|String|备注|
|create_time|Y|Long|应用创建时间，单位`微秒`|


[返回上一级](../README.md)
===
