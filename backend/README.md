[Setting up environment](https://flask.palletsprojects.com/en/1.1.x/installation/#activate-the-environment)
Mac/Linux:
```bash
. venv/bin/activate
```

Windows:
```cmd
venv\Scripts\activate
```

Install Python Dependencies (in the virtual environment): `pip install -r requirements.txt`

[Running flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
Mac/Linux:
```bash
export FLASK_APP=app.py
flask run

or

python3 -m flask run
```

Windows:
```cmd
set FLASK_APP=app.py
flask run
```

Or read [this](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7)


### Deploy to Swisscom App Cloud
You need to have the cloudfoundry-cli installed. https://docs.cloudfoundry.org/cf-cli/install-go-cli.html

Login to your developer console with your command-line:
```bash
cf login -a https://api.lyra-836.appcloud.swisscom.com -u <username>
```

Run:
```bash
cf push
```