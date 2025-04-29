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
    daemon = Pyro5.server.Daemon()         # make a Pyro daemon
    ns = Pyro5.api.locate_ns()             # find the name server
    uri = daemon.register(Calculadora)   # register the greeting maker as a Pyro object
    ns.register("dist.calculadora", uri)
    print("Servidor pronto.")
    daemon.requestLoop()   

if __name__ == "__main__":
    main()
