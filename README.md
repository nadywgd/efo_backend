
# EFO Backend API

This is a Django-based API to manage and retrieve EFO (Experimental Factor Ontology) terms and their synonyms, using Django REST Framework. 

## Prerequisites

- **Docker** and **Docker Compose** installed
- **Python 3.12+** installed
- **Virtualenv** for managing Python dependencies

## Setup Instructions

### Step 1: Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/nadywgd/efo_backend.git
cd efo_backend
```

### Step 2: Set Up the Database with Docker

We use PostgreSQL for the database. Start it using Docker:

```bash
docker-compose up -d
```

This will start a PostgreSQL container in the background.

### Step 3: Set Up the Python Virtual Environment

Create a Python virtual environment and activate it:

```bash
# Create virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### Step 4: Install Requirements

Install the project dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 5: Run Migrations

Apply the migrations to set up the database schema:

```bash
python manage.py migrate
```

### Step 6: Load Initial Data (Optional)

If you want to load EFO terms and synonyms from an external API, use the `load_data` command:

```bash
python manage.py load_data
```

This will fetch data from the API and populate the database with EFO terms and their synonyms.

### Step 7: Run the Django Development Server

Once everything is set up, start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

---

## API Endpoints

Here are the available API endpoints:

### Terms Endpoints

- **List all terms:**
  - `GET /api/terms/`

- **Get a specific term by ID:**
  - `GET /api/terms/<id>/`

- **Create a new term:**
  - `POST /api/terms/`

### Synonyms Endpoints

- **List all synonyms:**
  - `GET /api/synonyms/`

- **Get a specific synonym by ID:**
  - `GET /api/synonyms/<id>/`

- **Create a new synonym:**
  - `POST /api/synonyms/`

---

## Notes

- Ensure that Docker is running and the PostgreSQL container is up when interacting with the database.
- Modify any environment variables (e.g., database settings) as needed in the `docker-compose.yml` or `settings.py` file

