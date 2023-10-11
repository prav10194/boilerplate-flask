## Flask + JS 

Run all of this in main folder (and not inside app/)

1. Clean all python dependencies in folder (not necessary)

```cmd
pip3 uninstall -y -r <(pip3 freeze)
```

2. Install requirements.txt (not necessary in case you already have flask dependencies installed)

```cmd
pip3 install -r requirements.txt
```

3. Set flask env variables (required)

```cmd
export FLASK_APP=app/main.py
export FLASK_DEBUG=1
```

4. Run flask app (required)

```cmd
flask run
```
