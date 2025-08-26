def main():
  idade=int(input("qual a sua idade?"))

  if idade >= 18:
    print("entrada liberada")
  elif idade >= 16:
    acom=input("vc estaria com acompanhante?")
    if acom=="s" or acom == "S":
      print("entrada liberada!")
    else:
      print("entrada proibida!")
  else:
    print("entrada negada")




  return 0
main()    