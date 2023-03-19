
import os

# ./nginx -c /usr/local/nginx/conf/nginx.conf 启动nginx
# ./nginx -s stop 停止
# ./nginx -s reload

bind = '0.0.0.0:8080'
workers = os.cpu_count() * 2 - 1
cur_dir = os.path.dirname(__file__)
loglevel = 'warning'
errorlog = os.path.join(cur_dir, 'error.log')
accesslog = os.path.join(cur_dir, 'access.log')
daemon = True



