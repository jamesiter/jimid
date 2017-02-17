# OpenID

## 注册
### OpenID由JimID生成，并关联到与该用户相关的应用。

``` http
GET https://$domain
  /api/openid/_sign_up?appid=s65I5QXsXBGsxKyt&ts=1487297863&redirect_url=http://service.iit.im&sign=e60ab663ebb98a1d94d1163c7cfb234dadae0e13
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|appid|Y|String|APP-ID|
|ts|Y|Number|当前时间戳|
|redirect_url|Y|String|应用服务器回调地址|
|sign|Y|String|用APP-SECRET对本次请求的签名|

响应示例
``` json
{
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    },
    "redirect": {
        "code": "302",
        "location": "http://service.iit.im?openid=Zq8qa9JOUxxXuu6ipyh4xaKz9au4kL&code=20000&sign=d649fc312a079671e7bd01d345171ffe97bdb359&sid=09419e09-43f3-446b-9f5f-f83efdfc298b.xHVKdGXDrDfZKTd37zyP6fHcopI"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|redirect["code"]|Y|Number|客户端浏览器需要解析的HTTP状态码|
|redirect["location"]|Y|String|客户端浏览器重新|
|openid|Y|String|JimID生成给该用户在应用服务器的用户ID|
|code|Y|String|传给应用服务器的本次请求状态码，应用服务器根据该状态码，能知道是否执行成功|
|sign|Y|String|签名|
|sid|Y|String|该用户的session id|


## 绑定
### 绑定由应用服务器提供的OpenID到JimID，并关联到与该用户相关的应用。

``` http
GET https://$domain
  /api/openid/_bind?appid=s65I5QXsXBGsxKyt&ts=1487297863&openid=1&redirect_url=http://service.iit.im&sign=cebb36ec969ff3f3eb12224f67afeed0013cd678
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|appid|Y|String|APP-ID|
|ts|Y|Number|当前时间戳|
|redirect_url|Y|String|应用服务器回调地址|
|sign|Y|String|用APP-SECRET对本次请求的签名|

响应示例
``` json
{
    "redirect": {
        "code": "302",
        "location": "http://service.iit.im?openid=1&code=20000&sign=4f8845636dfcbb66b0cfdd575f0387c452d03ed5&sid=09419e09-43f3-446b-9f5f-f83efdfc298b.xHVKdGXDrDfZKTd37zyP6fHcopI"
    },
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|redirect["code"]|Y|Number|客户端浏览器需要解析的HTTP状态码|
|redirect["location"]|Y|String|客户端浏览器重新|
|openid|Y|String|JimID生成给该用户在应用服务器的用户ID|
|code|Y|String|传给应用服务器的本次请求状态码，应用服务器根据该状态码，能知道是否执行成功|
|sign|Y|String|签名|
|sid|Y|String|该用户的session id|


## 解绑
### 解除该用户此应用在JimID的OpenID绑定。

``` http
GET https://$domain
  /api/openid/_unbind?appid=s65I5QXsXBGsxKyt&ts=1487297863&redirect_url=http://service.iit.im&sign=2f8bb25917cfd68937fdec3f64d20e5beeb3eea7
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|appid|Y|String|APP-ID|
|ts|Y|Number|当前时间戳|
|redirect_url|Y|String|应用服务器回调地址|
|sign|Y|String|用APP-SECRET对本次请求的签名|

响应示例
``` json
{
    "redirect": {
        "code": "302",
        "location": "http://service.iit.im?code=20000&sign=73b186ef3a898b2f4cc88e0ec85515a45f69ba8a"
    },
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|redirect["code"]|Y|Number|客户端浏览器需要解析的HTTP状态码|
|redirect["location"]|Y|String|客户端浏览器重新|
|openid|Y|String|JimID生成给该用户在应用服务器的用户ID|
|code|Y|String|传给应用服务器的本次请求状态码，应用服务器根据该状态码，能知道是否执行成功|
|sign|Y|String|签名|
|sid|Y|String|该用户的session id|


## 验证
### 验证该用户在JimID，拥有该应用的OpenID。验证通过后，对应的OpenID会随响应返回。

``` http
GET https://$domain
  /api/openid/_auth?appid=s65I5QXsXBGsxKyt&ts=1487297863&redirect_url=http://service.iit.im&sign=a13676b5f8fe3cdc86ffdec53cfffef14f4fa49b
Header:
Cookie='cookie'
```

|参数名称|必须|类型|说明|
|:--:|:--:|:--:|:--:|
|appid|Y|String|APP-ID|
|ts|Y|Number|当前时间戳|
|redirect_url|Y|String|应用服务器回调地址|
|sign|Y|String|用APP-SECRET对本次请求的签名|

响应示例
``` json
{
    "redirect": {
        "code": "302",
        "location": "http://service.iit.im?openid=1&code=20000&sign=4f8845636dfcbb66b0cfdd575f0387c452d03ed5&sid=09419e09-43f3-446b-9f5f-f83efdfc298b.xHVKdGXDrDfZKTd37zyP6fHcopI"
    },
    "state": {
        "en-us": "OK",
        "zh-cn": "成功",
        "code": "200"
    }
}
```

|参数名称|必须|类型|说明|
|:--|:--:|:--:|:--|
|redirect["code"]|Y|Number|客户端浏览器需要解析的HTTP状态码|
|redirect["location"]|Y|String|客户端浏览器重新|
|openid|Y|String|JimID生成给该用户在应用服务器的用户ID|
|code|Y|String|传给应用服务器的本次请求状态码，应用服务器根据该状态码，能知道是否执行成功|
|sign|Y|String|签名|
|sid|Y|String|该用户的session id|