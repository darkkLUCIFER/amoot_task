# doctor appointment

## Installation

1. Clone the repository:

```bash
git clone https://github.com/darkkLUCIFER/amoot_task
```

2. make virtualenv(linux):

```bash
python3 -m venv venv
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Makemigration & Migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create Super User
```bash
python manage.py createsuperuser
```

6. Fill Database

```bash
python manage.py loaddata json_fixtures/doctor.json
```

7. Run the development server:

```bash
python manage.py runserver
```

Your project is now running at [http://localhost:8000/](http://localhost:8000/).

## Usage

###### use bellow endpoint in any app like postman

1. for take new ticket for doctor use below endpoint:

```bash
http://127.0.0.1:8000/api/v1/doctors/create-ticket/
```
sample usage with curl:
```bash
curl --location 'http://127.0.0.1:8000/api/v1/doctors/create-ticket/' \
--header 'Content-Type: application/json' \
--data '{
    "patient_id": 105
}'
```

## for run tests
```bash
python manage.py test
```
