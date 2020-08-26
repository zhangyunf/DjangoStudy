# 目录详解
```textmate
untitled
    -untitled  对整个程序进行配置
        -init 
        -settings 配置文件
        -url      url对应关系
        -wsgi     遵循WSGI规范，uwsgi+nginx 
    -manage.py    管理Django程序
```

# 常用命令
```text
1. 运行Django功能
python manage.py runserver 127.0.0.1:8001
2. 创建APP
python manage.py startapp cmdb
```
# APP目录
```text
app:
    migrations 数据库修改表结构操作记录
    admin      Django提供的后台管理
    apps       配置当前app
    models     ORM,写指定的类 通过命令可以创建数据库结构
    tests      单元测试
    views      业务代码
```