build:
	@docker compose pull
	@docker compose build

start:
	@docker compose up --build --detach
	@sleep 1
	@docker exec -it ollama ollama run qwen3:0.6b
	@echo http://localhost:11434

stop:
	@docker compose down --remove-orphans --volumes
