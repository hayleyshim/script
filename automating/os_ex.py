import os
dir_name = 'my_folder'
print('my_folder is created!', dir_name)
os.makedirs(dir_name)
file_name = os.path.join(dir_name, 'sample_example.txt')
print('creating', file_name)
with open(file_name, 'wt') as f:
    f.write('sample example file')
print('cleaning up ')
os.unlink(file_name)
os.rmdir(dir_name)