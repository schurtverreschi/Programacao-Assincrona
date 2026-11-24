import asyncio

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}

alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]

# Cria um Lock independente para cada curso
locks = {curso: asyncio.Lock() for curso in cursos}


async def verificar_matricula(inscricao):
    await asyncio.sleep(1)  # Simula tempo de consulta de matricula

    nome_aluno = inscricao["nome"]
    nome_curso = inscricao["curso"]

    if nome_aluno in cursos[nome_curso]["inscritos"]:
        print(
            f"{nome_aluno} já está inscrito(a) no curso {nome_curso}! Inscrição rejeitada."
        )
        return False
    return True


async def verificar_vagas(inscricao):
    await asyncio.sleep(1)  # Simula tempo de consulta de vagas

    nome_aluno = inscricao["nome"]
    nome_curso = inscricao["curso"]

    if cursos[nome_curso]["vagas"] == 0:
        print(
            f"Turma lotada! {nome_aluno} não pôde se inscrever no curso {nome_curso}."
        )
        return False
    return True


async def processar_inscricao(inscricao):
    nome_aluno = inscricao["nome"]
    nome_curso = inscricao["curso"]

    print(f"Inscrevendo {nome_aluno} no curso {nome_curso}...")

    if nome_curso not in cursos:
        print(f"Erro! O curso {nome_curso} não existe.\n")
        return

    async with locks[nome_curso]:
        matricula_ok = await verificar_matricula(inscricao)
        if not matricula_ok:
            return
        vagas_ok = await verificar_vagas(inscricao)
        if not vagas_ok:
            return

        await asyncio.sleep(2)  # Simula tempo para realizar matricula

        cursos[nome_curso]["vagas"] -= 1
        cursos[nome_curso]["inscritos"].append(nome_aluno)
        print(f"Inscrição confirmada para {nome_aluno} no curso {nome_curso}!")


async def main():
    tarefas = [processar_inscricao(matricula) for matricula in alunos]

    await asyncio.gather(*tarefas)

    print("\nTodas as inscrições foram processadas!")
    print("\n--- Relatório Final de Inscrições ---\n")
    for curso, dados in cursos.items():
        inscritos = ", ".join(dados["inscritos"]) if dados["inscritos"] else "Nenhum"
        print(
            f"{curso:.<23}: {dados['vagas']:>2} vaga(s) restante(s) {'':<1}| Inscritos: {inscritos}"
        )
    print()


asyncio.run(main())


# Python Avançado: 0 vaga(s) restante(s) | Inscritos: Alice, Bruno
# Java para Iniciantes: 0 vaga(s) restante(s) | Inscritos: Carlos
# Machine Learning: 0 vaga(s) restante(s) | Inscritos: Nenhum

# Gerenciando inscrições em cursos

# Paula trabalha em uma plataforma de ensino online e precisa garantir que os alunos sejam inscritos corretamente nos cursos desejados. O sistema deve seguir as seguintes regras:

# Cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponíveis;
# Se houver vagas, o aluno deve ser confirmado na turma e a vaga deve ser reduzida;
# Se não houver vagas, o aluno deve ser notificado de que a turma está lotada;
# Se um aluno já estiver inscrito, ele não pode se inscrever novamente no mesmo curso.

# A lista de alunos e os cursos disponíveis já está definida no sistema. Lembre-se de processar múltiplas inscrições em paralelo. Confira o código:

# cursos = {
#     "Python Avançado": {"vagas": 2, "inscritos": []},
#     "Java para Iniciantes": {"vagas": 1, "inscritos": []},
#     "Machine Learning": {"vagas": 0, "inscritos": []},
# }

# alunos = [
#     {"nome": "Alice", "curso": "Python Avançado"},
#     {"nome": "Bruno", "curso": "Python Avançado"},
#     {"nome": "Carlos", "curso": "Java para Iniciantes"},
#     {"nome": "Daniela", "curso": "Machine Learning"},
#     {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
# ]

# Saída esperada:

# Inscrevendo Alice no curso Python Avançado...
# Inscrição confirmada para Alice no curso Python Avançado!

# Inscrevendo Bruno no curso Python Avançado...
# Inscrição confirmada para Bruno no curso Python Avançado!

# Inscrevendo Carlos no curso Java para Iniciantes...
# Inscrição confirmada para Carlos no curso Java para Iniciantes!

# Inscrevendo Daniela no curso Machine Learning...
# Turma lotada! Daniela não pôde se inscrever no curso Machine Learning.

# Inscrevendo Alice no curso Python Avançado...
# Alice já está inscrita no curso Python Avançado! Inscrição rejeitada.

# Todas as inscrições foram processadas!
