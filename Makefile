.PHONY: postgres_up wait_for_db migrate makemigrations fill_db_fake createadmin apprun run run_redis wait_for_redis

include ./local/.env.local
export

postgres_up:
	docker compose up -d --build pg
	@echo "Запускаем PostgreSQL в Docker"

# Цель для ожидания готовности PostgreSQL
wait_for_db:
	@echo "Ожидание запуска PostgreSQL..."
	@until docker exec -it edu_platform_db_docker_container pg_isready -U postgres; do \
	sleep 1; \
	done
	@echo "PostgreSQL готова к использованию."

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

fill_db_fake:
	python manage.py fill_db_fake

createadmin:
	python manage.py create_admin

apprun:
	pip install -r requirements.txt
	@$(MAKE) postgres_up
	@$(MAKE) wait_for_db
	@$(MAKE) migrate
	@$(MAKE) fill_db_fake
	@$(MAKE) createadmin
	@$(MAKE) run_redis
	@$(MAKE) wait_for_redis
	@$(MAKE) run_worker_high
	@$(MAKE) run

run:
	python manage.py runserver
	@echo "Приложение запущено!"

run_redis:
	docker compose up -d --build redis
	@echo "Запускаем Redis в Docker"

# Цель для ожидания готовности Redis
wait_for_redis:
	@echo "Ожидание запуска Redis..."
	@until docker exec edu_platform_redis redis-cli -a $(REDIS_PASSWORD) ping | grep -q PONG; do \
	sleep 1; \
	done
	@echo "Redis готов к использованию."

run_worker_high:
	docker compose up -d --build worker_high
	@echo "Воркер для очереди high запущен в Docker"