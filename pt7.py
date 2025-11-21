def menu_principal():
    """Exibe o menu principal e gerencia o loop do sistema."""
    while True:
        clear_screen()
        print("=" * 50)
        print("     📝 SISTEMA TO DO INTERATIVO")
        print("=" * 50)
        print("1. ➕ Adicionar nova tarefa")
        print("2. 📜 Visualizar todas as tarefas")
        print("3. ✅ Marcar tarefa como concluída")
        print("4. ✏️ Editar tarefa (descrição)")
        print("5. 🗑️ Remover tarefa")
        print("6. 🚪 Sair do sistema")
        print("-" * 50)
        
        escolha = input("🔑 Digite sua escolha (1-6): ").strip()
        
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            interacao_por_id("✅ Marcar como Concluída", marcar_tarefa_concluida)
        elif escolha == '4':
            interacao_por_id("✏️ Editar Descrição", editar_tarefa)
        elif escolha == '5':
            interacao_por_id("🗑️ Remover Tarefa", remover_tarefa)
        elif escolha == '6':
            clear_screen()
            print("👋 Obrigado por usar o Organizador de Tarefas! Até logo.")
            time.sleep(1) 
            break
        else:
            print("\n⚠️ Escolha inválida. Por favor, digite um número de 1 a 6.")
            aguardar_input()

# --- Inicialização do Sistema ---
if _name_ == "_main_":
    menu_principal()
