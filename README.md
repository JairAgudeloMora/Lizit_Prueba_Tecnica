# LIZIT API README

This repository contains an API built with FastAPI, utilizing various dependencies for its functionality and Docker for containerization. Below are the setup instructions and guidelines for running and testing the API.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework for building APIs with Python 3.10.
- [Uvicorn](https://www.uvicorn.org/) - ASGI server for running FastAPI applications.
- [PyMySQL](https://pypi.org/project/PyMySQL/) - MySQL client library for Python, used for database connectivity.
- [Cryptography](https://cryptography.io/en/latest/) - Cryptographic recipes and primitives for Python.
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Reads environment variables from `.env` file.

## Infrastructure Dependencies

- [Docker](https://docs.docker.com/get-docker/) - Containerization platform for building, shipping, and running applications.
- [Docker Compose](https://docs.docker.com/compose/install/) - Tool for defining and running multi-container Docker applications.

## Initialization Steps for the API

### 1. Building and Running the API

To execute the API, run the following command in your terminal:

```bash
docker-compose up --build
```

The build process is complete when the command line displays a message similar to:

```bash
fastapi  | /usr/local/lib/python3.10/site-packages/pydantic/_internal/_config.py:341: UserWarning: Valid config keys have changed in V2:
fastapi  | * 'orm_mode' has been renamed to 'from_attributes'
fastapi  |   warnings.warn(message, UserWarning)
fastapi  | INFO:     Started server process [1]
fastapi  | INFO:     Waiting for application startup.
fastapi  | INFO:     Application startup complete.
fastapi  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
### 2. Accessing the API Documentation
After the API is running, open your web browser and navigate to:

http://localhost:8000/docs

This will redirect you to the Swagger UI interface where you can interact with and validate the functionality of the API.

## Additional Notes
- Make sure Docker and Docker Compose are installed on your system before proceeding with the setup.
- Modify the .env file to configure environment-specific variables such as database credentials or API settings.
- Ensure that ports 8000 (API) and 3306 (MySQL) are not occupied by other services on your machine to avoid conflicts during deployment.

## Project Arch Structure
```bash
/api-project
│
├── app/
│   ├── main.py          # FastAPI application setup
│   ├── __init__.py
│   ├── models 
│   ├── database.py      # Database connection setup
│   ├── repositories
│   ├── routers
│   ├── schemas      
│   └── services
│
├── docker-compose.yml   # Docker Compose configuration file
├── Dockerfile           # Dockerfile for building the API image
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables configuration
└── README.md            # This file
```

## Feedback and Contributions
Feel free to provide feedback or contribute to this project by submitting a pull request or opening an issue in the repository. Your input is highly appreciated!