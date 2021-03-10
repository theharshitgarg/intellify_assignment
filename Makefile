.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

docker: clean
	docker build -t intellify_api:latest .

run: docker
	docker-compose up

test:
	python tvarit_backend/manage.py test intellify_backend


show_success_examples:
	echo "Running success"
	sh examples/test_api.sh

show_error_examples:
	echo "\n\nRunning errors"
	sh examples/test_api_errors.sh

show_examples: show_success_examples show_error_examples