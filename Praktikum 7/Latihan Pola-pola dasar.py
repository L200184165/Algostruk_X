## halaman 65

import re

s = 'sebuah contoh kata:teh !!'
cocok = re.findall(r'kata:\w\w\w',s)

##latihan:
if cocok :
    print('menemukan', cocok)  
else :
    print('tidak menemukan')


# latihan 7.1 
a = 'sebuah contoh kata:batagor !!'
cocok = re.findall(r'kata:\w\w\w',a)


if cocok :
    print('menemukan', cocok) 
else :
    print('tidak menemukan')

b = 'sebuah contoh kata:es teh !!'
cocok = re.findall(r'kata:\w\w\w',b)


if cocok :
    print('menemukan', cocok) 
else :
    print('tidak menemukan')
