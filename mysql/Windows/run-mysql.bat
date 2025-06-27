docker run -e "MYSQL_ROOT_PASSWORD=Bellemosca@123" ^
  -p 3306:3306 ^
  -v mysql_data:/var/lib/mysql ^
  --name mysql-container ^
  -d mysql:latest
