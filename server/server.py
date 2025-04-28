import grpc
from concurrent import futures
import sys
import os

# Permite importar o proto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proto')))
import proto.calculator_pb2 as calculator_pb2
import proto.calculator_pb2_grpc as calculator_pb2_grpc
import math

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return calculator_pb2.Result(value=request.a + request.b)

    def Subtract(self, request, context):
        return calculator_pb2.Result(value=request.a - request.b)

    def Multiply(self, request, context):
        return calculator_pb2.Result(value=request.a * request.b)

    def Divide(self, request, context):
        if request.b == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Divisão por zero!')
            return calculator_pb2.Result()
        return calculator_pb2.Result(value=request.a / request.b)

    def Sqrt(self, request, context):
        if request.a < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Raiz quadrada de número negativo!')
            return calculator_pb2.Result()
        return calculator_pb2.Result(value=math.sqrt(request.a))

    def Power(self, request, context):
        return calculator_pb2.Result(value=math.pow(request.a, request.b))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
