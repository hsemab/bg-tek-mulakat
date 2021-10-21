#ikinci dereceden denklem: ax2+bx+c
while True:
    print("İkinci dereceden denklem: ax2+bx+c")

    try: # a ve b 0 girilmesin??
        a = int(input("a :"))
        b = int(input("b :"))
        c = int(input("c :"))
    
        delta=pow(b,2)-4*a*c #kökleri bulmak için gereken delta sayısı
        #print(delta)
        root1=(-b+delta**0.5)/(2*a) 
        root2=(-b-delta**0.5)/(2*a)

        print("Denklemin 1. kökü:", "{:g}".format(root1)) #uzun ondalık kısmın kısaltılması
        print("Denklemin 2. kökü:", "{:g}".format(root2))
        break

    except ZeroDivisionError:
        print("a=0 olamaz!")
        continue
    except ValueError:
        print("Lütfen sadece sayı girin!")
        continue