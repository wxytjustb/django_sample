


初始化开发环境

```
# 安装virtualenv 
pip3 install virtualenv
# 创建虚拟环境
virtualenv venv
# 安装依赖
pip install -r requiriments.txt

# 启动相关组件依赖（redis）
docker-compose up -d

```

初始化数据库
```shell script

# 生成migrations脚本
python manage.py makemigrations

# 生成数据库
python manage.py migrate

```


cd django_admin
python manage.py runserver 0.0.0.0:8090


# 生成数据库
python manage.py migrate


# 创建一个管理员
python manage.py createsuperuser

# 生成数据库脚本
python manage.py makemigrations
python manage.py migrate



celery相关

```
# broker默认使用redis


# 运行调度器
celery -A django_sample beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# 运行worker，运行worker之前需要将redis服务启动
celery -A django_sample worker -l INFO

```