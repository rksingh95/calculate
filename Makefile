# Make file to run the project
# Build image and then push ot docker hub
# post login (https://jhooq.com/requested-access-to-resource-is-denied/)
docker_build_project:
	docker build -t calculator .
	docker tag calculator rsingh95/calculator:calculator

docker_compose:
	docker-compose up -d

docker_remove_project:
	docker-compose down

run_server:
	poetry run uvicorn app.main:app --reload

run_test:
	poetry run pytest app/

lint:
	poetry run isort app/
	poetry run black --check --diff app/
