import grpc
import sys
import os

# Permite importar o proto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proto')))
import proto.calculator_pb2 as calculator_pb2
import proto.calculator_pb2_grpc as calculator_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    while True:
        print("\n--- CALCULADORA DISTRIBUÍDA gRPC ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Exponenciação")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                response = stub.Add(calculator_pb2.TwoNumbers(a=a, b=b))
                print("Resultado:", response.value)
            elif opcao == '2':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                response = stub.Subtract(calculator_pb2.TwoNumbers(a=a, b=b))
                print("Resultado:", response.value)
            elif opcao == '3':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                response = stub.Multiply(calculator_pb2.TwoNumbers(a=a, b=b))
                print("Resultado:", response.value)
            elif opcao == '4':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                try:
                    response = stub.Divide(calculator_pb2.TwoNumbers(a=a, b=b))
                    print("Resultado:", response.value)
                except grpc.RpcError as e:
                    print("Erro:", e.details())
            elif opcao == '5':
                a = float(input("Digite o número: "))
                try:
                    response = stub.Sqrt(calculator_pb2.OneNumber(a=a))
                    print("Resultado:", response.value)
                except grpc.RpcError as e:
                    print("Erro:", e.details())
            elif opcao == '6':
                a = float(input("Digite a base: "))
                b = float(input("Digite o expoente: "))
                response = stub.Power(calculator_pb2.TwoNumbers(a=a, b=b))
                print("Resultado:", response.value)
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    main()
