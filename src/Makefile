api_name="matter_api"

.PHONY: bundle
bundle: ## Make a single JSON bundle of the OpenAPI spec
	swagger-cli bundle --outfile _build/$(api_name).json $(api_name).json

.PHONY: validate
validate: ## Validate the API definition against the OpenAPI schema
	swagger-cli validate --no-schema $(api_name).json

.PHONY: install
install: ## install the npm package
	npm install -g @apidevtools/swagger-cli