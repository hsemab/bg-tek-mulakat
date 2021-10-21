class Main:

  def tetrahedralFormula(self,num):
    #Wikipedia'daki dörtyüzlüsel sayıyı bulma formülüne göre 
    result = int(num*(num+1)*(num+2)/6)
    print("Formül ile", num, "sayısının dörtyüzlüseli:", result)

  def tetrahedral(self,num):
    #"n. dörtyüzlüsel sayı ilk n üçgensel sayının toplamına eşittir" ifadesine göre
    triangulars=[]
    result=0
    sumNums=0

    for x in range (1,(num+1)):
        sumNums=sumNums+x #üçgensel oluşturmak için toplamlar
        triangulars.append(sumNums) #üçgensel sayılar diziye eklenir.
    #print(triangulars)

    for i in range(0,len(triangulars)):
        result+=triangulars[i] #üçgensel sayıların toplamı

    print("ilk", num, "üçgensel sayının toplamına göre", num, "sayısının dörtyüzlüseli:", result)

if __name__ == "__main__":
  run = Main()
  while True:      
      try:
        num = int(input("Dörtyüzlüsel bulmak için sayı giriniz:"))
        if num>0:
          run.tetrahedralFormula(num)
          run.tetrahedral(num)  
          break       
      except ValueError:
          continue