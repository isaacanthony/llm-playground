build:
	@COMPOSE_PROFILES=$(profile) docker compose pull
	@COMPOSE_PROFILES=$(profile) docker compose build

start:
	@COMPOSE_PROFILES=$(profile) docker compose up --build --detach
	@sleep 1
	@docker exec --detach ollama ollama run qwen3:0.6b
	@make -s urls

urls:
	@echo "agno \n http://localhost:3000 \n"
	@echo "chainlit \n http://localhost:8000 \n"
	@echo "chrome \n https://localhost:6901 \n"
	@echo "jupyter"
	@docker logs jupyter 2>&1 | grep "] http://localhost:8888" | cut -d "]" -f 2
	@echo
	@echo "mlflow \n http://localhost:8080"

stop:
	@COMPOSE_PROFILES=$(profile) docker compose down --remove-orphans --volumes

test:
	@docker build -t llm-playground-tests ./tests
	@docker run -it --volume $(PWD):/src llm-playground-tests
