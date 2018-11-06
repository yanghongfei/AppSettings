### AppSettings
- 用途：项目中settings配置文件信息
- 第一次使用请先修改`settings.py`数据库配置，和`models.py` 中`init_db`初始化数据库

#### 表结构
```mysql=
+-----------+--------------+------+-----+-------------------+-----------------------------+
| Field     | Type         | Null | Key | Default           | Extra                       |
+-----------+--------------+------+-----+-------------------+-----------------------------+
| id        | int(11)      | NO   | PRI | NULL              | auto_increment              |
| name      | varchar(100) | NO   |     | NULL              |                             |
| value     | longtext     | NO   |     | NULL              |                             |
| create_at | datetime     | NO   |     | NULL              |                             |
| update_at | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+-----------+--------------+------+-----+-------------------+-----------------------------+
```

#### 参数介绍
> 使用key Value方式, 方便后续一些`key value`配置信息直接写入即可
- ID: 自增长
- name: 名称(key)
- value: 值(value)
- create_at: 记录事件创建时间
- update_at: 记录事件更新时间

#### API接口
- URL: http://172.16.0.101:9000/app_settings
- 工具： Postman
- 支持： Get/POST/PUT/DELETE

##### GET示例
- 返回所有配置信息
```python
import requests

api = 'http://172.16.0.101:9000/app_settings'

r = requests.get(api)

print(r.text)

```
-  返回格式：`dict`
```json
{
    "status": 0,
    "data": {
        "SITE_URL": "http://opendevops.cn",
        "EMAIL_SUBJECT_PREFIX": "OpenDevOps",
        "EMAIL_HOST": "smtp.exmail.qq.com",
        "EMAIL_PORT": "465",
        "EMAIL_HOST_USER": "user@domain.com",
        "EMAIL_HOST_PASSWORD": "password",
        "EMAIL_USE_SSL": "true",
        "EMAIL_USE_TLS": "false"
    },
    "msg": "查询成功"
}
```

##### POST/PUT/DELETE示例
> 使用POSTMAN测试工具只需要填写body里面信息即可
- POST：新增
- PUT： 更新
- DELETE： 删除

```python
{
    "name": "SITE_URL",
    "value": "http://opendevops.cn"
}
```

#### 部署文档
- 克隆代码
```shell
$ git@github.com:yanghongfei/AppSettings.git
$ yum install mysql -y
$ create database OpenDevOps character set utf8;
#数据表由ORM自动生成
```
- Python3环境
```bash
$ yum install xz wget -y
$ wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
$ xz -d  Python-3.6.3.tar.xz
$ tar xvf Python-3.6.3.tar
$ cd Python-3.6.3/
$ ./configure
$ make && make install

# 查看安装
$ python3 -V
```

- 安装依赖
```bash
$ pip3 install -r requirements.txt
```

- 手动启动
```bash
$ python3 app.py --port=9000
```

- 守护进程
```bash
$ cp supervisord.conf /etc/supervisord.conf
$ /usr/bin/supervisord  #后台运行使用/usr/bin/supervisord &

```