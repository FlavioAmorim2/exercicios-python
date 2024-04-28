# No python você coloca cometarios usando "#"


# VARIAVÉIS

# Declarar uma variavel só basta colocar o nome junto com o valor

nome = "Liam"  # String
idade = 24  # Integer
fera = True  # Boolean
porcentagem_fera = 99.9  # Float

# Tipos de dados unicos no python

lista = ["SP", "RJ", "MG"]  # No python os Arrays são chamados de listas

dicionario = {
    "estados": lista,
    "populacao": [100000, 200000, 300000],
}  # Pode se entender como um json ou objeto do js

tupla = (
    "SP",
    "RJ",
    "MG",
)  # Parecido com as listas mas tem propiedades diferentes, por encuanto não precisa se focar nisso.

# Condicoes

if condicação:
    # faça alguma coisa
    pass

if not condição:  # O not no python funciona como ! no json
    # faça alguma coisa
    pass

elif condicao:
    # Elif é o else if do python
    pass
else:
    # faça alguma coisa
    pass

# Loops

while condicao:
    # Faça alguma coisa
    pass

# No python não existe o for (let i = 0; i < x; i++){} mas existe o foreach que tem no js e funciona bem similar.

paises = ["Brasil", "Argentina", "Chile"]

for pais in paises:
    # Faça alguma coisa
    pass

# No python não existe switch.


# Funcoes


def retorna_maior(numeros):  # Declara funcoes com def
    maior = numeros[0]
    for numero in numeros:
        if numeros[numero] > maior:
            maior = numeros[numero]

    return maior


# Builtins, funcoes já prontas no python

max()
min()
sorted()
len()
type()
