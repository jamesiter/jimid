# OpenID管理接口

## 更新OpenID
> 更新用户在目标应用下的OpenID。

``` http
PATCH https://$domain
  /api/openid_mgmt/{appid}/{uid}
Header:
Cookie='cookie'
Body:
{
    "openid": "5"
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|appid|Y|String|应用ID|
|uid|Y|Number|用户ID|
|openid|Y|String|将要更新的openid|

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


## 删除OpenID
> 删除用户在目标应用下的OpenID。

``` http
DELETE https://$domain
  /api/openid_mgmt/{appid}/{uid}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|appid|Y|String|应用ID|
|uid|Y|Number|用户ID|

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


## 获取OpenID列表
> 获取OpenID、用户、应用的映射列表

``` http
GET https://$domain
  /api/openids_mgmt?offset={number}&limit={number}
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
        "openid": "5",
        "uid": 706,
        "app": {
            "remark": "",
            "name": "onhPJ4",
            "home_page": "",
            "create_time": 1487236163783548,
            "id": "soCMzyieUlr5HlnL"
        },
        "create_time": 1487236164279760,
        "user": {
            "mobile_phone": "",
            "login_name": "GOPSbw",
            "mobile_phone_verified": 0,
            "email_verified": 0,
            "enabled": 1,
            "id": 706,
            "role_id": 0,
            "manager": 0,
            "create_time": 1487236163876692,
            "email": ""
        },
        "appid": "soCMzyieUlr5HlnL"
    }, {
        "openid": "1",
        "uid": 709,
        "app": {
            "remark": "",
            "name": "y7Y875",
            "home_page": "",
            "create_time": 1487247804049369,
            "id": "iZlcSXzelVJPLQfM"
        },
        "create_time": 1487247804501392,
        "user": {
            "mobile_phone": "",
            "login_name": "YmiHUl",
            "mobile_phone_verified": 0,
            "email_verified": 0,
            "enabled": 1,
            "id": 709,
            "role_id": 0,
            "manager": 0,
            "create_time": 1487247804110509,
            "email": ""
        },
        "appid": "iZlcSXzelVJPLQfM"
    }],
    "paging": {
        "first": "http://jimauth.dev.iit.im/api/openids_mgmt?page=1&page_size=50&order=asc&order_by=create_time",
        "prev": "http://jimauth.dev.iit.im/api/openids_mgmt?page=1&page_size=50&order=asc&order_by=create_time",
        "limit": 50,
        "offset": 0,
        "last": "http://jimauth.dev.iit.im/api/openids_mgmt?page=1&page_size=50&order=asc&order_by=create_time",
        "total": 2,
        "page": 1,
        "page_size": 50,
        "next": "http://jimauth.dev.iit.im/api/openids_mgmt?page=1&page_size=50&order=asc&order_by=create_time"
    }
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|openid|Y|String|OpenID|
|uid|Y|Number|用户ID|
|create_time|Y|Number|创建时间|
|appid|Y|String|应用ID|

字段描述参见 [获取用户信息](user.md#获取用户信息)、[创建应用](app.md#创建应用)


## 全文检索
> 通过全文检索的方式，查找出包含用户关键字的OpenID条目。

``` http
GET https://$domain
  /api/openids_mgmt/_search?keyword=go
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
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
        "openid": "5",
        "uid": 706,
        "app": {
            "remark": "",
            "name": "onhPJ4",
            "home_page": "",
            "create_time": 1487236163783548,
            "id": "soCMzyieUlr5HlnL"
        },
        "create_time": 1487236164279760,
        "user": {
            "mobile_phone": "",
            "login_name": "GOPSbw",
            "mobile_phone_verified": 0,
            "email_verified": 0,
            "enabled": 1,
            "id": 706,
            "role_id": 0,
            "manager": 0,
            "create_time": 1487236163876692,
            "email": ""
        },
        "appid": "soCMzyieUlr5HlnL"
    }],
    "paging": {
        "first": "http://jimauth.dev.iit.im/api/openids_mgmt/_search?page=1&page_size=50&keyword=go&order=asc&order_by=create_time",
        "prev": "http://jimauth.dev.iit.im/api/openids_mgmt/_search?page=1&page_size=50&keyword=go&order=asc&order_by=create_time",
        "limit": 50,
        "offset": 0,
        "last": "http://jimauth.dev.iit.im/api/openids_mgmt/_search?page=1&page_size=50&keyword=go&order=asc&order_by=create_time",
        "total": 1,
        "page": 1,
        "page_size": 50,
        "next": "http://jimauth.dev.iit.im/api/openids_mgmt/_search?page=1&page_size=50&keyword=go&order=asc&order_by=create_time"
    }
}
```

字段描述参见 [获取用户信息](user.md#获取用户信息)、[创建应用](app.md#创建应用)



[返回上一级](../README.md)
===

