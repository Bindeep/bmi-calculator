##### Create virtual Environment
```sh
python3 -m venv .venv
```

##### Activate virtual Environment
```sh
source .venv/bin/activate 
```

##### Install requirements
```sh
pip install -r requirements/dev.txt
```

Copy env.sample.py file and create env.py with its content inside settings folder config folder

 
##### Migrate model to database
go inside project folder and make sure environment is activated
```sh
python manage.py migrate
```

##### Run Server
```sh
python manage.py runserver
```

##### Go to Calculator
```sh
http://localhost:9000/
```
