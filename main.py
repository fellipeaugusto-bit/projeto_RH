import os
from services.auth_service import AuthService
from services.dashboard_service import DashboardService
from dao.funcionario_dao import FuncionarioDAO
from dao.departamento_dao import DepartamentoDAO
from dao.cargo_dao import CargoDAO
from dao.log_dao import LogDAO
from models.funcionario import Funcionario
from models.departamento import Departamento
from models.cargo import Cargo

class SistemaRH:
    def __init__(self):
        self.auth_service = AuthService()
        self.dashboard_service = DashboardService()
        self.funcionario_dao = FuncionarioDAO()
        self.departamento_dao = DepartamentoDAO()
        self.cargo_dao = CargoDAO()
        self.log_dao = LogDAO()
        self.usuario_logado = None

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_menu_principal(self):
        while True:
            self.limpar_tela()
            print("=== SISTEMA DE GESTÃO DE RH ===")
            print("1. Dashboard")
            print("2. Gestão de Funcionários")
            print("3. Gestão de Departamentos")
            print("4. Gestão de Cargos")
            print("5. Visualizar Logs")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exibir_dashboard()
            elif opcao == '2':
                self.menu_funcionarios()
            elif opcao == '3':
                self.menu_departamentos()
            elif opcao == '4':
                self.menu_cargos()
            elif opcao == '5':
                self.exibir_logs()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                input("Opção inválida. Pressione Enter para continuar...")

    def exibir_dashboard(self):
        self.limpar_tela()
        stats = self.dashboard_service.obter_estatisticas()
        print("=== DASHBOARD ===")
        print(f"Total de Funcionários: {stats['total_funcionarios']}")
        print(f"Total de Departamentos: {stats['total_departamentos']}")
        print(f"Total de Cargos: {stats['total_cargos']}")
        print("\nÚltimos 5 logs do sistema:")
        logs = self.log_dao.listar_ultimos(5)
        for log in logs:
            print(f"[{log['data_hora']}] {log['usuario']}: {log['acao']}")
        input("\nPressione Enter para voltar...")

    def menu_funcionarios(self):
        while True:
            self.limpar_tela()
            print("=== GESTÃO DE FUNCIONÁRIOS ===")
            print("1. Cadastrar Funcionário")
            print("2. Listar Funcionários")
            print("3. Pesquisar Funcionário")
            print("4. Atualizar Funcionário")
            print("5. Excluir Funcionário")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_funcionario()
            elif opcao == '2':
                self.listar_funcionarios()
            elif opcao == '3':
                self.pesquisar_funcionario()
            elif opcao == '4':
                self.atualizar_funcionario()
            elif opcao == '5':
                self.excluir_funcionario()
            elif opcao == '0':
                break

    def cadastrar_funcionario(self):
        self.limpar_tela()
        print("=== CADASTRO DE FUNCIONÁRIO ===")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        
        print("\nCargos disponíveis:")
        cargos = self.cargo_dao.listar_todos()
        for c in cargos:
            print(f"ID: {c['id']} | Nome: {c['nome']}")
        cargo_id = int(input("ID do Cargo: "))
        
        salario = float(input("Salário: "))
        
        print("\nDepartamentos disponíveis:")
        deptos = self.departamento_dao.listar_todos()
        for d in deptos:
            print(f"ID: {d['id']} | Nome: {d['nome']}")
        depto_id = int(input("ID do Departamento: "))

        func = Funcionario(nome, cpf, email, telefone, cargo_id, salario, depto_id)
        self.funcionario_dao.cadastrar(func)
        self.log_dao.registrar(self.usuario_logado, f"Cadastrou funcionário: {nome}")
        print("\n✓ Funcionário cadastrado com sucesso!")
        input("Pressione Enter para continuar...")

    def listar_funcionarios(self):
        self.limpar_tela()
        print("=== LISTA DE FUNCIONÁRIOS ===")
        funcs = self.funcionario_dao.listar_todos()
        print(f"{'ID':<4} | {'Nome':<20} | {'CPF':<14} | {'Cargo':<20} | {'Salário':<10} | {'Departamento':<15}")
        print("-" * 90)
        for f in funcs:
            print(f"{f['id']:<4} | {f['nome']:<20} | {f['cpf']:<14} | {f['cargo_nome']:<20} | R$ {f['salario']:<8.2f} | {f['depto_nome']:<15}")
        input("\nPressione Enter para continuar...")

    def pesquisar_funcionario(self):
        self.limpar_tela()
        print("=== PESQUISAR FUNCIONÁRIO ===")
        print("1. Por Nome")
        print("2. Por CPF")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            nome = input("Digite o nome: ")
            funcs = self.funcionario_dao.pesquisar_por_nome(nome)
        elif opcao == '2':
            cpf = input("Digite o CPF: ")
            funcs = self.funcionario_dao.pesquisar_por_cpf(cpf)
        else:
            return

        print("\nResultados:")
        for f in funcs:
            print(f"ID: {f['id']} | Nome: {f['nome']} | Cargo: {f['cargo_nome']}")
        input("\nPressione Enter para continuar...")

    def atualizar_funcionario(self):
        self.limpar_tela()
        print("=== ATUALIZAR FUNCIONÁRIO ===")
        id_func = int(input("ID do funcionário a atualizar: "))
        
        print("\nNovos dados (deixe em branco para manter ou digite novos):")
        email = input("Novo Email: ")
        telefone = input("Novo Telefone: ")
        
        print("\nCargos disponíveis:")
        cargos = self.cargo_dao.listar_todos()
        for c in cargos:
            print(f"ID: {c['id']} | Nome: {c['nome']}")
        cargo_id = int(input("Novo ID do Cargo: "))
        
        salario = float(input("Novo Salário: "))
        
        print("\nDepartamentos disponíveis:")
        deptos = self.departamento_dao.listar_todos()
        for d in deptos:
            print(f"ID: {d['id']} | Nome: {d['nome']}")
        depto_id = int(input("Novo ID do Departamento: "))

        self.funcionario_dao.atualizar(id_func, cargo_id, salario, depto_id, telefone, email)
        self.log_dao.registrar(self.usuario_logado, f"Atualizou funcionário ID: {id_func}")
        print("\n✓ Funcionário atualizado com sucesso!")
        input("Pressione Enter para continuar...")

    def excluir_funcionario(self):
        self.limpar_tela()
        print("=== EXCLUIR FUNCIONÁRIO ===")
        id_func = int(input("ID do funcionário a remover: "))
        self.funcionario_dao.excluir(id_func)
        self.log_dao.registrar(self.usuario_logado, f"Removeu funcionário ID: {id_func}")
        print("\n✓ Funcionário removido com sucesso!")
        input("Pressione Enter para continuar...")

    def menu_departamentos(self):
        while True:
            self.limpar_tela()
            print("=== GESTÃO DE DEPARTAMENTOS ===")
            print("1. Cadastrar Departamento")
            print("2. Listar Departamentos")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome do Departamento: ")
                gerente = input("Nome do Gerente: ")
                depto = Departamento(nome, gerente)
                self.departamento_dao.cadastrar(depto)
                self.log_dao.registrar(self.usuario_logado, f"Cadastrou departamento: {nome}")
                print("\n✓ Departamento cadastrado com sucesso!")
                input("Pressione Enter para continuar...")
            elif opcao == '2':
                self.limpar_tela()
                deptos = self.departamento_dao.listar_todos()
                for d in deptos:
                    print(f"ID: {d['id']} | Nome: {d['nome']} | Gerente: {d['gerente']}")
                input("\nPressione Enter para continuar...")
            elif opcao == '0':
                break

    def menu_cargos(self):
        while True:
            self.limpar_tela()
            print("=== GESTÃO DE CARGOS ===")
            print("1. Cadastrar Cargo")
            print("2. Listar Cargos")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome do Cargo: ")
                salario_base = float(input("Salário Base: "))
                cargo = Cargo(nome, salario_base)
                self.cargo_dao.cadastrar(cargo)
                self.log_dao.registrar(self.usuario_logado, f"Cadastrou cargo: {nome}")
                print("\n✓ Cargo cadastrado com sucesso!")
                input("Pressione Enter para continuar...")
            elif opcao == '2':
                self.limpar_tela()
                cargos = self.cargo_dao.listar_todos()
                for c in cargos:
                    print(f"ID: {c['id']} | Nome: {c['nome']} | Salário Base: R$ {c['salario_base']:.2f}")
                input("\nPressione Enter para continuar...")
            elif opcao == '0':
                break

    def exibir_logs(self):
        self.limpar_tela()
        print("=== LOGS DO SISTEMA ===")
        logs = self.log_dao.listar_todos()
        for log in logs:
            print(f"[{log['data_hora']}] Usuário: {log['usuario']} | Ação: {log['acao']}")
        input("\nPressione Enter para continuar...")

    def iniciar(self):
        self.limpar_tela()
        print("=== LOGIN DO SISTEMA ===")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if self.auth_service.login(usuario, senha):
            self.usuario_logado = usuario
            self.log_dao.registrar(usuario, "Login realizado")
            print("\n✓ Login realizado com sucesso!")
            input("Pressione Enter para acessar o sistema...")
            self.exibir_menu_principal()
        else:
            print("\nLogin inválido.")
            input("Pressione Enter para sair...")

if __name__ == "__main__":
    sistema = SistemaRH()
    sistema.iniciar()
