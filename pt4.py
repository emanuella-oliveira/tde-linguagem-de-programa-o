def marcar_tarefa_concluida(tarefa):
  "Acao especifica para marcar como concluida."
  if tarefa['concluida']:
    print(f"\ni A tarefa ID {tarefa['id']} ja estava CONCLUÍDA")
  else:
    tarefa['concluida']=TRUE
    print(f"\n Tarefa ID {tarefa['id']} marcada como CONCLUÍDA: {tarefa['descricao']}).
