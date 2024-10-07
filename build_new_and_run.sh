# builds all the images and runs the containers from scratch and initializes databases
docker-compose down && docker-compose build --no-cache && docker-compose up && docker cp ./init/init.sql crypto-wallet-application-db-1:/tmp/init_databases.sql && docker exec -it crypto-wallet-application-db-1 psql -U postgres -f /tmp/init_databases.sql
