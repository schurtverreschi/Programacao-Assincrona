import asyncio
import random

tamanhos = [(random.randrange(10, 51)) for _ in range(5)]
nomes = [
    "arquivo_1.txt",
    "arquivo_2.txt",
    "arquivo_3.txt",
    "arquivo_4.txt",
    "arquivo_5.txt",
]

VELOCIDADE_DOWNLOAD = 5


async def download(nome, tamanho):
    progresso = 0
    segundos = 0
    print(f"Iniciando download de {nome} (tamanho: {tamanho}MB)...")

    while progresso < tamanho:
        await asyncio.sleep(1)
        segundos += 1
        progresso += VELOCIDADE_DOWNLOAD
        progresso = min(progresso, tamanho)
        print(f"[{segundos}s] {nome}: {progresso}MB baixados")

    print(f"Download de {nome} concluído!")


async def main():
    tarefas = [download(nomes[int(i)], tamanhos[int(i)]) for i in range(5)]
    await asyncio.gather(*tarefas)
    print("\nTodos os downloads foram finalizados!\n")


asyncio.run(main())

# Monitoramento de download

# Imagine que você está desenvolvendo um gerenciador de downloads que permite baixar múltiplos arquivos simultaneamente. Como nem todos os arquivos têm o mesmo tamanho, alguns downloads demoram mais que outros. Seu programa deve:

# Baixar cinco arquivos diferentes, cada um com um tamanho aleatório entre 10MB e 50MB;
# A velocidade de download de cada arquivo é de 5MB por segundo;
# Exibir mensagens de progresso a cada segundo, mostrando quanto já foi baixado de cada arquivo;
# Exibir uma mensagem quando cada download for concluído;
# Aguarde todos os downloads antes de encerrar o programa.

# Saída esperada:

# Iniciando download de arquivo_1.txt (tamanho: 30MB)...
# Iniciando download de arquivo_2.txt (tamanho: 45MB)...
# Iniciando download de arquivo_3.txt (tamanho: 20MB)...
# Iniciando download de arquivo_4.txt (tamanho: 10MB)...
# Iniciando download de arquivo_5.txt (tamanho: 50MB)...

# [1s] arquivo_1.txt: 5MB baixados
# [1s] arquivo_2.txt: 5MB baixados
# [1s] arquivo_3.txt: 5MB baixados
# [1s] arquivo_4.txt: 5MB baixados
# [1s] arquivo_5.txt: 5MB baixados

# [2s] arquivo_1.txt: 10MB baixados
# [2s] arquivo_2.txt: 10MB baixados
# [2s] arquivo_3.txt: 10MB baixados
# [2s] arquivo_4.txt: 10MB baixados
# arquivo_4.txt concluído!

# [3s] arquivo_1.txt: 15MB baixados
# [3s] arquivo_2.txt: 15MB baixados
# [3s] arquivo_3.txt: 15MB baixados

# [4s] arquivo_1.txt: 20MB baixados
# [4s] arquivo_2.txt: 20MB baixados
# arquivo_3.txt concluído!

# ...

# arquivo_1.txt concluído!
# arquivo_2.txt concluído!
# arquivo_5.txt concluído!

# Todos os downloads foram finalizados!
