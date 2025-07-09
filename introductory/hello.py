
import os

    # file_path=f'./channel/{file}'
    # content = open().read()

    # print(content)
    
# nothing = 90052
# # os.listdir('./channel')
# file = f'./channel/{nothing}.txt'
# while file :
# print()

import zipfile
archive = zipfile.ZipFile('channel.zip', 'r')
comments = []

nothing=90052
lol=[]
while nothing:
    file =open(f'./channel/{nothing}.txt')
    content=file.read()
    # lol.append(content)
    comments.append(str(archive.getinfo(f'{nothing}.txt').comment))
    try:
        nothing=int(content.split()[-1])
    except:
        break
# print(lol[-1])
# print(nothing)
# print(comments)
print(''.join(map(str,comments)))