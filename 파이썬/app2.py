f = open('파이썬\\data2.csv',mode='r',encoding='UTF-8')
arr = f.readlines()

for row in arr:
    row=row.replace("/n","")
    row=row.replace(",","")
    print(row)
    