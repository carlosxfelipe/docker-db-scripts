# MySQL Docker Script

Este script interativo cria e inicia um container Docker com MySQL, solicitando os parâmetros básicos ao usuário.

## Pré-requisitos

- Docker em execução no sistema

## Como usar

1. Abra o terminal.
2. Execute o script:

```bash
python run-mysql.py
```

3. Informe os dados solicitados (usuário, senha, porta, nome do container, volume e versão do MySQL).
4. O container será iniciado automaticamente.
5. Um arquivo `dados_conexao_mysql.txt` será gerado com todas as informações de conexão.

## Observações

- A senha do usuário `root` não pode estar em branco.
- O script usa a imagem oficial `mysql`.
- O volume Docker é persistente.
