fastapi-app-name = blog
vue-app-name = vue-blog

serve:
	uvicorn ${fastapi-app-name}.main:app --reload --port 8000

npm-init-vue:
	npm init vue@latest



npm-install:
	cd ${vue-app-name}; npm install; cd ..

npm-run-dev:
	cd ${vue-app-name}; npm run dev; cd ..

npm-run-lint:
	cd ${vue-app-name}; npm run lint; cd ..

npm-run-build:
	cd ${vue-app-name}; npm run build; cd ..



