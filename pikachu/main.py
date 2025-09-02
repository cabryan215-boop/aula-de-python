import random 
def main():
    notas=[0] * 4
    i = 0
    while i < 4 :
        notas[i]=random.randint(1,10)
        i += 1
    media = notas[0]+notas[1]+notas[2]+notas[3]
    media /= 4
    print("as notas sao:\n""\n",notas[0],"\n",notas[1],"\n",notas[2],"\n",notas[3],"\na media da nota é",media)
    if media >=6:
        print("voce foi aprovado!")
    elif media>=4:
        print("voce esta de recuperaçao")
    else:
        print("reprovado")        








    return 0
main()