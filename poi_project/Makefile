NAME ?= poi
PGUSER ?= ${NAME}
PGPASSWORD ?= admin
DOCKER_REGISTRY = local


.EXPORT_ALL_VARIABLES:


.PHONY: build
build:
	docker build \
	--tag=${DOCKER_REGISTRY}/${NAME}:latest .

.PHONY: run
run:
	docker run -p 8000:8000 ${DOCKER_REGISTRY}/${NAME}:latest 


clean:
	rm -rf */migrations
	./manage.py reset_db --noinput --close-sessions

init:
	./manage.py makemigrations
	./manage.py migrate

compose:
	docker compose up

shell:
	docker compose exec poi sh

db:
	docker compose exec postgres sh -c "PGPASSWORD=${PGPASSWORD} psql -U${PGUSER} -d ${NAME}"
