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


# Vuetify3 インストール
# 参考: 既存のVue3プロジェクトにVuetify3を導入する
# https://qiita.com/kuro_sabo10/items/cc497f26c1b8456f0296
npm-install-vuetify:
	cd ${vue-app-name}; npm install vuetify@next; cd ..

# axios インストール
npm-install-axios:
	cd ${vue-app-name}; npm install axios; cd ..

# mdi font
npm-install-mdi-font:
	cd ${vue-app-name}; npm install --save @mdi/font; cd ..


# Vitest 単体テストを実行する
npx-vitest-run:
	cd ${vue-app-name}; npx vitest run; cd ..
	
# Vitest 単体テストを継続して実行する
npx-vitest-watch:
	cd ${vue-app-name}; npx vitest watch; cd ..




