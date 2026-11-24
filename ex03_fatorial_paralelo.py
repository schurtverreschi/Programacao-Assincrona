import asyncio


async def fatorial(n):
    await asyncio.sleep(n)

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    print(f"Fatorial de {n} = {resultado}")


async def main(lista_numeros):
    tarefas = [fatorial(int(i)) for i in lista_numeros]
    await asyncio.gather(*tarefas)


asyncio.run(main([5, 3, 7, 4, 6]))


# Executando fatorial em paralelo

# Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.

# Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, em ordem de menor número para maior número.

# Dica: use a função sleep para simular um tempo de processamento.

# Dica: para testar o funcionamento do seu código, utilize uma lista de números em ordem de tamanho aleatória. Exemplo: números = [5, 3, 7, 4, 6]

# Saída esperada:

# Fatorial de 3 = 6
# Fatorial de 4 = 24
# Fatorial de 5 = 120
# Fatorial de 6 = 720
# Fatorial de 7 = 5040
