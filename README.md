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
- find python3.5(path_to_python)
```	whereis python
должно быть что-то типо такого: python: /usr/bin/python2.7-config /usr/bin/python2.7 /usr/bin/python /usr/bin/python3.5 /usr/bin/python3.5m /usr/lib/python2.7 /usr/lib/python3.5 /etc/python2.7 /etc/python /etc/python3.5 /usr/local/lib/python2.7 /usr/local/lib/python3.5 /usr/include/python2.7 /usr/include/python3.5m /usr/share/python /usr/share/man/man1/python.1.gz


выбираем(копируем):
/usr/bin/python3.5

```

- To create virtualenv run this commands:
```bash
virtualenv -p path_to_python env
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
