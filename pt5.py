def editar_tarefa(tarefa):
  """Ação específica para editar a descrição."""
  print(f"\nTarefa atual (ID {tarefa['id']}): {tarefa['descricao']}")

  while True:
      nova_descricao = input("Digite a nova descrição (deixe vazio para cancelar): ").strip()
      if not nova_descricao:
          print("\Operação de edição cancelada.")
          break

      tarefa['descricao'] = nova_descricao
      print(f"\nTarefa ID {tarefa['id']} editada com sucesso!")
      break
    
    
    
