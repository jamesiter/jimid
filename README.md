<p>
<img width="220" height="100" src="./JimID-Logo.jpg">
</p>
[![License](https://img.shields.io/badge/License-GPL3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Format](https://img.shields.io/badge/Format-JSON-blue.svg)](http://www.json.org/json-zh.html)
[![Python versions](https://img.shields.io/badge/Python-2.7.10-blue.svg)](https://www.python.org)
[![API](https://img.shields.io/badge/API-RESTful-blue.svg)](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)

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

## 项目成员
<pre>
姓名:    James Iter
E-Mail: james.iter.cn@gmail.com
</pre>

Demo
