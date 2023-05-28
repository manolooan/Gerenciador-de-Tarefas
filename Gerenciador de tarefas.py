import pickle

class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.titulo}\nDescrição: {self.descricao}\nData de Vencimento: {self.data_vencimento}\nStatus: {status}\n"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

    def exibir_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            for tarefa in self.tarefas:
                print(tarefa)

    def salvar_tarefas(self, nome_arquivo):
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.tarefas, arquivo)

    def carregar_tarefas(self, nome_arquivo):
        try:
            with open(nome_arquivo, "rb") as arquivo:
                self.tarefas = pickle.load(arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

# Criando uma instância do gerenciador de tarefas
gerenciador = GerenciadorTarefas()

# Carregando tarefas existentes (se houver) do arquivo "tarefas.pkl"
gerenciador.carregar_tarefas("tarefas.pkl")

while True:
    # Exibindo o menu principal
    print("\n===== Gerenciador de Tarefas =====")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas")
    print("5. Salvar Tarefas")
    print("6. Sair")

    # Solicitando a escolha do usuário
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        # Adicionando uma nova tarefa
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        data_vencimento = input("Digite a data de vencimento da tarefa: ")
        tarefa = Tarefa(titulo, descricao, data_vencimento)
        gerenciador.adicionar_tarefa(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif escolha == "2":
        # Removendo uma tarefa existente
        gerenciador.exibir_tarefas()
        indice_tarefa = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if indice_tarefa >= 0 and indice_tarefa < len(gerenciador.tarefas):
            gerenciador.remover_tarefa(gerenciador.tarefas[indice_tarefa])
            print("Tarefa removida com sucesso!")

    elif escolha == "3":
        # Marcando uma tarefa como concluída
        gerenciador.exibir_tarefas()
        indice_tarefa = int(input("Digite o número da tarefa concluída: ")) - 1
        if indice_tarefa >= 0 and indice_tarefa < len(gerenciador.tarefas):
            gerenciador.tarefas[indice_tarefa].marcar_como_concluida()
            print("Tarefa marcada como concluída!")

    elif escolha == "4":
        # Exibindo todas as tarefas
        gerenciador.exibir_tarefas()

    elif escolha == "5":
        # Salvando as tarefas no arquivo "tarefas.pkl"
        gerenciador.salvar_tarefas("tarefas.pkl")
        print("Tarefas salvas com sucesso!")

    elif escolha == "6":
        # Salvando as tarefas antes de sair do programa
        gerenciador.salvar_tarefas("tarefas.pkl")
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")