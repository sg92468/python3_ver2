# 15.1 プログラムとプロセス
import os
print(os.getpid())
print(os.getcwd())
print(os.getuid())
print(os.getgid())

# 15.1.1 subprocessのプロセス作成
import subprocess
ret = subprocess.getoutput('date')
print(ret)
ret = subprocess.getoutput('date -u')
print(ret)
ret = subprocess.getoutput('date -u | wc')
print(ret)
ret = subprocess.check_output(['date', '-u'])
print(ret)
ret = subprocess.call('date')
print(ret)
ret = subprocess.call('date -u', shell=True)

# 15.1.2 multprocessingのプロセス作成
# mp.pyに記載

# 15.1.3 terminate()によるプロセスの強制終了
# mp2.pyに記載

# 15.1.4 osでのシステム情報の入手
import os
print(os.uname())
print(os.getloadavg())
print(os.cpu_count())

# 15.1.5 psutilによるプロセス情報の取得
# import psutil
# print(psutil.cpu_times(True))
# print(psutil.cpu_percent(True))
# print(psutil.cpu_percent(percpu=True))

# 15.3.2 プロセス
# dishes.pyに記載

# 15.3.3 スレッド
# thread1.pyに記載

# 15.3.4 concurrent.futures
# cf.pyに記載

# 15.3.5 グリーンスレッドとgevent
# gevent_test.pyに記載

# 15.3.6 twisted
# knock_server.py,knock_client.pyに記載 起動はしない

# 15.3.8 Redis
# redis_washer.py,redis_dryer.pyに記載 エラー発生

# q15
import multiprocessing
import random

from datetime import datetime
from time import sleep

def now(seconds):
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()




