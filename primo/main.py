def main():
    num = int (input("digite um numero:"))
    i=2
    while num!= i and num>1:
        if num % i == 0:
          break
        i += 1
    if num == i:
       print("o numero ",num,"é primo")
    else:
       print("o numero ",num,"nao é primo")       



    return 0
main()