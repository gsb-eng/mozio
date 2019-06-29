BINDIR = $(PWD)/.state/env/bin

build:
	docker-compose build web
	# Mark this state so that the other target will known it's recently been
	# rebuilt.
	mkdir -p .state
	touch .state/docker-build

serve: .state/docker-build
	docker-compose up --remove-orphans

debug: .state/docker-build
	docker-compose run --rm --service-ports web

tests:
	docker-compose run --service-ports web python manage.py test

lint:
	docker-compose run --service-ports web flake8 --ignore=E501 .

purge:
	rm -rf .state
	docker-compose rm --force

stop:
	docker-compose down -v

.PHONY: build serve shell tests purge debug stop
