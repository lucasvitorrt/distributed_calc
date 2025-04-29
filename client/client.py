import Pyro5.api

def main():
    
    calculadora = Pyro5.api.Proxy("PYRONAME:dist.calculadora")
    
    #Como a rede deve permiti Bradcast UDP, caso queira utilizar em uma outra maquina o acesso a classe
    #distribuída, substituir o "0.0.0.0" pelo ip do servidor.
    #ns = Pyro5.api.locate_ns(host="0.0.0.0")
    #uri = ns.lookup("dist.calculadora")
    #calculadora = Pyro5.api.Proxy(uri)

    while True:
        print("\n--- CALCULADORA DISTRIBUÍDA ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Exponenciação")
        print("0. Sair\n")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("\nResultado:", calculadora.somar(a, b))
            elif opcao == '2':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("\nResultado:", calculadora.subtrair(a, b))
            elif opcao == '3':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("\nResultado:", calculadora.multiplicar(a, b))
            elif opcao == '4':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("\nResultado:", calculadora.dividir(a, b))
            elif opcao == '5':
                a = float(input("Digite o número: "))
                print("\nResultado:", calculadora.raiz_quadrada(a))
            elif opcao == '6':
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                print("\nResultado:", calculadora.exponenciar(base, expoente))
            elif opcao == '0':
                print("\nSaindo...")
                break
            else:
                print("\nOpção inválida!")
        except Exception as e:
            print("\nErro:", e)

if __name__ == "__main__":
    main()

