# 用户管理接口

## 获取指定用户信息
> 通过用户ID获取用户信息

``` http
GET https://$domain
  /api/user_mgmt/{uid}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|uid|Y|Number|将获取用户信息的用户ID|

响应示例
``` json
{
    "state": {
        "code": "200",
        "zh-cn": "成功",
        "en-us": "OK"
    },
    "data": {
        "mobile_phone": "93939932999",
        "mobile_phone_verified": 1,
        "email_verified": 0,
        "enabled": 1,
        "login_name": "james1",
        "email": "",
        "manager": 0,
        "create_time": 1482152726801783,
        "role_id": 3,
        "id": 140
    }
}
```

字段描述参见 [获取用户信息](user.md#获取用户信息)


## 通过用户登录名获取用户信息
> 获取用户信息

``` http
GET https://$domain
  /api/user_mgmt/_by_login_name/{login_name}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|login_name|Y|String|将获取用户信息的登录名称|

响应示例
``` json
{
    "state": {
        "code": "200",
        "zh-cn": "成功",
        "en-us": "OK"
    },
    "data": {
        "mobile_phone": "93939932999",
        "mobile_phone_verified": 1,
        "email_verified": 0,
        "enabled": 1,
        "login_name": "james1",
        "email": "",
        "manager": 0,
        "create_time": 1482152726801783,
        "role_id": 3,
        "id": 140
    }
}
```

字段描述参见 [获取用户信息](user.md#获取用户信息)


## 禁用用户账号
> 禁用掉的账号将不允许登录, 且通过不了验证. 管理员无法自我禁用.

``` http
PATCH https://$domain
  /api/user_mgmt/_disable/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|uid|Y|Number|将要禁用的用户ID|

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


## 启用用户账号
> 启用已禁用的账号

``` http
PATCH https://$domain
  /api/user_mgmt/_enable/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--|:--|
|uid|Y|Number|将要解禁的用户ID|

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


## 删除用户账号
> 删除账号. 管理员无法自我删除.

``` http
DELETE https://$domain
  /api/user_mgmt/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|uid|Y|Number|将要删除的用户ID|

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


## 更新用户账号信息
> 更新账号信息. 不支持普通用户自我更新, 普通用户更新各字段, 将有专门的接口

``` http
PUT https://$domain
  /api/user_mgmt/_update/{uid}
Header:
Cookie='cookie'
{
    "login_name": "new_login_name",
    "mobile_phone": "15600000000",
    "mobile_phone_verified": true,
    "email": "jimit@qq.com",
    "email_verified": true
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|Number|将要更新的用户ID|
其它字段都是可选, 详细描述参见 [获取用户信息](user.md#获取用户信息)

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


## 更改指定用户密码
> 超级用户更改指定用户的登录密码

``` http
PATCH https://$domain
  /api/user_mgmt/_change_password/{uid}
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


## 获取用户列表
> 获取用户列表

``` http
GET https://$domain
  /api/users_mgmt?offset={number}&limit={number}
  or
  /api/users_mgmt?page={number}&page_size={number}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|offset|N|Number|偏移量, 默认值0|
|limit|N|Number|返回条目数量, 默认值50|
|page|N|Number|页号, 与offset同时存在时, 以offset为准, 默认值1|
|page_size|N|Number|页大小, 默认值50|
|order_by|N|String|所依据的字段|
|order|N|Enum|排序策略，`asc`\|`desc`|

响应示例
``` json
{
    "state": {
        "code": "200",
        "zh-cn": "成功",
        "en-us": "OK"
    },
    "data": [{
        "mobile_phone": "",
        "login_name": "admin",
        "mobile_phone_verified": 0,
        "email_verified": 0,
        "enabled": 1,
        "id": 1,
        "role_id": 0,
        "manager": 1,
        "create_time": 1479283506000000,
        "email": ""
    }, {
          ...
    }, {
        "mobile_phone": "93939932999",
        "login_name": "james1",
        "mobile_phone_verified": 1,
        "email_verified": 0,
        "enabled": 1,
        "id": 140,
        "role_id": 3,
        "manager": 0,
        "create_time": 1482152726801783,
        "email": ""
    }],
    "paging": {
        "first": "https://$domain/api/users_mgmt?page=1&page_size=2&filter=&order=asc&order_by=id",
        "prev": "https://$domain/api/users_mgmt?page=1&page_size=2&filter=&order=asc&order_by=id",
        "limit": 2,
        "offset": 0,
        "last": "https://$domain/api/users_mgmt?page=75&page_size=2&filter=&order=asc&order_by=id",
        "total": 149,
        "page": 1,
        "page_size": 2,
        "next": "https://$domain/api/users_mgmt?page=2&page_size=2&filter=&order=asc&order_by=id"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|total|Y|Number|用户总量|
|offset|Y|Number|当前偏移量|
|limit|Y|Number|返回条目数量|
|page|Y|Number|透传客户端请求的该参数, 如果没有传递, 则返回默认值1|
|page_size|Y|Number|透传客户端请求的该参数, 如果没有传递, 则返回默认值 50|

用户信息字段描述参见 [获取用户信息](user.md#获取用户信息)


## 批量更新用户信息
> 批量更新用户信息

``` http
PATCH https://$domain
  /api/users_mgmt
Header:
Cookie='cookie'
{
    "ids": "1,2,3"
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|ids|Y|String|欲更新的用户ID列表，以`,`为分隔符|
|mobile_phone_verified|N|Boolean|经校验的用户手机号码|
|email_verified|N|Boolean|经校验的用户电子邮箱地址|
|enabled|N|Boolean|账号是否被启用|
|role_id|N|Long|用户角色id|

响应示例
``` json
{
    "state": {
        "code": "200",
        "zh-cn": "成功",
        "en-us": "OK"
    }
}
```


[返回上一级](../README.md)
===
