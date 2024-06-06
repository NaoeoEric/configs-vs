nota1 = 5
nota3 = 10
nota2 = 7

nota_media = nota1 + nota2 + nota3
nota_media = nota_media/3
falta = 21

if falta <= 20 and nota_media >= 7:
  print("Você passou!")
  
if falta > 20 and nota_media >= 7:
  print("Você reprovou por falta!")

if falta < 20 and nota_media < 7:
  print("Você reprovou por nota!")
  
print(f"""a primeira nota foi {nota1}
a segunda nota foi {nota2}
a terceira nota foi {nota3}
a nota média final foi {nota_media}
a quantidade de falta foi {falta} faltas""")
