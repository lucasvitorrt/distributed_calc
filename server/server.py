import Pyro5.api
import Pyro5.server

@Pyro5.api.expose
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida.")
        return a / b

    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Raiz quadrada de número negativo não permitida.")
        return a ** 0.5

    def exponenciar(self, base, expoente):
        return base ** expoente

def main():
    # Substitua '0.0.0.0' pelo IP real da máquina do servidor, se quiser restringir
    #daemon = Pyro5.server.Daemon(host="0.0.0.0")  # Escuta em todas as interfaces
    daemon = Pyro5.server.Daemon()       # Cria uma instância de daemon Pyro, que é responsável por escutar requisições remotas vindas de clientes e direcioná-las para os objetos Python corretos. Ele atua como um "servidor RPC" (Remote Procedure Call).
    ns = Pyro5.api.locate_ns()           # Conecta-se ao servidor de nomes do Pyro5 (pyro5-ns), que deve estar previamente em execução.
    uri = daemon.register(Calculadora)   # Registra a classe Calculadora no daemon Pyro.
    ns.register("dist.calculadora", uri) # Associa o nome "dist.calculadora" ao URI gerado anteriormente, tornando o objeto acessível por esse nome simbólico.
    print("Servidor pronto.")
    daemon.requestLoop()                 # Inicia o loop de escuta do daemon.

if __name__ == "__main__":
    main()
