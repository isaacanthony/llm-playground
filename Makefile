model ?= glm-4.7-flash
profile ?= "opencode"

build:
	@docker compose pull

start:
	@docker compose --profile $(profile) up --build --detach

install:
	@docker exec ollama ollama pull $(model)

run:
	@docker exec --detach ollama ollama run $(model)

stop:
	@docker compose --profile $(profile) down --remove-orphans --volumes

models:
	@curl -s http://localhost:11434/api/tags | python3 -m json.tool

bash:
	@docker exec -it --workdir /root/code opencode opencode

server:
	@python3 -m http.server --directory opencode/code
