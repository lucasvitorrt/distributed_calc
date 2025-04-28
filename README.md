
# 📚 Calculadora Distribuída gRPC

Este projeto implementa uma **calculadora distribuída** usando **gRPC** em **Python**, com operações básicas expostas remotamente para serem usadas por um cliente.

## 📂 Estrutura do Projeto

```
calculadora-grpc/
├── client/
│   └── client.py
├── server/
│   └── server.py
├── proto/
│   ├── calculator.proto
│   ├── calculator_pb2.py
│   └── calculator_pb2_grpc.py
├── Makefile
└── README.md
```

## ⚙️ Tecnologias Usadas

- Python 3.10+
- gRPC
- Protobuf
- Makefile

## 🔧 Pré-requisitos

Antes de rodar o projeto, instale as dependências necessárias:

```bash
pip install grpcio grpcio-tools
```

## 🚀 Instruções de Uso

Clone o repositório:

```bash
git clone https://github.com/lucasvitorrt/distributed_calc.git
cd calculadora-grpc
```

### 1. Gerar os arquivos a partir do `.proto`

**(Execute uma vez para gerar `calculator_pb2.py` e `calculator_pb2_grpc.py`)**

```bash
make proto
```

### 2. Iniciar o Servidor

```bash
make server
```
O servidor gRPC será iniciado e ficará escutando na porta `50051`.

### 3. Iniciar o Cliente

Em outro terminal (também dentro da pasta do projeto):

```bash
make client
```
O cliente entrará em um loop interativo para que você escolha e execute as operações:

- Soma
- Subtração
- Multiplicação
- Divisão
- Raiz Quadrada
- Exponenciação

Digite `0` para sair.

## 🎯 Funcionalidades Implementadas

- Operações matemáticas básicas e avançadas
- Comunicação Cliente-Servidor via gRPC
- Estrutura de projeto organizada
- Automação com Makefile

## 🛠️ Comandos Úteis

| Comando        | Descrição                                |
|:---------------|:-----------------------------------------|
| `make proto`   | Gera o código gRPC a partir do `.proto`   |
| `make server`  | Inicia o servidor gRPC                   |
| `make client`  | Inicia o cliente gRPC                    |

## 📢 Observações

- Certifique-se de que o servidor esteja rodando **antes** de iniciar o cliente.
- Em caso de erro, verifique se a versão do Python é compatível (3.10 ou superior recomendado).
- O projeto usa comunicação sem autenticação (ideal para ambientes de testes).

## 🧑‍💻 Autor

- Nome: **Lucas Vitor**
- GitHub: [@lucasvitorrt](https://github.com/lucasvitorrt)

---