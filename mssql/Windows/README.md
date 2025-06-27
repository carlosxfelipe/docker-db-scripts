# SQL Server Docker - Inicialização com .BAT

Este projeto inclui um script `.bat` que inicia um container Docker com o SQL Server 2022.

## Como usar

1. Verifique se o Docker está instalado e em execução.
2. Execute o arquivo `.bat` no Windows com um clique duplo ou via terminal (cmd).

O comando no `.bat` cria o container com:

- Porta padrão do SQL Server (1433)
- Volume persistente `sqlserver_data`
- Nome do container `sqlserver-container`
- Senha predefinida para o usuário `SA`

## Informações de Conexão

Use os dados abaixo para se conectar ao SQL Server rodando no seu container com ferramentas como TablePlus, Beekeeper Studio, DBeaver, etc.

| Parâmetro             | Valor                      | Descrição                                              |
| --------------------- | -------------------------- | ------------------------------------------------------ |
| **Host**              | `localhost`                | O container está rodando localmente                    |
| **Porta (Port)**      | `1433`                     | Porta padrão do SQL Server                             |
| **Usuário (User)**    | `SA`                       | Usuário administrador padrão                           |
| **Senha (Password)**  | `Bellemosca@123`           | Senha definida no script Docker                        |
| **Database**          | `master` (ou outro criado) | Banco padrão, pode criar e usar outro se desejar       |
| **Driver**            | `SQL Server` / `MSSQL`     | Escolha o driver SQL Server na ferramenta              |
| **Nome do Container** | `sqlserver-container`      | Nome do container Docker (não é necessário na conexão) |
