import random
def main():
    numA =random.randint(1,12)
    print("agora vc tem:",numA,)
    come=input("Quer arriscar e pedir mais? ")
    i = random.randint(1, 21)
    
    while numA < 21:
        numA += random.randint(1,12)
        print("agora vc tem:",numA,)
        
        if numA > 21:
           break
        come=input("Quer arriscar e pedir mais? ")

        if come != "s":
           break

    print("O seu oponente tem ", i) 
    if numA > 21:
      print("vc perdeu por passar de 21")
    elif numA < i:
      print("Vc perdeu pro oponente")
        
    else:
       print("vc ganhou")
      
   




    return 0
main()
