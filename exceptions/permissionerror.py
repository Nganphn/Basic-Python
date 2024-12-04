import os

# entries = os.listdir('C:\\')
# files = [entry for entry in entries if os.path.isfile(os.path.join('C:\\', entry))]

# for file in files:
#     print(file)



# PermissionError: [Errno 13] Permission denied
# PermissionError when trying to read the files

with os.scandir('C:\\') as entries:
    for entry in entries:
        if entry.is_file():
            # print(entry.name)
            try:
                with open(entry.path, 'r') as file:
                    content = file.read()
                    print(content)
            except PermissionError:
                print('Read permission denied:', entry.path)

# PermissionError: [Errno 13] Permission denied
# PermissionError when trying to create the file

try:
    with open('C:\\ayho.txt', 'w'):
        pass
except PermissionError:
    print('Write permission denied')

# Use 'sudo' to gain elevated privileges to crete/add file in the root directory