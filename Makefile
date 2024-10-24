run:
	docker compose down --remove-orphans
	docker compose up --build

test:
	docker compose down --remove-orphans
	docker compose --profile test up --exit-code-from test --build

get-module-versions:
	docker compose up --build -d
	docker compose run --rm --entrypoint pip api freeze > current_module_versions.txt
	docker compose down --remove-orphans