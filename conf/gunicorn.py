import multiprocessing


bind = '127.0.0.1:8000'
backlog = 512 
workers = multiprocessing.cpu_count() * 2
threads = 2
worker_class = 'sync'
timeout = 30
keepalive = 2
pidfile = '/home/matt/git/work/graduationproject/var/gunocorn.pid'
loglevel = 'info'
accesslog = "/home/matt/git/work/graduationproject/var/gunocorn_access.log"
errorlog = "/home/matt/git/work/graduationproject/var/gunocorn_error.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
