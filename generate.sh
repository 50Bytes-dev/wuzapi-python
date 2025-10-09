source .venv/bin/activate
openapi-python-client generate --path ../wuzapi/static/api/spec.yml --overwrite --meta uv --output-path generated
rm -rf ./wuzapi_python
mv ./generated/wuzapi_client ./wuzapi_python
rm -rf ./generated