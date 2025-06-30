def 빈칸출력(name):
    f = open(f'파이썬\\{name}', mode='r', encoding='UTF-8')
    arr = f.readlines()
    arr2 = []
    for row in arr:
        row = row.replace("\n", "")
        arr2.append( row.split(",") )
    print('='*30)
    for row in arr2:
        행 = ""
        for v in row:
            행 += 'O' if v == 'O' else ' '
        print(행)
        
빈칸출력('픽셀팀.csv')
빈칸출력('고담팀.csv')
빈칸출력('문제.csv')