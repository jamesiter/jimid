<p>
<img width="220" height="100" src="./JimID-Logo.jpg">
</p>
[![License](https://img.shields.io/badge/License-GPL3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Format](https://img.shields.io/badge/Format-JSON-blue.svg)](http://www.json.org/json-zh.html)
[![Python versions](https://img.shields.io/badge/Python-2.7.10-blue.svg)](https://www.python.org)
[![API](https://img.shields.io/badge/API-RESTful-blue.svg)](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)


## 项目描述
> JimID，可以把它想象成一个单点登录管理系统。由于传统的单独登陆解决方案过于复杂，所以JimID便由此而生。相比于传统的单点登录方式，JimID有如下特点：
* 纯 HTTP 的交互方式；
* 通过 OpenID 机制，平滑融合工作环境中现存的业务系统；
* 通过对角色的定义，限定用户只能看到自己所属的应用；
* 用户身份验证方式灵活，既可以通过OpenID的方式，也可以直接通过[验证接口](https://github.com/jamesiter/jimid/blob/master/docs/user.md#验证)`/api/user/_auth`来验证用户。

## 未来计划
>
* 弱密码检测；
* 暴力破解防御；
* 基于 Google Authenticator 的 两步验证。


## 安装
### 创建web用户
``` bash
useradd -m www
```

### 创建站点发布目录
``` bash
su - www
mkdir ~/sites
```

### 克隆JimID项目
``` bash
git clone https://github.com/jamesiter/jimid.git ~/sites/jimid
```

### 安装所需库
``` bash
# 创建 python 虚拟环境
virtualenv --system-site-packages venv
# 导入 python 虚拟环境
source ~/venv/bin/activate
# 安装JimID所需扩展库
pip install -r ~/sites/jimid/requirements.txt
# 安装Python连接MySQL的适配器
git clone https://github.com/mysql/mysql-connector-python.git; cd ~/mysql-connector-python; python setup.py install; cd ..; rm -rf mysql-connector-python
```

### 初始化JimID MySQL数据库
``` bash
# 建立JimID数据库专属用户
mysql -u root -pyour_db_password -e 'grant all on jimid.* to jimid@localhost identified by "your_jimid_db_password"; flush privileges'
# 初始化数据库
mysql -u jimid -pyour_jimid_db_password < sites/jimid/misc/init.sql
# 确认是否初始化成功
mysql -u jimid -pyour_jimid_db_password -e 'show databases'
```

### 修改配置文件
配置文件路径：`sites/jimid/config.json`
<br>
**提示：**
> 下表中凸显的配置项，需要用户根据自己的环境手动修改。

|配置项|默认值|说明|
|:--|:--|:--|
|db_name|jimid|数据库名称|
|db_host|localhost|数据库地址|
|db_port|3306|数据库端口|
|db_user|jimid|连接数控的用户名|
|**`db_password`**|jimid.pswd.com|连接数控的密码|
|db_pool_size|10|连接池|
|db_charset|utf8|默认字符集|
|debug|false|是否为调试模式|
|log_cycle|D|日志轮转周期|
|token_ttl|604800|token有效期|
|**`jwt_secret`**||token安全码|
|jwt_algorithm|HS512|token哈希算法|
|SESSION_TYPE|filesystem|session存放类型|
|SESSION_PERMANENT|true|session是否持久化存储|
|SESSION_USE_SIGNER|true|session是否使用并校验签名|
|SESSION_FILE_DIR|../cache|session存放路径|
|SESSION_FILE_THRESHOLD|1000|存放的session超过该数量，之前的将被删除|
|SESSION_COOKIE_NAME|sid|session id在客户端cookie中的存放名称|
|SESSION_COOKIE_SECURE|false|cookie的传输是否只在https的环境中进行|
|**`SECRET_KEY`**||session安全码|
|PERMANENT_SESSION_LIFETIME|604800|cookie在客户端的持久化时间。该值需与token_ttl相同|


### 启动服务
``` bash
# 进入JimID目录
cd ~/sites/jimid
# 启动JimID
gunicorn -c gunicorn_config.py main:app
```


### Nginx 参考配置
``` nginx
    gzip on;
    gzip_min_length 1100;
    gzip_buffers 4 8k;
    gzip_types text/plain application/javascript text/css;

    autoindex off;
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-Content-Type-Options: nosniff;

    server {
        listen 443;
        server_name jimid.your-domain;

        access_log  /var/log/nginx/jimid.access.log;
        error_log  /var/log/nginx/jimid.error.log;

        ssl on;
        ssl_certificate /opt/pki/tls/certs/jimid.your.crt;
        ssl_certificate_key /opt/pki/tls/certs/jimid.your.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers AESGCM:ALL:!DH:!EXPORT:!RC4:+HIGH:!MEDIUM:!LOW:!aNULL:!eNULL;
        ssl_prefer_server_ciphers on;

        root /home/www/sites/jimid/html;

        # 拒绝访问隐藏文件(如：.git、.svn等目录)
        location ~ /\..* {
            return 403;
        }
        location ~ .(sql|py|pyc|ini|conf|log|svn|git|cfg)$ {
            return 403;
        }
        location ~ /$ {
            rewrite http://$host/index.html break;
        }
        location / {
            try_files $uri @inner;
        }

        location @inner {
            proxy_pass         http://127.0.0.1:8001;
            proxy_redirect     off;
            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        }
    }
```


## API
> 默认数据交互格式 Content-Type: application/json

### [状态码参考列表](docs/state_code.md)
### [过滤器操作符原语](docs/filter_primitive.md)
### [用户账号](docs/user.md)
### [用户管理](docs/user_mgmt.md)
### [应用管理](docs/app.md)
### [角色管理](docs/role.md)
### [OpenID](docs/openid.md)
### [OpenID管理](docs/openid_mgmt.md)


## 流程图
* [用户登录](./topology/sign_in.png)
* [资源服务器注册OpenID](./topology/sign_up_openid.png)
* [资源服务器绑定OpenID](./topology/bind_openid.png)
* [资源服务器用户从JimID获取授权](./topology/authorization.png)
* [资源服务器从JimID处验证请求资源的用户合法性](./topology/authentication.png)
* [用户登出](./topology/sign_out.png)


## Web端
[Web端项目地址](https://github.com/jamesiter/jimid-web)


## 问题反馈
[提交Bug](https://github.com/jamesiter/jimid/issues)
<br>
技术交流 QQ 群: 613400104


## 项目成员
<pre>
姓名:    James Iter
E-Mail: james.iter.cn@gmail.com
</pre>


## Web端程序截图
[Web端程序截图](docs/screenshot.md)


## Demo
[demo.jimid.org](https://demo.jimid.org)
<br>
管理员账密 `admin`:`admin`
