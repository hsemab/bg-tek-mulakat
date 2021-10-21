def magic_square(matrix):
    L = len(matrix[0]) #satırdaki eleman sayısı
    L1= len(matrix) # sütundaki eleman sayısı
    sumList=[] #satır ve sütunların toplamlarının içine atılacağı liste, toplamların karşılaştırılması için kullanılacaktır.

    if L==L1: # kare mi kontrolü      

        #Satır
        for i in range(L): 
            sumCol=0
            for j in range(L):
                sumCol+=matrix[i][j] #satırdaki elemanların toplamı
            sumList.append(sumCol) #değer listeye eklenir

        #Sütun
        for i in range(L):
            sumRow=0
            for j in range(L):
                sumRow+=matrix[j][i] #sütundaki elemanların toplamı
            sumList.append(sumRow)  #değer listeye eklenir
    else:
        sumList=[]
    return sumList 

def magic_square_test(m):
    listSum=magic_square(m) #fonksiyondan gelen sumList bu atamayla listSum olur.
    L = len(listSum)

    if L!=0:
        firstItem=listSum[0]
        flag=0 # eşitliğinin kontrolü için flag değeri

        #Karşılaştırma
        for i in range(0,L):
            if  firstItem!=listSum[i]: #toplam değerleri karşılaştırılır
                flag+=1
        if flag!=0: #eşitliğin bozulması durumu
            return False
        else:
            return True
    else:
        return "Matrix kare değildir."

#[7, 12, 1, 14],
#[2, 13, 8, 11],
#[16, 3, 10, 5], 
#[9, 6, 15, 4]

m=[[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]] 
print(magic_square_test(m))

m=[[2, 7, 6], [9, 5, 1], [4, 3, 8], [4, 3, 8]]
print(magic_square_test(m))

m=[[2, 7, 6], [9, 5, 1], [4, 3, 7]]
print(magic_square_test(m))