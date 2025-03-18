n = input('Digite algo: ')
st = input('Digite algo: ')
nst = input('Digite algo: ')
up = input('Digite algo: ')

print(n.isnumeric()) #serve para indicar se o que o usuario escreveu no terminal é ou não numerico/numero
print(st.isalpha()) #serve para indicar se o que o usuario escreveu no terminal é ou não letra/str
print(nst.isalnum()) #serve para indicar se o que o usuario escreveu no terminal é ou não letra ou numerico(tambem serve para os dois juntos)
print(up.isupper()) ##serve para indicar se existe alguma letra maiuscula