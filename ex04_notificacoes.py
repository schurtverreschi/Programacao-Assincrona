import asyncio

usuarios = [
    {"nome": "Carla", "vip": False, "notificações_ativadas": False},
    {"nome": "João", "vip": False, "notificações_ativadas": True},
    {"nome": "Ana", "vip": True, "notificações_ativadas": True},
    {"nome": "Bruno", "vip": True, "notificações_ativadas": False},
]


async def enviar_notificações(usuario):
    if usuario["vip"] and usuario["notificações_ativadas"]:
        print("Notificação VIP para ", usuario["nome"], " enviada!")
    elif usuario["notificações_ativadas"]:
        await asyncio.sleep(0.1)
        print("Notificação normal para ", usuario["nome"], " enviada!")
    else:
        await asyncio.sleep(0.2)
        print(usuario["nome"], " desativou as notificações. Nada foi enviado.")


async def main(lista):
    tarefas = [enviar_notificações(u) for u in lista]

    print("\nEnviando notificações...\n")
    await asyncio.gather(*tarefas)
    print("\nTodas as notificações foram processadas!\n")


asyncio.run(main(usuarios))


# Sistema de notificação inteligente

# Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. No entanto, algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema. Além disso, se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.

# Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status diferente:

# Ana: VIP (deve receber uma notificação prioritária antes das normais).
# João: Usuário comum, mas ativou as notificações.
# Carla: Usuária comum, mas desativou as notificações (não deve receber nada).

# O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.

# Saída esperada:

# Enviando notificações...
# Notificação VIP para Ana enviada!
# Notificação normal para João enviada!
# Carla desativou as notificações. Nada foi enviado.
# Todas as notificações foram processadas!
