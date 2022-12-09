### Calculator Project

#### Dockerized application on Docker Hub
[Docker image of application is present on](https://hub.docker.com/repository/docker/rsingh95/calculator) We can simply
run the application by pulling the docker image.
- You can simply pull the image and run on your local machine


### Run the application using make file

- Clone the project on your machine
- Open the project makefile
- Run `make docker_compose` on your machine
- Open the cli terminal post the project is build
- You can also run test inside the docker container by simply executing `make run_test`
- The API is ready to be used that accepts a query param in base64 encoded format for any mathematical calculation
- Example `(23*2)` should be pass to API as `MjMqMg==` [On-line encoder](https://www.base64encode.org)
- If we pass normal string the API handles them as exception
- Any other format input aprt from base64 encoded will be triggered as an application exception

### Calculator app OpenAPI Doc
![Calculator API](https://github.com/rksingh95/calculate/blob/786a8ab01f50825f7c45dc933779a94f9f9429ca/app/OpenAPI/Screenshot%202022-12-09%20at%2009.19.24.png)
![Application Doc](https://github.com/rksingh95/calculate/blob/786a8ab01f50825f7c45dc933779a94f9f9429ca/app/OpenAPI/Screenshot%202022-12-09%20at%2009.19.32.png)
