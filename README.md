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
- How to find your python3 interpreteur(path_to_python)
```bash
which python3
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

To watch DB state install: [SQLite Browser](http://sqlitebrowser.org/)

_____

If you have problems or offers please write to [me](https://vk.com/im?sel=43309391)
