dia=25
mes=6
ano=2020

if dia>=1 and dia<=31:
  if mes> 0 and mes < 13:
    if ano>2019:
      print("Estamos no dia %d / %d / %d" %(dia,mes,ano))
    else:
      print("Esse ano já passou...")
