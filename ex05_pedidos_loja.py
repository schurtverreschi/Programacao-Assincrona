import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponível": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponível": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponível": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponível": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponível": False},
]


async def verificar_pagamento(pedido):
    await asyncio.sleep(2)
    if pedido["pagamento_aprovado"]:
        print(f"Pagamento aprovado para pedido #{pedido['id']}.")
        return True
    else:
        print(
            f"Pagamento recusado para pedido #{pedido['id']}.{'':<7}\033[31mPedido cancelado.\033[0m"
        )
        return False


async def verificar_estoque(pedido):
    await asyncio.sleep(1)
    if pedido["estoque_disponível"]:
        print(f"Estoque disponível para pedido #{pedido['id']}.")
        return True
    else:
        print(
            f"Estoque indisponível para pedido #{pedido['id']}.{'':<5}\033[31mPedido cancelado.\033[0m"
        )
        return False


async def processar_pedido(pedido):
    print(f"Processando pedido #{pedido['id']}...")

    pagamento_ok = await verificar_pagamento(pedido)
    if not pagamento_ok:
        return
    estoque_ok = await verificar_estoque(pedido)
    if not estoque_ok:
        return
    print(
        f"Pedido #{pedido['id']} confirmado!{'':<20}\033[32mEnviado para entrega.\033[0m"
    )


async def main():
    tarefas = [processar_pedido(id) for id in pedidos]

    await asyncio.gather(*tarefas)

    print("\nTodos os pedidos foram processados!\n")


asyncio.run(main())


# Pedido #101 confirmado! Enviado para entrega.


# Processando pedidos de uma loja

# Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. O sistema deve seguir a seguinte lógica:

#     Primeiro, verificar se o pagamento foi aprovado;
#     Se o pagamento for aprovado, verificar se há estoque disponível;
#     Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
#     Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.

# A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. Confira o código:

# pedidos = [
#     {"id": 101, "pagamento_aprovado": True, "estoque_disponível": True},
#     {"id": 102, "pagamento_aprovado": True, "estoque_disponível": False},
#     {"id": 103, "pagamento_aprovado": False, "estoque_disponível": True},
#     {"id": 104, "pagamento_aprovado": True, "estoque_disponível": True},
#     {"id": 105, "pagamento_aprovado": False, "estoque_disponível": False},
# ]

# O programa deve simular essa lógica para três pedidos, exibindo mensagens conforme o processamento ocorre.

# Saída esperada:

# Processando pedido #101...
# Pagamento aprovado para pedido #101.
# Estoque disponível para pedido #101.
# Pedido #101 confirmado! Enviado para entrega.

# Processando pedido #102...
# Pagamento aprovado para pedido #102.
# Estoque indisponível para pedido #102. Pedido cancelado.

# Processando pedido #103...
# Pagamento recusado para pedido #103. Pedido cancelado.

# Todos os pedidos foram processados!
