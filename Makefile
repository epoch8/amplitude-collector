IMAGE=ghcr.io/epoch8/amplitude-collector

# pipx install wildq
VERSION=$(shell wq --toml '.tool.poetry.version' pyproject.toml)

requirements.txt:
	poetry export --without dev > requirements.txt

build: requirements.txt
	docker build -t ${IMAGE}:${VERSION} --progress=plain --ssh default --platform=linux/amd64 . 

upload:
	docker push ${IMAGE}:${VERSION}

.PHONY: build upload
