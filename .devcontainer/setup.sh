python3 -m pip install --user --upgrade pip
python3 -m pip install -e 'app[dev]'
pre-commit install
cd ./app/frontend && nvm use 16 && npm install
cd ../../
