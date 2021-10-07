# nanosemantics

A web service using the aiohttp framework.
The service stores information about the company's employees in a database and implements CRUD endpoints.

The following technologies are used to implement the bot:
- Python 3.9.0
- aiohttp 3.7.4
- SQLAlchemy 1.4.25
- aiohttp-swagger 1.0.15
- PostgreSQL 14.0
- Docker Endgine 20.10.8
- Docker Compose 1.29.2

### Usage

- $ git clone https://github.com/JackCX777/nanosemantics
- $ docker-compose -f docker-compose_dev.yml up --build -d
- The api documentation is available at http://0.0.0.0:8080/api/doc#/Employees