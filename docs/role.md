# 角色接口

## 创建角色
> 创建一个角色

``` http
POST https://$domain
  /api/role
Header:
Cookie='cookie'
Body:
{
    "name": "IT",
    "remark": "信息技术部"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|name|Y|String|角色名称|
|remark|N|String|备注|

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    },
    "data": {
        "remark": "信息技术部",
        "id": 5,
        "name": "IT"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|Long|角色ID|
|name|Y|String|角色名称|
|remark|Y|String|备注|


## 获取角色列表
> 获取系统中所有角色

``` http
GET https://$domain
  /api/roles
Header:
Cookie='cookie'
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
        "remark": "运维",
        "id": 3,
        "name": "OM"
    }, {
        "remark": "人事",
        "id": 4,
        "name": "HR"
    }, {
        "remark": "信息技术部",
        "id": 5,
        "name": "IT"
    }],
    "paging": {
        "first": "http://jimauth.dev.iit.im/api/role?page=1&page_size=50&filter=&order=asc&order_by=id",
        "prev": "http://jimauth.dev.iit.im/api/role?page=1&page_size=50&filter=&order=asc&order_by=id",
        "limit": 50,
        "offset": 0,
        "last": "http://jimauth.dev.iit.im/api/role?page=1&page_size=50&filter=&order=asc&order_by=id",
        "total": 3,
        "page": 1,
        "page_size": 50,
        "next": "http://jimauth.dev.iit.im/api/role?page=1&page_size=50&filter=&order=asc&order_by=id"
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

应用信息字段描述参见 [创建角色](role.md#创建角色)


## 获取指定角色的应用
> 通过角色ID获取所属应用列表

``` http
GET https://$domain
  /api/roles/_get_app_by_role_id/{role_id}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|role_id|Y|Number|角色ID|

响应示例
``` json
{
    "state": {
        "code": "200",
        "zh-cn": "成功",
        "en-us": "OK"
    },
    "data": [{
        "remark": "修改备注",
        "name": "第一个应用",
        "home_page": "http://www.iit.im",
        "create_time": 1484623643693070,
        "id": "0I5jpQVYsJ0QNk3f"
    }, {
        "remark": "zabbix监控系统",
        "name": "ZABBIX",
        "home_page": "http://zabbix.iit.im",
        "create_time": 1484899430368602,
        "id": "6HRh4tuDVuYS4QPF"
    }, {
        "remark": "虚拟化平台",
        "name": "虚拟化平台",
        "home_page": "http://v.iit.im",
        "create_time": 1484741145208302,
        "id": "UuAsvSbVTsyHpqvF"
    }]
}
```

字段描述参见 [创建应用](app.md#创建应用)


## 获取角色本身，及其所关联的用户和应用
> 获取角色本身，及其所关联的用户和应用

``` http
GET https://$domain
  /api/roles/_get_user_role_app_mapping
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
        "users": [{
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
        }, {
          ...
        }, {
            "mobile_phone": "",
            "login_name": "james106",
            "mobile_phone_verified": 0,
            "email_verified": 0,
            "enabled": 1,
            "id": 201,
            "role_id": 3,
            "manager": 0,
            "create_time": 1482153107852822,
            "email": ""
        }],
        "remark": "运维",
        "apps": [{
            "remark": "修改备注",
            "name": "第一个应用",
            "home_page": "http://www.iit.im",
            "create_time": 1484623643693070,
            "id": "0I5jpQVYsJ0QNk3f"
        }, {
            "remark": "zabbix监控系统",
            "name": "ZABBIX",
            "home_page": "http://zabbix.iit.im",
            "create_time": 1484899430368602,
            "id": "6HRh4tuDVuYS4QPF"
        }, {
            "remark": "虚拟化平台",
            "name": "虚拟化平台",
            "home_page": "http://v.iit.im",
            "create_time": 1484741145208302,
            "id": "UuAsvSbVTsyHpqvF"
        }],
        "id": 3,
        "name": "OM"
    }, {
        "users": [{
            "mobile_phone": "",
            "login_name": "james14",
            "mobile_phone_verified": 0,
            "email_verified": 0,
            "enabled": 1,
            "id": 153,
            "role_id": 4,
            "manager": 0,
            "create_time": 1482152727408620,
            "email": ""
        }, {
          ...
        }, {
            "mobile_phone": "",
            "login_name": "james104",
            "mobile_phone_verified": 0,
            "email_verified": 0,
            "enabled": 1,
            "id": 199,
            "role_id": 4,
            "manager": 0,
            "create_time": 1482153107773494,
            "email": ""
        }],
        "remark": "人事",
        "apps": [],
        "id": 4,
        "name": "HR"
    }, {
        "users": [],
        "remark": "信息技术部",
        "apps": [],
        "id": 5,
        "name": "IT"
    }],
    "paging": {
        "total": 3
    }
}
```

字段描述参见 [获取用户信息](user.md#获取用户信息)、[创建应用](app.md#创建应用)、[创建角色](role.md#创建角色)


## 更新角色信息
> 更新指定角色的信息。

``` http
PATCH https://$domain
  /api/role/{role_id}
