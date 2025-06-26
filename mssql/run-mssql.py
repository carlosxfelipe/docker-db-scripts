import subprocess


def prompt(texto, padrao):
    entrada = input(f"{texto} (default: {padrao}): ").strip()
    return padrao if entrada.lower() in ["", "default"] else entrada


username = prompt("Informe o usuário", "SA")

while True:
    password = input(f"Informe a senha para o usuário {username}: ").strip()
    if password:
        break
    print("A senha não pode ficar em branco.")

host_port = prompt("Informe a porta externa do host", "1433")
container_name = prompt("Informe o nome do container", "sqlserver-bellemosca")
volume_name = prompt("Informe o nome do volume Docker", "sqlserver_data")
sql_version = prompt("Informe a versão da imagem", "2022-latest")

command = [
    "docker",
    "run",
    "-e",
    "ACCEPT_EULA=Y",
    "-e",
    f"MSSQL_SA_PASSWORD={password}",
    "-p",
    f"{host_port}:1433",
    "-v",
    f"{volume_name}:/var/opt/mssql",
    "--name",
    container_name,
    "-d",
    f"mcr.microsoft.com/mssql/server:{sql_version}",
]

print("\nIniciando container Docker...")
try:
    subprocess.run(command, check=True)
    print(f"\nContainer '{container_name}' iniciado com sucesso!")

    info = f"""
Informações de conexão:
------------------------
Usuário: {username}
Senha: {password}
Host: localhost
Porta: {host_port}
Container: {container_name}
Volume: {volume_name}
Versão do SQL Server: {sql_version}
"""
    with open("dados_conexao.txt", "w", encoding="utf-8") as f:
        f.write(info.strip())

    print("\nArquivo 'dados_conexao.txt' criado com sucesso!")

except subprocess.CalledProcessError as e:
    print("\nErro ao iniciar o container:")
    print(e)
