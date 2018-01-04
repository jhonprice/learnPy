import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)


print('$ nslookup')

p = subprocess.Popen(['nslookup'])
p.communicate("127.0.0.1")

print(p.returncode)