Header:
Cookie='cookie'
Body:
{
    "name": "DevOps",
    "remark": "运维开发部"
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|role_id|Y|Number|将要更新的角色ID|
其它字段都是可选, 详细描述参见 [创建角色](role.md#创建角色)

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


## 删除角色
> 删除指定角色。角色删除时，会把所依赖的用户标识、映射的应用都初始化和清空。

``` http
DELETE https://$domain
  /api/role/{role_id}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|role_id|Y|Number|将要删除的角色ID|

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


## 添加角色到用户
> 给指定角色添加一个用户。

``` http
POST https://$domain
  /api/role/_add_user_to_role/{role_id}/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|role_id|Y|Number|将要添加用户到此角色的角色ID|
|uid|Y|Number|将要添加到此角色的用户ID|

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


## 从角色中把用户删除
> 把指定用户从此角色中删除。

``` http
DELETE https://$domain
  /api/role/_delete_user_from_role/{role_id}/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|role_id|Y|Number|将要把用户从此角色中删除。角色ID|
|uid|Y|Number|将要删除此角色中的用户。用户ID|

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


## 给角色添加应用
> 给指定角色添加一个应用。

``` http
POST https://$domain
  /api/role/_add_app_to_role/{role_id}/{appid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|role_id|Y|Number|将要添加应用到此角色的角色ID|
|appid|Y|Number|将要添加应用到此角色的应用ID|

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


## 从角色中删除应用
> 把指定应用从此角色中删除。

``` http
DELETE https://$domain
  /api/role/_delete_app_from_role/{role_id}/{appid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|role_id|Y|Number|将要把用户从此角色中删除。角色ID|
|appid|Y|String|将要删除此角色中的应用。应用ID|

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


## 查找自由用户
> 模糊查找不属于任何角色的用户

``` http
GET https://$domain
  /roles/_search_with_free_users?page=1&page_size=2&keyword=james16
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|keyword|N|String|全文检索的关键字|
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
        "login_name": "james160",
        "mobile_phone_verified": 0,
        "email_verified": 0,
        "enabled": 1,
        "id": 255,
        "role_id": 0,
        "manager": 0,
        "create_time": 1482153110341713,
        "email": ""
    }, {
        "mobile_phone": "",
        "login_name": "james161",
        "mobile_phone_verified": 0,
        "email_verified": 0,
        "enabled": 1,
        "id": 256,
        "role_id": 0,
        "manager": 0,
        "create_time": 1482153110387360,
        "email": ""
    }],
    "paging": {
        "total": 9,
        "last": "http://jimauth.dev.iit.im/api/roles/_search_with_free_users?page=5&page_size=2&keyword=james16&order=asc&order_by=id",
        "page_size": 2,
        "next": "http://jimauth.dev.iit.im/api/roles/_search_with_free_users?page=2&page_size=2&keyword=james16&order=asc&order_by=id",
        "limit": 2,
        "offset": 0,
        "prev": "http://jimauth.dev.iit.im/api/roles/_search_with_free_users?page=1&page_size=2&keyword=james16&order=asc&order_by=id",
        "page": 1,
        "first": "http://jimauth.dev.iit.im/api/roles/_search_with_free_users?page=1&page_size=2&keyword=james16&order=asc&order_by=id"
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


[返回上一级](../README.md)
===
