PHONY: all

all: build test

build:
	docker build . -t mail-service

test:
	docker run --env-file ./.env --rm -p 5000:5000 mail-service