# **Encontrar PI até a N-ésima casa decimal** - Insira um número e faça o programa gerar PI até essa quantidade de casas decimais. Mantenha um limite para até onde o programa irá.

from mpmath import mp

def encontrar_pi(numero_casas):
    mp.dps = numero_casas + 2;
    pi = str(mp.pi);

    return pi[numero_casas + 1];

numero_casas = 100
result_casas = encontrar_pi(numero_casas)
print(f"A {numero_casas + 1}-esima casa decimal de PI e: {result_casas}");
