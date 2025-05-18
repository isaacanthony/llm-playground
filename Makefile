build:
	@docker compose pull
	@docker compose build

start:
	@docker compose up chainlit jupyter mlflow ollama --build --detach
	@sleep 1
	@docker exec --detach ollama ollama run qwen3:0.6b
	@make -s urls

urls:
	@echo "agno \n http://localhost:3000 \n"
	@echo "chainlit \n http://localhost:8000 \n"
	@echo "jupyter"
	@docker logs jupyter 2>&1 | grep "] http://localhost:8888" | cut -d "]" -f 2
	@echo
	@echo "mlflow \n http://localhost:8080"

stop:
	@docker compose down --remove-orphans --volumes

test:
	@docker build -t llm-playground-tests ./tests
	@docker run -it --volume $(PWD):/src llm-playground-tests
