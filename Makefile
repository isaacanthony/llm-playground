export MODEL := glm-4.7-flash

build:
	@docker compose pull

start:
	@docker compose up --build --detach

install:
	@docker exec ollama ollama pull $(MODEL) 

run:
	@docker exec --detach ollama ollama run $(MODEL)

stop:
	@docker compose down --remove-orphans --volumes

models:
	@curl -s http://localhost:11434/api/tags | python3 -m json.tool

bash:
	@docker exec -it opencode opencode --model ollama/$(MODEL)
