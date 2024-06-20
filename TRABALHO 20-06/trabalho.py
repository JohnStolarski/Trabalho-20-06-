"""
Sistema de Estacionamento

Este programa permite o cadastro, retirada e consulta de veículos em um estacionamento.
Utiliza dicionários para armazenar informações dos veículos.

Data de criação: 20/06/2024
"""

# Dicionário para armazenar os veículos estacionados
estacionamento = {}

def estacionar_veiculo(placa, marca, modelo, cor, proprietario):
    """
    Estaciona um veículo no estacionamento.

    Parâmetros:
    placa (str): A placa do veículo (chave no dicionário).
    marca (str): A marca do veículo.
    modelo (str): O modelo do veículo.
    cor (str): A cor do veículo.
    proprietario (str): O nome do proprietário do veículo.
    """
    global estacionamento
    estacionamento[placa] = {
        'marca': marca,
        'modelo': modelo,
        'cor': cor,
        'proprietario': proprietario
    }
    print(f"Veículo com placa '{placa}' estacionado com sucesso.")

def retirar_veiculo(placa):
    """
    Retira um veículo do estacionamento.

    Parâmetros:
    placa (str): A placa do veículo a ser retirado.
    """
    global estacionamento
    if placa in estacionamento:
        veiculo = estacionamento.pop(placa)
        print(f"Veículo com placa '{placa}' foi retirado do estacionamento.")
    else:
        print(f"Veículo com placa '{placa}' não encontrado no estacionamento.")

def veiculos_estacionados():
    """
    Exibe todos os veículos atualmente estacionados no estacionamento.
    """
    global estacionamento
    if estacionamento:
        print("Veículos estacionados:")
        for placa, info in estacionamento.items():
            print(f"Placa: {placa}, Marca: {info['marca']}, Modelo: {info['modelo']}, Cor: {info['cor']}, Proprietário: {info['proprietario']}")
    else:
        print("Não há veículos estacionados no momento.")

def esta_estacionado(placa):
    """
    Verifica se um veículo está estacionado no estacionamento.

    Parâmetros:
    placa (str): A placa do veículo a ser verificado.
    """
    global estacionamento
    if placa in estacionamento:
        print(f"O veículo com placa '{placa}' está estacionado.")
    else:
        print(f"O veículo com placa '{placa}' não está estacionado.")

def main():
    """
    Função principal que controla o menu e interações com o usuário.
    """
    while True:
        print("\n*** Menu ***")
        print("1 - Estacionar veículo")
        print("2 - Retirar veículo")
        print("3 - Veículos estacionados")
        print("4 - Está estacionado?")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Digite a placa do veículo: ")
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            cor = input("Digite a cor do veículo: ")
            proprietario = input("Digite o nome do proprietário: ")
            estacionar_veiculo(placa, marca, modelo, cor, proprietario)
        
        elif opcao == '2':
            placa = input("Digite a placa do veículo a ser retirado: ")
            retirar_veiculo(placa)
        
        elif opcao == '3':
            veiculos_estacionados()
        
        elif opcao == '4':
            placa = input("Digite a placa do veículo a ser verificado: ")
            esta_estacionado(placa)
        
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()