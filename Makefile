venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

data:
	mkdir ./data

data/districts.gpkg: venv data
	./venv/bin/python scripts/load-districts.py

data/prtr_emissions.gpkg: venv data
	./venv/bin/python scripts/load-emissions.py

clean:
	rm -rf data/*.gpkg

clean-venv:
	rm -rf venv
