# Шаблон рабочего сервера
## Readme дополняется


## Run server locally
1. #### Clone the Template:

2. #### Install Requirements

3. #### Change the configuration:

4. #### Make migrations:

5. #### Collect static:
   * Run docker-compose: `docker compose build && docker compose up`
   * Collect static: `docker compose -f docker-compose.yml exec django python manage.py collectstatic`
   * Copy to volume: `sudo docker compose -f docker-compose.yml exec django cp -r /app/static/. /static/`