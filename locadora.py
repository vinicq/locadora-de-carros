import os

carros_disponiveis = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
    ("Toyota Corolla", 150),
    ("Toyota Hilux", 200),
    ("Ford Ka", 80),
    ("Ford EcoSport", 140),
    ("Volkswagen Gol", 75),
    ("Volkswagen Polo", 100),
    ("Volkswagen T-Cross", 160),
    ("Honda Civic", 150),
    ("Honda Fit", 90),
    ("Honda HR-V", 170),
    ("Renault Kwid", 60),
    ("Renault Duster", 130),
    ("Jeep Renegade", 160),
    ("Jeep Compass", 190),
    ("Nissan Kicks", 140),
    ("Nissan Versa", 110),
    ("Peugeot 208", 90),
    ("Peugeot 3008", 180),
    ("Citroën C3", 85),
    ("Citroën C4 Cactus", 140),
    ("BMW Série 3", 300),
    ("BMW X1", 350),
    ("Mercedes-Benz Classe A", 320),
    ("Mercedes-Benz GLA", 400),
    ("Audi A3", 280),
    ("Audi Q3", 350),
    ("Land Rover Discovery Sport", 450),
    ("Volvo XC40", 400),
    ("Tesla Model 3", 500),
    ("Tesla Model Y", 600)
]

carros_alugados = []


def limpar_tela():
    os.system("clear" if os.name == "posix" else "cls")

def mostrar_lista_de_carros(lista, titulo="Carros Disponíveis"):
    print(f"=== {titulo} ===")
    for i, (modelo, preco) in enumerate(lista):
        print(f"[{i}] {modelo} - R$ {preco} / dia")
    print("=========================")

def alugar_carro():
    if not carros_disponiveis:
        print("Nenhum carro disponível para aluguel no momento.")
        return

    mostrar_lista_de_carros(carros_disponiveis)
    try:
        cod_car = int(input("Escolha o código do carro que deseja alugar: "))
        if cod_car < 0 or cod_car >= len(carros_disponiveis):
            print("Código inválido.")
            return

        dias = int(input("Por quantos dias você deseja alugar este carro? "))
        if dias <= 0:
            print("Quantidade de dias inválida.")
            return

        modelo, preco = carros_disponiveis[cod_car]
        total = dias * preco

        print(f"Você escolheu {modelo} por {dias} dias.")
        print(f"O aluguel totalizaria R$ {total:.2f}. Deseja alugar?")
        confirmacao = input("Digite 'S' para confirmar ou qualquer outra tecla para cancelar: ").strip().lower()
        if confirmacao == "s":
            carros_alugados.append(carros_disponiveis.pop(cod_car))
            print(f"Parabéns! Você alugou o {modelo} por {dias} dias.")
        else:
            print("Aluguel cancelado.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def devolver_carro():
    if not carros_alugados:
        print("Não há carros para devolver.")
        return

    mostrar_lista_de_carros(carros_alugados, titulo="Carros Alugados")
    try:
        cod_car = int(input("Escolha o código do carro que deseja devolver: "))
        if cod_car < 0 or cod_car >= len(carros_alugados):
            print("Código inválido.")
            return

        modelo, _ = carros_alugados.pop(cod_car)
        carros_disponiveis.append((modelo, _))
        print(f"Obrigado por devolver o carro {modelo}.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

while True:
    limpar_tela()
    print("======== LOCADORA DE CARROS ========")
    print("O que deseja fazer?")
    print("1 - Mostrar Portfólio")
    print("2 - Alugar um Carro")
    print("3 - Devolver um Carro")
    print("0 - Sair")
    print("====================================")

    try:
        opcao = int(input("Escolha uma opção: "))
        limpar_tela()

        if opcao == 1:
            mostrar_lista_de_carros(carros_disponiveis)
        elif opcao == 2:
            alugar_carro()
        elif opcao == 3:
            devolver_carro()
        elif opcao == 0:
            print("Obrigado por usar a locadora! Até mais.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
    except ValueError:
        print("Entrada inválida. Tente novamente.")
