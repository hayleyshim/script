import subprocess

"""subprocess.call(['touch', 'document.txt'])
subprocess.call(['ls', '-l'])
print('document is created!')
subprocess.call(['rm', 'document.txt'])
subprocess.call('ls')
print('document is deleted!')"""

res = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE,)
print('return code: ', res.returncode)
print('{} type in stdout:\n{}'.format(len(res.stdout), res.stdout.decode('utf-8')))