#Crie um programa em Python que leia as notas do estudante nos 4 bimestres da
#nossa disciplina e a frequência (em porcentagem). A seguir informe se o estudante
#passou por média, rodou ou ficou em exame. Para passar por média, o estudante
#deve ter média maior ou igual a 7. Estudante com média abaixo de 3 roda sem ao
#menos fazer o exame. O estudante que tiver menos de 75% de frequência também
#está rodado na disciplina.

Frequência = float(input("Informe sua frequência: "))
nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))
nota3 = float(input("Informe sua terceira nota: "))
nota4 = float(input("Informe sua quarta nota: "))
média = (nota1 + nota2 + nota3 + nota4)/4

if média >=7:
    print ("Passou por média")
    if média < 3 or média < 7:
        print ("Pegou exame!")
else:
    print ("Rodou")
if Frequência < 75:
    print ("Rodou")
