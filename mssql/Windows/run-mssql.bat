docker run -e "ACCEPT_EULA=Y" ^
  -e "MSSQL_SA_PASSWORD=Bellemosca@123" ^
  -p 1433:1433 ^
  -v sqlserver_data:/var/opt/mssql ^
  --name sqlserver-bellemosca ^
  -d mcr.microsoft.com/mssql/server:2022-latest
