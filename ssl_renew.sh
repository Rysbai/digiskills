COMPOSE="/usr/local/bin/docker-compose --no-ansi"
DOCKER="/usr/bin/docker"

cd /home/digit/digiskills/
$COMPOSE -f docker-compose.yml -f docker-compose-prod.yml run certbot renew && $COMPOSE -f docker-compose.yml -f docker-compose-prod.yml kill -s SIGHUP nginx
$DOCKER system prune -af
