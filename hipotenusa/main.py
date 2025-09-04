import math

def main():
   cateto= int (input("qual o cateto? "))
   catetoA= int (input("qual o cateto adjecente? "))
   hipotenusa= (cateto * cateto)  + (catetoA *catetoA)
   hipotenusa = math.sqrt(hipotenusa)
   print("pitagoras disse que a resposta é",hipotenusa)





   return 0
main()