def calculate():
    operation = input( '''
Por favor, digite a operação matemática que você gostaria de concluir:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))


    adicao = num1 + num2
    subtracao = num1 - num2
    multiplicacao =  num1 * num2
    divisao = num1 / num2

    if operation == '+':
        print('{} + {} = {}'.format(num1, num2, adicao))

    elif operation == '-':
        print('{} + {} = {}'.format(num1, num2, subtracao))

    elif operation == '*':
        print('{} + {} = {}'.format(num1, num2, multiplicacao))

    elif operation == '/':
        print('{} + {} = {}'.format(num1, num2, divisao))

    else:
        print('Por favor, escolha uma operação valida ' 
              'Execute o programa novamente')

    #adicionando a função again()
    again()

def again():
    calc_again = input( '''
Quer calcular novamente? Por favor, digite Y para SIM e N para NÃO
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais..bye')
    else:
        again()

def welcome():
    print('''
Bem vindo a minha calculadora
    ''')
welcome()
calculate()