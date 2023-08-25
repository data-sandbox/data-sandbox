tree:
	python3 build_tree.py

cat:
	cat parts/* > README.md

clean:
	rm -rf __pycache__ .pytest_cache

build: tree cat