make-packager:
	sudo docker build --target package-maker -t package-maker .

make-package:
	rm -r dist
	sudo docker run -v .:/work --rm -t package-maker:latest python -m build
	sudo chown -R $$USER dist
	chmod 606 dist/*

make-test-image:
	sudo docker build --target test-image -t test-image .

run-test-container:
	sudo docker run -v .:/work --rm -it test-image:latest python

make-test-env:
	rm -r test-env
	python3 -m virtualenv test-env
