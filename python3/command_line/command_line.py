import subprocess


user = raw_input("host\n > ")
x = subprocess.check_output(['ping', user])
print(x)
