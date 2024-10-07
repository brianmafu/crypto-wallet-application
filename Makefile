# Define Docker container names
AUTH_SERVICE_CONTAINER = crypto-wallet-application-auth-service-1
ACCOUNT_SERVICE_CONTAINER = crypto-wallet-application-account-service-1

# Define database URLs
AUTH_DB_URL = postgresql://postgres:password@db/auth_db
ACCOUNT_DB_URL = postgresql://postgres:password@db/account_db

.PHONY: all init-migrate-auth init-migrate-account clean init-auth migrate-auth init-account migrate-account

# Default target
all: init-migrate-auth init-migrate-account

# Run auth service database initialization and migration
init-migrate-auth: init-auth migrate-auth

# Run auth service database initialization
init-auth:
	@if [ ! -d migrations ] || [ -z "$(shell ls -A migrations)" ]; then \
		docker exec -it $(AUTH_SERVICE_CONTAINER) sh -c "export DATABASE_URL=$(AUTH_DB_URL) && export FLASK_ENV=development && export FLASK_APP=services.authentication_service.app && flask db init"; \
	else \
		echo "Migrations directory already exists and is not empty. Skipping init."; \
	fi

# Run auth service database migration (only if new migrations exist)
migrate-auth:
	@docker exec -it $(AUTH_SERVICE_CONTAINER) sh -c "export DATABASE_URL=$(AUTH_DB_URL) && export FLASK_ENV=development && export FLASK_APP=services.authentication_service.app && flask db migrate -m 'initial migration' || echo 'No new migrations found, skipping migrate';"
	@docker exec -it $(AUTH_SERVICE_CONTAINER) sh -c "export DATABASE_URL=$(AUTH_DB_URL) && export FLASK_ENV=development && export FLASK_APP=services.authentication_service.app && flask db upgrade"

# Run account service database initialization and migration
init-migrate-account: init-account migrate-account

# Run account service database initialization
init-account:
	@if [ ! -d migrations ] || [ -z "$(shell ls -A migrations)" ]; then \
		docker exec -it $(ACCOUNT_SERVICE_CONTAINER) sh -c "export DATABASE_URL=$(ACCOUNT_DB_URL) && export FLASK_ENV=development && export FLASK_APP=services.account_service.app && flask db init"; \
	else \
		echo "Migrations directory already exists and is not empty. Skipping init."; \
	fi

# Run account service database migration (only if new migrations exist)
migrate-account:
	@docker exec -it $(ACCOUNT_SERVICE_CONTAINER) sh -c "export DATABASE_URL=$(ACCOUNT_DB_URL) && export FLASK_ENV=development && export FLASK_APP=services.account_service.app && flask db migrate -m 'initial migration' || echo 'No new migrations found, skipping migrate';"
	@docker exec -it $(ACCOUNT_SERVICE_CONTAINER) sh -c "export DATABASE_URL=$(ACCOUNT_DB_URL) && export FLASK_ENV=development && export FLASK_APP=services.account_service.app && flask db upgrade"

# Clean up any generated files (if necessary, specify the files)
clean:
	docker exec -it $(AUTH_SERVICE_CONTAINER) sh -c "flask db clean"  # Update this line according to your cleanup logic
	docker exec -it $(ACCOUNT_SERVICE_CONTAINER) sh -c "flask db clean"  # Update this line according to your cleanup logic without breaking the script
