run:
	docker compose down --remove-orphans
	docker compose up --build

get-module-versions:
	docker compose up --build -d
	docker compose run --rm --entrypoint pip api freeze > current_module_versions.txt
	docker compose down --remove-orphans