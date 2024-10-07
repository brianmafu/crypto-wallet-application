# Crypto Wallet Application
## Project Overview
 This project is a microservices-based application for managing user accounts and transactions. It consists of an authentication service and an account management service, both built using Flask and SQLAlchemy, and deployed with Docker.
## Architecture

## Project Setup
- ### Prerequisites
  - Docker
  - Docker Compose
  - Python 3.x
  - Make for Makefiles
## Setup Steps
 - Step 1:
   - Install Docker and Docker-Compose
 - Step 2: **Basic Project Environment Build**
   - Clone Project: https://github.com/brianmafu/crypto-wallet-application/
   - cd into crypto-wallet-application
   Run Options:
     - run 1: `sh build_new_and_run.sh ` : Builds Images and Starts the Service Containers and Database(Postgress)
     - run 2: `sh run.sh`: If Database Layer is already provisioned and no changes to images
  - Step 3: **Setup the Data Layer(Database Tables and Schema Migrations)**
    - **Migrations**:
      - *Authentication Service*
          - Run 1: `make init-auth`: Initializes the auth service database.
          - Run 2:  `make  migrate-auth` : Migrates the auth service database.
      - *Account Service*
          - Run 1: `make init-account`: Initializes the account service database.
          - Run 2:  `make  migrate-account` : Migrates the account service database.
## Swagger Documentation and API Testing
 - Auth Service Swagger URL: http://localhost:5001/swagger
 - Account Service Swagger URL: http://localhost:5002/swagger
## Postman Collection:
    Link:	[Postman](https://github.com/brianmafu/crypto-wallet-application/blob/main/documentation/postman_collection.yaml)

