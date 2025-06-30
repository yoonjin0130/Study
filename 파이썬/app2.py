f = open('파이썬\\data3.csv',mode='r',encoding='UTF-8')
arr = f.readlines()

arr2=[]
for row in arr:
    row=row.replace("\n","")
    #row=row.replace(",","X")
    arr2.append(row.split(","))

for row in arr2:
    행 = ""
    for v in row:
        행 += 'O' if v=='O' else ' '
    print(행)
        
    