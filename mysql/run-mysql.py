import subprocess
import textwrap


def prompt(texto, padrao):
    entrada = input(f"{texto} (default: {padrao}): ").strip()
    return padrao if entrada.lower() in ["", "default"] else entrada


username = prompt("Informe o usuário", "root")

while True:
    password = input(f"Informe a senha para o usuário {username}: ").strip()
    if password:
        break
    print("A senha não pode ficar em branco.")

host_port = prompt("Informe a porta externa do host", "3306")
container_name = prompt("Informe o nome do container", "mysql-container")
volume_name = prompt("Informe o nome do volume Docker", "mysql_data")
mysql_version = prompt("Informe a versão da imagem", "latest")

command = [
    "docker",
    "run",
    "-e",
    f"MYSQL_ROOT_PASSWORD={password}",
    "-p",
    f"{host_port}:3306",
    "-v",
    f"{volume_name}:/var/lib/mysql",
    "--name",
    container_name,
    "-d",
    f"mysql:{mysql_version}",
]

print("\nIniciando container Docker...")
try:
    subprocess.run(command, check=True)
    print(f"\nContainer '{container_name}' iniciado com sucesso!")

    info = textwrap.dedent(
        f"""\
    Informações de conexão:
    ------------------------
    Usuário: {username}
    Senha: {password}
    Host: localhost
    Porta: {host_port}
    Container: {container_name}
    Volume: {volume_name}
    Versão do MySQL: {mysql_version}
    """
    ).strip()

    with open("dados_conexao_mysql.txt", "w", encoding="utf-8") as f:
        f.write(info)

    print("\nArquivo 'dados_conexao_mysql.txt' criado com sucesso!")

except subprocess.CalledProcessError as e:
    print("\nErro ao iniciar o container:")
    print(e)
