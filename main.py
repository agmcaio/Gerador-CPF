from random import randint

numero = str(randint(100000000, 999999999))
cpf = numero

soma_total = 0 
reverter = 10 

for i in range(19):
    if i > 8: 
        i -= 9

    soma_total += int(cpf[i]) * reverter 

    reverter -= 1
    if reverter < 2:
        reverter = 11
        digito = 11 - (soma_total % 11)

        if digito > 9:
            digito = 0

        soma_total = 0
        cpf += str(digito)

print(f'Aqui está um CPF válido: {cpf}')