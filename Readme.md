
cd django_admin
python manage.py runserver 0.0.0.0:8090


# 生成数据库
python manage.py migrate


# 创建一个管理员
python manage.py createsuperuser

# 生成数据库脚本
python manage.py makemigrations
python manage.py migrate