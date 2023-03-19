
import multiprocessing

# ./nginx -c /usr/local/nginx/conf/nginx.conf 启动nginx
# ./nginx -s stop 停止
# ./nginx -s reload

bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '/var/log/pythonbbs/access.log'
daemon = True
