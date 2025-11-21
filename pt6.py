def remover_tarefa(tarefa):
    """Ação específica para remover a tarefa."""
    global tarefas
    confirmacao = input(f"Tem certeza que deseja remover a tarefa ID {tarefa['id']} ('{tarefa['descricao']}')? (S/N): ").strip().upper()
    
    if confirmacao == 'S':
        tarefas.remove(tarefa)
        print(f"\n🗑️ Tarefa ID {tarefa['id']} removida com sucesso!")
    else:
        print("\nRemoção cancelada.")
