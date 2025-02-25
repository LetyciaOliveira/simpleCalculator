print("Hello World")

a = 1;
b = 2

soma = a + b

substracao = a - b

print (substracao)


if a >= b : 
 print ("A é maior ou igual a B")
else  :
 print("não é")

#recebe informação

#: tipar (anotações)
#str variavel do tipo texto
 nome: str = input("Qual é seu nome?")

 #f processa o texto
 texto: str = f"Olá, {nome}"
#devolve
print(texto)

if nome == "Letycia":
 print ("Olá adm")
elif nome == "Elias" :
 print("Olá aluno")
else: 
 print ("oi qualquer")


 match nome:
  case "Letycia":
   print ("Ola adm 2")
  case "Antonio":
   print ("Olá zé ninguém")
##conhecer todos os tipos de variaveis em python

#numero

numero = int(input("Digite um numero:"))

if numero > 0:
 print ("numero maior")
 if numero == 20:
  print ("O numero é 20")
else :
 print ("maior")