while True:
    for i in range(1):
        a=input("aya menu dar khast  ha baz beshe (y/n) ?")
    if a == "y":
        def menu():
            print('1 : masaht morab')
            print('2 : masaht mosalas')  
            chois=int(input("which one : 1 or 2 ?      "))  
            return chois
        break
        
    elif a == "n":
            print("etmam barname |<love you>|")
            break
        
chois=menu()  

if chois == 1:
     def msmoraba():
        ZEL=int(input('enter ZEL ?'))
        print('masaht morab :',ZEL * ZEL)
     msmoraba()
if chois == 2:
    def msmoslas():
        h=int(input('enter h ?'))
        b=int(input('enter b ?'))
        print('masaht mosalas :',h*b/2)
    msmoslas()
    

      

   






