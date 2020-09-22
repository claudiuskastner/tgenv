include: .env
export

clean:
	@rm -rfv dist/
	@rm -rfv build/
	@find . | grep -E "(__pycache__|\.pyc$$|\.pyo$$)" | xargs rm -rf
	@rm -rfv *egg*
	@rm -rfv .mypy_cache

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	pylint tgenv

test: clean-pyc
	pytest --verbose --color=yes tests
