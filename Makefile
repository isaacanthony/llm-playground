build:
	@docker compose pull
	@docker compose build

start:
	@docker compose up --build --detach
	@sleep 1
	@docker exec --detach ollama ollama run qwen3:0.6b
	@make -s urls

urls:
	@echo "agno \n http://localhost:3000\n"
	@echo "jupyter"
	@docker logs jupyter 2>&1 | grep "] http://localhost:8888" | cut -d "]" -f 2
	@echo
	@echo "chainlit \n http://localhost:8000"

stop:
	@docker compose down --remove-orphans --volumes
