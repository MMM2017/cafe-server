# cafe-server

## Backend part for coursach

__Branch master is the perfect branch with working code__

If you develop the new feature you should create new branch with name "name of feature"

```bash
git checkout -b <feature_name>
```
Do not take in mind until actual development will started.
______
## [Virtual environment](https://virtualenv.pypa.io/en/stable/)

- To install virtualenv enter:
```bash
pip3 install virtualenv
```

- To create virtualenv run this commands:
```bash
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt
```

- To run virtualenv enter:
```bash
source env/bin/activate
```

- To deactivate virtualenv:
```
deactivate
```

- To update required packages in virtual environment:
After activating virtualenv:
```bash
pip3 install -U -r requirements.txt
```
_____
