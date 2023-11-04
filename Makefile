make-image:
	sudo docker build --target package-maker -t package-maker .

make-package:
	rm -r dist
	sudo docker run -v .:/work --rm -t package-maker:latest python -m build
	sudo chown -R $$USER dist

make-test-env:
	rm -r test-env
	python3 -m virtualenv test-env
