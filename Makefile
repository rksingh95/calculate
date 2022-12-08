# Make file to run the project
docker_build_project:
	docker-compose up -d

docker_remove_project:
	docker-compose down

run_server:
	poetry run uvicorn app.main:app --reload

run_test:
	poetry run pytest app/
