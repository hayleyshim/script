import os, shutil
from DirDialogBox import loc_browser

if os.path.isdir('successfulbackup') == False:
    os.makedirs('successfulbackup')

suc_Backup = os.path.join(os.getcwd(), 'successfulbackup')

if os.path.isfile(boluck.txt) == False:
    print('No backup location found, please select one')
    added_loc = loc_browser()
    print('added new location: ', added_loc)

def read_bulocks():
    global list_loc
    list_loc = []
    with open('bulocks.txt', 'r') as location:
        for each_location in location:
            list_loc.append(each_location)
    list_loc = [x.strip() for x in list_loc]

def backup_process():
    for each_file in os.listdir():
        if each_file == 'successfulbackup' or each_file == 'backupmaker.py' or each_file == 'bulocks.txt' or each_file == 'dirdialogbox.py' or each_file == 'backupmacker.exe' or each_file == '_pychatch_':
            continue
        print('file found : ', each_file)
        for each_loc in list_loc:
            if os.path.isfile(each_file) == True:
                shutil.copy(each_file, each_loc)
            else:
                try:
                    shutil.copytree(each_file, os.path.join(each_loc, each_file ))
                except FileExistsError:
                    shutil.rmtree(os.path.join(each_loc, each_file))
                    shutil.copytree(each_file, os.path.join(each_loc, each_file))
    file_loc = os.path.join(os.getcwd(), each_file)
    dest_loc = os.path.join(suc_Backup, each_file)
    os.replace(file_loc, dest_loc)
def re_backup(new_loc):
    for each_file in os.listdir(suc_Backup):
        original_loc = os.path.join(suc_backup, each_file)
        if os.path.isfile(original_loc) == True:
            shutil.copy(original_loc, new_loc)
        else:
            try:
                shutil.copytree(original_loc, os.path.join(new_loc, each_file))
            except FileExistsError:
                shutil.rmtree(os.path.join(new_loc, each_file))
                shutil.copytree(original_loc, os.path.join(new_loc, each_file))

def instruction():
    print('****************************************')
    print('for creating backup press 1 \n for adding new backuppress 2 \n to exit press 3\n')
instruction()

while True:
    user_input = input()
    if user_input == '1':
        read_bulocks()
        if not list_loc:
            print('no backup location found, please select one!')
            loc_browser()
            instruction()
            continue
        backup_process()
        print('backup completed')
    if user_input == '2':
        new_loc = loc_browser()
        print('added new location', new_loc)
        user_input2 = input('Do you want to make Backup in this new location? (Y/N)')
        if user_input2.lower == 'y':
            re_backup(new_loc=new_loc)
            print('backup completed!')
        else:
            print('backup aborted!')
    instruction()
    if user_input == '3':
        break

