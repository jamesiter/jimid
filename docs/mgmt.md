# 管理接口
## 获取用户列表
---
> 获取用户列表

``` http
GET https://$domain
  /auth/_list?offset={number}&limit={number}
  or
  /auth/_list?page={number}&page_size={number}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|offset|N|Number|偏移量, 默认值0|
|limit|N|Number|返回条目数量, 默认值50|
|page|N|Number|页号, 与offset同时存在时, 以offset为准, 默认值1|
|page_size|N|Number|页大小, 默认值50|

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    },
    "data": [{
        "mobile_phone": "",
        "mobile_phone_verified": 0,
        "email_verified": 0,
        "enabled": 1,
        "login_name": "james10",
        "email": "",
        "create_time": 1470020252554296,
        "password": "ji_pbkdf2$sha1$1000$1eG0j9ETrTsGyECixXCwjA97bADEJIn9$f7796bed7d3b1c1ac1e32bbe9adce47b539556af",
        "id": 539
    }, {
          ...
    }, {
        "mobile_phone": "",
        "mobile_phone_verified": 0,
        "email_verified": 0,
        "enabled": 1,
        "login_name": "james14",
        "email": "",
        "create_time": 1470020252702894,
        "password": "ji_pbkdf2$sha1$1000$oHh9Yhn8FtDeAAn0pF3j4ioBUCtCSApr$d40b3dd48091c0ca16ec3c220ca4075e740ba2db",
        "id": 543
    }],
    "paging": {
        "total": 20,
        "limit": 5,
        "offset": 10,
        "page": 1,
        "page_size": 10
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|total|Y|Long|用户总量|
|offset|Y|Long|当前偏移量|
|limit|Y|Long|返回条目数量|
|page|Y|Long|透传客户端请求的该参数, 如果没有传递, 则返回默认值1|
|page_size|Y|Long|透传客户端请求的该参数, 如果没有传递, 则返回默认值 50|

用户信息字段描述参见 [获取用户信息](auth.md#获取用户信息)

## 通过用户登录名获取用户信息
---
> 获取用户信息

``` http
GET https://$domain
  /mgmt/_by_login_name/{login_name}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|login_name|Y|String|将获取用户信息的登录名称|

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
        "create_time": 1470022570532929,
        "id": 549,
        "login_name": "james"
    }
}
```

字段描述参见 [获取用户信息](auth.md#获取用户信息)

## 禁用用户账号
---
> 禁用掉的账号将不允许登录, 且通过不了验证. 管理员无法自我禁用.
``` http
PATCH https://$domain
  /mgmt/_disable/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|uid|Y|Number|将要禁用的账号ID|

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
---
> 启用已禁用的账号
``` http
PATCH https://$domain
  /mgmt/_enable/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--|:--|
|uid|Y|Number|将要解禁的账号ID|

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
---
> 删除账号. 管理员无法自我删除.
``` http
DELETE https://$domain
  /mgmt/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|uid|Y|Number|将要删除的用户账号ID|

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

## 更新账号信息
---
> 更新账号. 不支持普通用户自我更新, 普通用户更新各字段, 将有专门的接口
``` http
PUT https://$domain
  /auth/_update
Header:
Cookie='cookie'
{
    "id": 768,
    "login_name": "new_login_name",
    "mobile_phone": "15601603670",
    "mobile_phone_verified": true,
    "email": "jimit@qq.com",
    "email_verified": true
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|Number|将要更新的用户账号ID|
其它字段都是可选, 详细描述参见 [获取用户信息](auth.md#获取用户信息)

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

[返回上一级](../README.md)
===
