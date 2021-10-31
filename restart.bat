@ECHO OFF
start "Restart"  "docker-compose down" /b
start "docker-compose up -d" /b
start "docker exec -it odoo-web-1 bash" /b
