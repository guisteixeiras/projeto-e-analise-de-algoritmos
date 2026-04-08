agenda = {} 

def adicionar_contato(agenda, nome, telefone):
    if nome in agenda:
        print(f"Não foi possível adicionar. O nome '{nome}' já existe.")
        return

    if telefone in agenda.values():
        print(f"Não foi possível adicionar. O telefone '{telefone}' já está cadastrado.")
        return

    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso.")

def ler_contato(agenda, nome):
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado.")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def listar_contatos(agenda):
    if not agenda:
        print("Agenda vazia.")
        return

    print("\nContatos cadastrados:")
    for nome, telefone in agenda.items():
        print(f"{nome} -> {telefone}")

adicionar_contato(agenda, "Ana", "99999-1111")
adicionar_contato(agenda, "Bruno", "99999-2222")
adicionar_contato(agenda, "Ana", "99999-3333")      
adicionar_contato(agenda, "Carlos", "99999-2222")  

ler_contato(agenda, "Ana")
remover_contato(agenda, "Bruno")
listar_contatos(agenda)