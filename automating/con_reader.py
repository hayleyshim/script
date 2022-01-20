from configparser import ConfigParser

p = ConfigParser()
#p.read('conf.ini')
#print(p.get('bug_tracker', 'url'))

files = ['hello.ini', 'python.ini', 'conf.ini']
files_found = p.read(files)
files_missing = set(files) - set(files_found)
print('file found: ',files_found)
print('file missing: ',files_missing)