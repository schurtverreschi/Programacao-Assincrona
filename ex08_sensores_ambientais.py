import asyncio
import random
import time


async def sensor_temperatua():
    while True:
        temperatura_atual = random.randrange(-11, 41)
        await asyncio.sleep(2)
        tempo = time.perf_counter() - INICIO
        tempo_str = f"[{tempo:.0f}s]"
        print(f"{tempo_str:<5} {'Temperatura:':<16} {temperatura_atual}°C")


async def sensor_umidade():
    while True:
        umidade_atual = random.randrange(0, 101)
        await asyncio.sleep(3)
        tempo = time.perf_counter() - INICIO
        tempo_str = f"[{tempo:.0f}s]"
        print(f"{tempo_str:<5} {'Umidade:':<16} {umidade_atual}%")


async def sensor_qualidade_ar():
    while True:
        qualidade_ar_atual = random.choice(
            ["Péssima", "Ruim", "Regular", "Boa", "Excelente"]
        )
        await asyncio.sleep(5)
        tempo = time.perf_counter() - INICIO
        tempo_str = f"[{tempo:.0f}s]"
        print(f"{tempo_str:<5} {'Qualidade do ar:':<16} {qualidade_ar_atual}")


async def main():
    global INICIO
    INICIO = time.perf_counter()
    tarefas = [sensor_qualidade_ar(), sensor_umidade(), sensor_temperatua()]
    await asyncio.gather(*tarefas)


asyncio.run(main())


# Simulação de sensores ambientais

# Lucas está desenvolvendo um sistema de monitoramento ambiental. Para isso, ele precisa criar sensores assíncronos que coletam dados periodicamente, sem que o programa fique travado esperando por cada um.

# O sistema deve ter três sensores, que coletam e exibem dados em intervalos diferentes:

# Sensor de temperatura: Atualiza os dados a cada 2 segundos.
# Sensor de umidade: Atualiza os dados a cada 3 segundos.
# Sensor de qualidade do ar: Atualiza os dados a cada 5 segundos.

# O sistema nunca deve parar de rodar, exibindo os valores atualizados de cada sensor assim que novos dados estiverem disponíveis.

# Dica: Utilize uma corrotinas para resolver este problema e use o método random.choice para definir a temperatura e qualidade do ar.

# Saída esperada:

# [2s] Temperatura: 22°C
# [3s] Umidade: 60%
# [4s] Temperatura: 23°C
# [5s] Qualidade do ar: Boa
# [6s] Umidade: 58%
# [8s] Temperatura: 21°C
# [10s] Qualidade do ar: Regular
# ...
