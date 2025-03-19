num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

operation = input(
    '''
    Por favor, digite a operação matemática que você gostaria de concluir:
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    '''

)

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao =  num1 * num2
divisao = num1 / num2


print('{} + {} = {}'.format(num1, num2, adicao))
