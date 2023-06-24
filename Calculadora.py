import math
#Criação da class calculadora
class calculadora:
  def __init_subclass__(self):
    self.num1 = 0
    self.num2 = 0
    self.resultado = 0

  #Função da adição
  def somar(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 + self.num2
    return self.resultado

  #Função da subtração
  def subtrair(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 - self.num2
    return self.resultado

  #Função da multiplicação
  def multiplicar(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 * self.num2
    return self.resultado

  #Função da divisão
  def dividir(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 / self.num2
    return self.resultado

  #Função da exponenciação
  def exponenciar(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 ** self.num2
    return self.resultado

  #Função do resto
  def resto(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 % self.num2
    return self.resultado

  #Função da raiz quadrada
  def raiz(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.resultado = math.sqrt(self.num1 + self.num2)
    return self.resultado

def continuar(entrada):
  if entrada:
    return True
  else:
    return False

#Criação do MENU da calculadora
def menu():
  opc = {1: 'Adição',
         2: 'Subtração',
         3: 'Multiplicação',
         4: 'Divisão',
         5: 'Exponenciação',
         6: 'Resto',
         7: 'Raiz'}
  calc = calculadora()
  print('-----------MENU------------')
  print('|--Num---|----Operação----|')
  print('|   1    |     Adição     |')
  print('|   2    |    Subtração   |')
  print('|   3    |  Multiplicação |')
  print('|   4    |     Divisão    |')
  print('|   5    |  Exponenciação |')
  print('|   6    |      Resto     |')
  print('|   7    |      Raiz      |')
  print('---------------------------')
  #Escolha da operação matemática
  print("Digite um número para realizar uma operação matemática e aperte ENTER;")
  calcular = True
  while calcular:
      opcao = input("\nEscolha a opção de cálculo (1, 2, 3, 4, 5, 6 ou 7):")
      if not(opcao in '1 2 3 4 5 6 7'):
        print("Opção inválida!")
        continue
      else:
        opcao = int(opcao)
        print(f"Operação matemática escolhida é {opc[opcao]}.")

      #Operação da adição
      if opcao == 1:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.somar(num1, num2)
        print(f"O valor da adição é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))

      #Operação da subtração
      elif opcao == 2:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.subtrair(num1, num2)
        print(f"O valor da subtração é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))

      #Operação da multiplicação
      elif opcao == 3:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.multiplicar(num1, num2)
        print(f"O valor da multiplicação é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))

      #Operação da divisão
      elif opcao == 4:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.dividir(num1, num2)
        print(f"O valor da divisão é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))

      #Operação da exponenciação
      elif opcao == 5:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.exponenciar(num1, num2)
        print(f"O valor da exponenciação é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))

      #Operação do resto
      elif opcao == 6:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.resto(num1, num2)
        print(f"O valor do resto é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))

      #Operação da raiz quadrada
      elif opcao == 7:
        num1 = int(input("Digite o penúltimo número do seu RU:"))
        num2 = int(input("Digite o último número do seu RU:"))
        resultado = calc.raiz(num1, num2)
        print(f"O valor da raiz quadrada da soma dos dois números é {resultado}.")
        calcular = continuar(input("Digite algo para continuar ou aperte ENTER para sair da calculadora: "))
        print("!!!Calculadora finalizada!!!")
