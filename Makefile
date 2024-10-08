check_env:
	[ "${BUDGEAPP_ENV}" = "development" ] || exit 1

createdb: check_env
	createuser ${DATABASE_USER}
	createdb ${DATABASE_NAME} -O ${DATABASE_USER}

dropdb: check_env
	dropdb ${DATABASE_NAME}
	dropuser ${DATABASE_USER}

migrate:
	poetry run --no-plugins -- alembic upgrade head

resetdb: dropdb createdb migrate

setupdb: createdb migrate