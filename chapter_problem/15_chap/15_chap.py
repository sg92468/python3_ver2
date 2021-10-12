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


