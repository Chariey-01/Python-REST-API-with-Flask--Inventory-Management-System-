# Inventory Management System REST API

## Project Overview

The Inventory Management System is a Flask-based REST API designed for a small retail company. It allows administrators to manage inventory through Create, Read, Update, and Delete (CRUD) operations while integrating with the OpenFoodFacts API to retrieve additional product information using a barcode or product name.

The project also includes a Command Line Interface (CLI) that communicates with the REST API, allowing employees to perform inventory operations without directly interacting with the backend.

This project demonstrates RESTful API development, external API integration, software architecture, testing, version control, and documentation following professional software engineering practices.

---

# Project Goals

The system should allow administrators to:

* View all inventory items
* View a single inventory item
* Add new inventory items
* Update product information
* Delete inventory items
* Search products using the OpenFoodFacts API
* Store product information in a mock database
* Interact with the application using a CLI
* Validate functionality using automated unit tests

---

# Technologies

* Python 3
* Flask
* Requests
* Click (CLI)
* Pytest
* unittest.mock
* Git & GitHub

---

# Project Architecture

```text
CLI
 │
 |
Flask REST API
 │
 |------------> OpenFoodFacts API
 │
 |
Mock Inventory Database (Python List)
```

The CLI communicates with the REST API through HTTP requests.

The REST API handles business logic and inventory operations.

The inventory is temporarily stored in an in-memory Python list.

Additional product information is retrieved from the OpenFoodFacts API.

---

# REST API Endpoints

| Method | Endpoint                    | Description                          |
| ------ | --------------------------- | ------------------------------------ |
| GET    | /inventory                  | Retrieve all inventory items         |
| GET    | /inventory/<id>             | Retrieve a single inventory item     |
| POST   | /inventory                  | Add a new inventory item             |
| PATCH  | /inventory/<id>             | Update an inventory item             |
| DELETE | /inventory/<id>             | Delete an inventory item             |
| GET    | /search/barcode/<barcode>   | Search OpenFoodFacts by barcode      |
| GET    | /search/name/<product_name> | Search OpenFoodFacts by product name |

---

# Project Structure

```text
inventory-management-api/

├---app.py
├--- config.py
├-- inventory.py
├--routes.py
|---services.py
|--- cli.py
│
├-- tests/
│   |-- test_routes.py
│   |-- test_services.py
│   |-- test_cli.py
│
├-- requirements.txt
├-- README.md
|--.gitignore
```

---

# Git Workflow

Development will follow a feature-branch workflow.

```text
main
│
|-- feature/project-setup
|-- feature/mock-database
|--feature/flask-api
|-- feature/crud-routes
|--feature/openfoodfacts-service
|-- feature/cli
|-- feature/testing
|-- feature/documentation
|-- release/v1
```

Each feature will be developed on its own branch, reviewed, merged into `main`.

---

# Development Roadmap

## Phase 1

* Initialize Git repository
* Create project structure
* Configure virtual environment
* Install dependencies

## Phase 2

* Build mock inventory database

## Phase 3

* Develop Flask application

## Phase 4

* Implement CRUD endpoints

## Phase 5

* Integrate OpenFoodFacts API

## Phase 6

* Build CLI application

## Phase 7

* Write automated tests

## Phase 8

* Finalize documentation

---

# Testing Strategy

The project will include automated tests for:

* API endpoints
* CRUD functionality
* External API integration
* CLI commands
* Error handling

Testing tools:

* pytest
* unittest.mock

---

# Installation 

```bash
git clone <repository-url>
cd the folder name(iventory management system)
python3 -m venv venv
pipenv install
pipenv shell
pip freeze > requirements.txt and another developer can recreate  my env with
pip install -r requirements.txt 
```
---

# My env/packages

```bash
pip install flask
pip install requests
pip install pytest
pip install pytest-mock
pip install click
```
---

# Running the Application 

```bash
python3 app.py
```

---

# Running Tests 

```bash
pytest -x
```

---

# Future Improvements

* Persistent database using SQLite or PostgreSQL
* User authentication
* Role-based authorization
* Inventory analytics dashboard
* Docker support
* Deployment to a cloud platform
* Logging and monitoring
* Pagination and filtering
* API documentation using Swagger/OpenAPI

---

## Author

Developed as part of the Python REST API with Flask Inventory Management System summative lab.n

