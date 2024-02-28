"""
Formatar o CPF 
"""
#---------------------------- Criando variaveis ----------------------
CPF= str(input("Informe o seu cpf:")) 
multi_10 = 10
multi_11 = 11
soma_10 = 0
soma_11 = 0
#CPF = "14538220620"
digito_CPF = 0
#---------------------------- Criando variaveis ----------------------
#---------------------------- Formatação ------------------------------
formatado = CPF[0:3] + '.'+ CPF[3:6] + '.'+ CPF[6:9] + '-' + CPF[9:11]
print(CPF)
print(formatado)
print("------------------------------")
#----------------------------- Formatação -----------------------------
"""
Validar o CPF
"""
#--------------------------- Primeira Verificação ----------------------------------
while multi_10 >= 2:
    soma_10 = soma_10 + int(CPF[digito_CPF]) * (multi_10 - 2)
    digito_CPF = digito_CPF + 1
    multi_10 = multi_10 - 1
soma_10 = soma_10 % 11
if soma_10 >= 10:
    soma_10 = 11 - soma_10
print(soma_10)
print ("------------------------------")
#---------------------------- Primeira Verificação -----------------------------------
#---------------------------- Segunda verificação --------------------------
digito_CPF = 0
while multi_11 >= 2:
    soma_11 = soma_11 +int(CPF[digito_CPF]) * (multi_11)
    digito_CPF = digito_CPF + 1
    multi_11 = multi_11 - 1
soma_11 = soma_11 % 11
soma_11 = 11 - soma_11
#--------------------------- Segunda verificação ----------------------------
#--------------------------- Condição ----------------------------------------
if soma_11 >= 10:
    soma_11 = 0
print(soma_11)
print ("------------------------------")
#-------------------------- Condição --------------------------------------------
#-------------------------- Verificação Final -----------------------------------------
resultado = str(soma_11)
gabarito = CPF[10]
if gabarito == resultado:
    print ("Seu CPF é verdadeiro")
else:
    primt ("CPF é invalido")
#-------------------------- Verificação Final -----------------------------------------