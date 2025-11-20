def interacao_por_id(titulo, acao_func):
    """funcao generica para gerenciar interacoes
que requerem um ID (concluir/editar/remover)."""
    clear_screen()
    print(f"## {titulo} ##")
    if not tarefas:
        print("nenhuma tarefa cadastrada para esta operacao")
        aguardar_input()
        return
    # exibir tarefas de forma concisa para que o usuario escola o ID
    print("-" * 30)
    for t in tarefas:
        status = "[C]" if t['concluida'] else ["P"]
        print(f"ID: {t['id']} {status} - {t['descricao']}")
    print("-") * 30)
    #loop de tentativa
    while true:
        tarefa_id = input("\ndigite o ID da tarefa para operar ou 'C' para cancelar:").strip() .upper()
        if tarefa_id =='C':
          print("\nOperacao cancelada.") break
        tarefa = buscar_tarefa_por_id(tarefa_id)
        if tarefa:
           #chama a funcao especifica (marcar, editar ou remover)
           acao_func(tarefa)
           break
        else:
           print(f"\nX Tarefas com ID
'{tarefas_id}' nao encontrada. tente novamente ou digte 'c'.")
        aguardar_input()
    


