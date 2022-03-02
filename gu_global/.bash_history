cd gu_global
pip install whitenoise
python manage.py runserver
pip install pillow
python manage.py runserver
ps ax|grep gunicorn
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
ps ax|grep gunicorn
kill -9 5363
kill -9 5366
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global
python manage.py runserver
ps ax|grep gunicorn
kill -9 6189
kill -9 6192
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 &
ps ax|grep gunicorn
kill -9 8006
kill -9 8009
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
python manage.py runserver
ps ax|grep gunicorn
kill -9 9415
kill -9 9418
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
pip install pymysql
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
ps ax|grep gunicorn
kill -9 11590
kill -9 11593
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
ps ax|grep gunicorn
kill -9 17592
kill -9 17595
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global/
python manage.py runserver
ps ax|grep gunicorn
kill -9 18491
kill -9 19099
ps ax|grep gunicorn
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global/
python manage.py runserver
ps ax|grep gunicorn
kill -9 21937
kill -9 21940
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
ps ax|grep gunicorn
kill -9 23739
kill -9 23742
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
ps ax|grep gunicorn
kill -9 24675
kill -9 24678
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
python manage.py runserver
cd gu_global/
python manage.py runserver
ps ax|grep gunicorn
kill -9 25359
kill -9 25398
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global/
python manage.py runvers
python manage.py runserver
ps ax|grep gunicorn
kill -9 25395
kill -9 29688
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global/
ps ax|grep gunicorn
kill -9 34819
kill -9 34822
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global/
python manage.py runserver
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
ps ax|grep gunicorn
kill -9 36761
kill -9 36764
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
cd gu_global/
ps ax|grep gunicorn
kill -9 41009
kill -9 41012
gunicorn gu_global.wsgi:application --bind 0.0.0.0:8080 --daemon
