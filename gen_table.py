import os

dir_list = os.listdir('./')
dir_list.remove('.idea')
dir_list.remove('gen_table.py')
dir_list.remove('readme.md')

print('name|type')
print('---|---')
for i in dir_list:
    for j in os.listdir(i):
        print('['+j[:-3]+']'+'('+ i+'/'+j.replace(' ','%20') +')' '  |  '+i)