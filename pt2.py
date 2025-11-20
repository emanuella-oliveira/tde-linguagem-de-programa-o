def listar_tarefas():
    "Exibe todas as tarefas com formatação interativa."
    clear_screen() #pyright: ignore [reportUndefinedVariable]
    
#1. Cabeçalho e Estatísticas
print("=" * 60)
print("LISTA DE TAREFAS ATUAIS")
print("=" * 60)

if not tarefa:
    print("\nNenhuma tarefa cadastrada. Hora de adicionar algumas!")
    print("-" * 60)
    aguardar_input() #pyright: ignore[reportUnderfinedVariable] 
return

#2. Exibição Detalhada (incompletas primeiro)
tarefas_ordenadas = sorted(tarefa, key=lambda t: t['concluida'])

cont_pendentes = 0
cont_concluidas = 0

print(f"{'ID': < 5} | {'Status': < 15} | {'Descrição': < 35}")
print("-" * 60)

for tarefa in tarefas_ordenadas:
    if tarefa['concluida']:
        status_cor = "CONCLUÍDA"
        cont_concluidas += 1
    else:
        status_cor = "PENDENTE"
        cont_pendentes += 1
        
        print(f"{tarefa['id']: < 5} | {status_cor: < 15} | {tarefa['descrição']: < 35}")

print("-" * 60)
print(f"RESUMO: Pendentes: {cont_pendentes} | Concluídas: {cont_concluidas} | Total: {len(tarefa)}")
print("=" * 60)

aguardar_input()
