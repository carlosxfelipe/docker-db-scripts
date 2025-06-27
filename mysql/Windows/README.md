# MySQL Docker - Inicialização com .BAT

Este projeto inclui um script `.bat` que inicia um container Docker com o MySQL.

## Como usar

1. Verifique se o Docker está instalado e em execução.
2. Execute o arquivo `.bat` no Windows com um clique duplo ou via terminal (cmd).

O comando no `.bat` cria o container com:

- Porta padrão do MySQL (3306)
- Volume persistente `mysql_data`
- Nome do container `mysql-container`
- Senha predefinida para o usuário `root`

## Informações de Conexão

Use os dados abaixo para se conectar ao MySQL rodando no seu container com ferramentas como DBeaver, Beekeeper Studio, TablePlus, etc.

| Parâmetro             | Valor               | Descrição                                              |
|----------------------|---------------------|--------------------------------------------------------|
| **Host**             | `localhost`         | O container está rodando localmente                    |
| **Porta (Port)**     | `3306`              | Porta padrão do MySQL                                  |
| **Usuário (User)**   | `root`              | Usuário administrador padrão                           |
| **Senha (Password)** | `Bellemosca@123`    | Senha definida no script Docker                        |
| **Database**         | `mysql` (default)   | Banco padrão, você pode criar outros                   |
| **Driver**           | `MySQL`             | Escolha o driver correspondente na ferramenta          |
| **Container**        | `mysql-container`   | Nome do container Docker                               |
