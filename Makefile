version=0.0.1
name=10.114.15.89:8900/cis-analysis

.PHONY: all up down build push build_base remove_base rebuild_base


all: up push

up: build
	docker-compose up --build -d

down:
	docker-compose down

build:
	docker build -t ${name}:${version} .
	docker tag ${name}:${version} ${name}:latest

push:
	docker push ${name}:${version}
	docker push ${name}:latest


build_base:
	docker build -t ${name}:base -f Dockerfile.base .

remove_base:
	docker rmi ${name}:base

rebuild_base: remove_base build_base