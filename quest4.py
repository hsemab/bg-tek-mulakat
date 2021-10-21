def magic_square_test(matrix):
    columnNum = len(matrix[0]) #satırdaki eleman sayısı
    rowNum= len(matrix) # sütundaki eleman sayısı
    sumList=[] #satır ve sütunların toplamlarının içine atılacağı liste, toplamların karşılaştırılması için kullanılacaktır.

    if columnNum==rowNum: # kare mi kontrolü      

        #Satır
        for i in range(columnNum): 
            sumCol=0
            for j in range(columnNum):
                sumCol+=matrix[i][j] #satırdaki elemanların toplamı
            sumList.append(sumCol) #değer listeye eklenir

        #Sütun
        for i in range(columnNum):
            sumRow=0
            for j in range(columnNum):
                sumRow+=matrix[j][i] #sütundaki elemanların toplamı
            sumList.append(sumRow)  #değer listeye eklenir
    else:
        sumList=[]

    sumNum = len(sumList)

    if sumNum!=0: #liste boş değilse
        firstItem=sumList[0]
        isEqual=0 # eşitliğinin kontrolü için flag değeri

        #Karşılaştırma
        for i in range(0,sumNum):
            if  firstItem!=sumList[i]: #toplam değerleri karşılaştırılır
                isEqual+=1
        if isEqual!=0: #eşitliğin bozulması durumu
            return False
        else:
            return True
    else:
        return "Matrix kare değildir."

# [7, 12, 1, 14],
# [2, 13, 8, 11],
# [16, 3, 10, 5], 
# [9, 6, 15, 4]

m=[[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]] 
print(magic_square_test(m))

m=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(magic_square_test(m))

m=[[2, 7, 6], [9, 5, 1], [4, 3, 7]]
print(magic_square_test(m))