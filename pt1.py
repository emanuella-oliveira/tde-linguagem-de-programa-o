import os
import time

# --- Estrutura de Dados Global ---
tarefas = []
proximo_id = 1

# --- Funções de Ajuda ---

def clear_screen():
    """Limpa o console para uma experiência mais limpa."""
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_tarefa_por_id(id_alvo):
    """Função auxiliar para encontrar uma tarefa pelo ID."""
    try:
        id_alvo = int(id_alvo)
        for tarefa in tarefas:
            if tarefa['id'] == id_alvo:
                return tarefa
        return None
    except ValueError:
        return None

def aguardar_input():
    """Pausa para o usuário ler a mensagem antes de continuar."""
    input("\n[ENTER] para retornar ao menu principal...")

# --- Funções de Manipulação de Tarefas ---

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    global proximo_id
    clear_screen()
    print("## ➕ Adicionar Nova Tarefa ##")
    
    # Loop de repetição caso o usuário tente adicionar uma descrição vazia
    while True:
        descricao = input("Digite a descrição da nova tarefa: ").strip()
        
        if descricao:
            nova_tarefa = {
                "id": proximo_id,
                "descricao": descricao,
                "concluida": False
            }
            tarefas.append(nova_tarefa)
            proximo_id += 1
            print(f"\n✅ Tarefa '{descricao}' adicionada com sucesso! (ID: {nova_tarefa['id']})")
            break
        else:
            print("\n❌ A descrição não pode ser vazia. Tente novamente.")
        
    aguardar_input()