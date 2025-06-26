# 💰 DIO's Bank - Sistema Bancário em Python

Este projeto foi desenvolvido durante o **Bootcamp de Python oferecido pelo Santander e a DIO**. Trata-se de um sistema bancário simples que permite realizar operações básicas como depósito, saque e visualização de extrato.

## 📋 Funcionalidades

- Depositar valores na conta
- Realizar saques com limite por operação e por quantidade diária
- Consultar o extrato bancário com o histórico de movimentações
- Validações de saldo, limite de saque e número de saques diários

## 🛠 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- Lógica de programação
- Estrutura de controle condicional (`if`, `elif`, `else`)
- Laços de repetição (`while`)
- Operações com números e strings

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em seu sistema.
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/dios-bank-python.git
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd dios-bank-python
   ```
4. Execute o arquivo Python:
   ```bash
   python dio_bank.py
   ```

## 💡 Exemplo de Uso

```text
***** Bem vindo ao DIO's Bank*****

O que deseja fazer hoje? Escolha uma opção abaixo

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

Powered By Python
```

O sistema solicitará a entrada do usuário para realizar operações e exibirá mensagens adequadas conforme as ações.

## 📌 Regras Implementadas

- O limite máximo por saque é de R$500.
- O número máximo de saques por sessão é 3.
- Depósitos e saques com valores negativos não são permitidos.
- O extrato exibe todas as transações e o saldo atual.

## 👨‍💻 Autor

Desenvolvido por **Moroni Pereira** durante o Bootcamp Python da DIO em parceria com o Santander.  
Sinta-se à vontade para contribuir, abrir issues ou dar uma ⭐ no projeto!
