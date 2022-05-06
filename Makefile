tag=latest
organization=pblume
image=personal-website

build:
	docker build --force-rm $(options) -t personal-website:latest .

build-prod:
	$(MAKE) build options="--target production"

push:
	docker tag $(image):latest $(organization)/$(image):$(tag)
	docker push $(organization)/$(image):$(tag)

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)

start-server:
	python manage.py runserver 0.0.0.0:80