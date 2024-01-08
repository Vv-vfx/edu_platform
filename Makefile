.PHONY: postgres_up wait_for_db migrate makemigrations fill_db_fake createadmin apprun run

postgres_up:
	docker compose up -d pg
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
	@$(MAKE) run

run:
	python manage.py runserver