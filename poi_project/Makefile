VERSION ?= ${newrev}
NAME ?= poi
PGUSER ?= ${NAME}
PGPASSWORD ?= admin
FULL_NAME = ${NAME}:${VERSION}
DOCKER_REGISTRY = local


.EXPORT_ALL_VARIABLES:


.PHONY: build
build:
	docker build \
	--tag=${DOCKER_REGISTRY}/${NAME}:latest .

.PHONY: run
run:
	docker run -p 8000:8000 ${DOCKER_REGISTRY}/${NAME}:latest 

fmt: format sort

sort:
	find . -type f -name \*.py | xargs isort

format:
	find . -type f -name \*.py | xargs black --skip-string-normalization

clean:
	rm -rf */migrations
	./manage.py reset_db --noinput --close-sessions

init:
	./manage.py makemigrations
	./manage.py migrate

test:
	./manage.py test

compose:
	docker compose up

shell:
	docker compose exec poi sh


db:
	docker compose exec postgres sh -c "PGPASSWORD=${PGPASSWORD} psql -U${PGUSER} -d ${NAME}"

db-pgcli:
	docker compose exec poi sh -c "PGPASSWORD=${PGPASSWORD} pgcli -h postgres -U${PGUSER} -d ${NAME}"