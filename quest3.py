class Numbers:
    def __init__(self,n):
        if not isinstance(n, int):
            raise TypeError('Invalid Init')
        self.number = n

    def isPalindrome(self):
        num=str(self.number)
        revNum=num[::-1]
        if num==revNum:
            #print("Sayı Palindromdur.") 
            return True
        else:
            #print("Sayı Palindrom değildir.")
            return False

if __name__ == "__main__":

    num=int(input("Bulunacak palindrom 'sayı'yı giriniz:"))
    print(Numbers(num).isPalindrome())    # False