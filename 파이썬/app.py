print('안녕하세요')

file=open('파이썬\\text.txt',encoding='UTF-8',mode='w')
file.write('여보세요\n')
file.close()

file=open('파이썬\\text.txt',encoding='UTF-8',mode='r')
print(file.readlines())
file.close()

file=open('파이썬\\text.txt',encoding='UTF-8',mode='a')
file.write('이게 뭡니까\n')
file.close()

file=open('파이썬\\text.txt',encoding='UTF-8',mode='r')
print(file.readlines())
file.close()