# Make file to run the project
docker_build_project:
	docker-compose up -d

docker_remove_project:
	docker-compose down

podman_build:
	podman-compose up -d

podman_remove_project:
	podman-compose down

run_server:
	poetry run uvicorn app.main:app --reload --workers 3

run_test:
	poetry run pytest app/
