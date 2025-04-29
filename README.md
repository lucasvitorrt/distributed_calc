# 🧮 Calculadora Distribuída com Pyro5

Este projeto implementa uma **calculadora distribuída** utilizando o framework [Pyro5](https://pyro5.readthedocs.io/), permitindo a realização de operações matemáticas remotamente entre cliente e servidor.

## 📦 Funcionalidades

A calculadora oferece as seguintes operações:

- Soma
- Subtração
- Multiplicação
- Divisão (com tratamento para divisão por zero)
- Raiz quadrada (com validação para números negativos)
- Exponenciação

## 📁 Estrutura do Projeto

- `server.py`: Servidor que expõe os métodos da calculadora via Pyro5.
- `client.py`: Cliente que acessa os métodos remotos da calculadora.
- `pyro5-ns`: Servidor de nomes do Pyro5 (não incluído no repositório; instalado com o Pyro5).

## 🚀 Como Executar

### 1. Pré-requisitos

Certifique-se de ter o Python instalado, juntamente com o Pyro5:

```cmd
pip install Pyro5
```

### 2. Inicie o servidor de nomes Pyro5

Antes de rodar o servidor e o cliente, **é necessário inicializar o servidor de nomes** do Pyro5. No terminal:

```cmd
pyro5-ns
```

> ⚠️ Este comando deve ser executado em um terminal separado e **mantido em execução**.

### 3. Execute o servidor

Em outro terminal, execute o servidor:

```cmd
python server.py
```

Você verá a mensagem:
```
Servidor pronto.
```

### 4. Execute o cliente

Por fim, em um terceiro terminal, execute o cliente:

```cmd
python client.py
```

A interface em linha de comando será apresentada para que você escolha a operação desejada.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pyro5 (Python Remote Objects)

## 🧑‍💻 Autores

- Lucas Vitor
