# 应用接口

## 创建应用
> 创建一个应用

``` http
POST https://$domain
  /api/app
Header:
Cookie='cookie'
Body:
{
    "name": "OA",
    "home_page": "http://oa.iit.im",
    "remark": "公司办公自动化系统"
}
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|name|Y|String|应用名称|
|home_page|N|String|应用Web入口|
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
        "remark": "公司办公自动化系统",
        "name": "OA",
        "home_page": "http://oa.iit.im",
        "secret": "ti2YUDmCUZjbMUpSkkXgEWj5dZ4Oirhb",
        "create_time": 1487160183392168,
        "id": "mcMzC6CcdIlGamsc"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|String|APP-ID|
|secret|Y|String|APP-Secret|
|name|Y|String|应用名称|
|home_page|Y|String|应用Web入口|
|remark|Y|String|备注|
|create_time|Y|Long|应用创建时间，单位`微秒`|


## 获取应用列表
> 获取系统中所有应用

``` http
GET https://$domain
  /api/apps
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
        "remark": "邮件服务器",
        "name": "邮件系统",
        "home_page": "http://mail.iit.im",
        "secret": "8gUCt1yu3KwSutHGvWTwF5DzKoi9Rpjl",
        "create_time": 1484899404566830,
        "id": "6o3H13DqJOiTu53v"
    }, {
        "remark": "公司办公自动化系统",
        "name": "OA",
        "home_page": "http://oa.iit.im",
        "secret": "ti2YUDmCUZjbMUpSkkXgEWj5dZ4Oirhb",
        "create_time": 1487160183392168,
        "id": "mcMzC6CcdIlGamsc"
    }, {
        "remark": "虚拟化平台",
        "name": "虚拟化平台",
        "home_page": "http://v.iit.im",
        "secret": "qkfNtdoD5qDwCIhPTFDZzCGoBXmBBfJL",
        "create_time": 1484741145208302,
        "id": "UuAsvSbVTsyHpqvF"
    }],
    "paging": {
        "first": "http://jimauth.dev.iit.im/api/app?page=1&page_size=50&filter=&order=asc&order_by=id",
        "prev": "http://jimauth.dev.iit.im/api/app?page=1&page_size=50&filter=&order=asc&order_by=id",
        "limit": 50,
        "offset": 0,
        "last": "http://jimauth.dev.iit.im/api/app?page=1&page_size=50&filter=&order=asc&order_by=id",
        "total": 3,
        "page": 1,
        "page_size": 50,
        "next": "http://jimauth.dev.iit.im/api/app?page=1&page_size=50&filter=&order=asc&order_by=id"
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

应用信息字段描述参见 [创建应用](app.md#创建应用)


## 全文检索
> 检索出包含关键字的应用。

``` http
GET https://$domain
  /api/apps/_search?keyword=oa
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
        "remark": "公司办公自动化系统",
        "name": "OA",
        "home_page": "http://oa.iit.im",
        "secret": "ti2YUDmCUZjbMUpSkkXgEWj5dZ4Oirhb",
        "create_time": 1487160183392168,
        "id": "mcMzC6CcdIlGamsc"
    }],
    "paging": {
        "total": 1,
        "last": "http://jimauth.dev.iit.im/api/apps/_search?page=1&page_size=50&keyword=oa&order=asc&order_by=id",
        "page_size": 50,
        "next": "http://jimauth.dev.iit.im/api/apps/_search?page=1&page_size=50&keyword=oa&order=asc&order_by=id",
        "limit": 50,
        "offset": 0,
        "prev": "http://jimauth.dev.iit.im/api/apps/_search?page=1&page_size=50&keyword=oa&order=asc&order_by=id",
        "page": 1,
        "first": "http://jimauth.dev.iit.im/api/apps/_search?page=1&page_size=50&keyword=oa&order=asc&order_by=id"
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

应用信息字段描述参见 [创建应用](app.md#创建应用)


## 更新应用信息
> 更新指定应用的信息。

``` http
PATCH https://$domain
  /api/app/{id}
Header:
Cookie='cookie'
Body:
{
    "secret": True,
    "name": "新应用",
    "home_page": "http://new.iit.im",
    "remark": "新的应用"
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|String|将要更新的应用ID|
其它字段都是可选, 详细描述参见 [创建应用](app.md#创建应用)

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


## 删除应用
> 删除指定应用.

``` http
DELETE https://$domain
  /api/app/{id}
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|id|Y|String|将要删除的应用ID|

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
