import os
path = 'C:\\Users\\user\\Desktop'


def check_files_content(path, level = 1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Go into', path + '\\' + i)
            check_files_content(path + '\\' + i, level + 1)
            print('Go out!', path)


check_files_content(path)
