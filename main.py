import subprocess

print("                                                                       Among Ass                                                                        ")

print('~Tasks~\n'
      '~Emergency button<exit> (press 0)\n'
      '~Security (press 1)\n'
      '~MedBay (press 2)\n'
      '\n'
      '\n'
      '\n')

answ = int(input("What we shoud do?"))

if answ == 0:
      subprocess.Popen('emergency.py 1', shell=True)
if answ == 1:
      subprocess.Popen('security_task.py 1', shell=True)
if answ == 2:
      subprocess.Popen('medbay.py 1', shell=True)
