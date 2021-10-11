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

