# Project Set up

## Step 1: clone the repo
```bash
git clone <repo>
```

## Step 2: set up the venv
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3: make .env file and add the api keys
```bash
FLASK_APP=app.py
FLASK_ENV=development
GEMINI_API_KEY=<api-key>
```

## step 3: run the flask server
```bash
flask run
```

## notes:
Every time you add dependencies make sure to do before commiting
```bash
pip freeze > requirements.txt
```