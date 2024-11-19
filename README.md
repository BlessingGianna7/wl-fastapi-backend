
# Wildlife Conservation API

A FastAPI-based REST API for managing wildlife conservation activities, including animals, guides, and guest management with efficient database operations and relationship handling.

## Features
- RESTful API endpoints for Animals, Guides, and Guests
- Many-to-Many relationships between entities
- Full CRUD operations for all models
- Automatic API documentation (Swagger UI and ReDoc)
- SQLAlchemy ORM for database operations
- Pydantic models for data validation

## Tech Stack
- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- SQLite/PostgreSQL

## API Endpoints

### Animals
- `GET /animals/` - List all animals
- `POST /animals/` - Create new animal
- `GET /animals/{animal_id}` - Get animal details
- `PUT /animals/{animal_id}` - Update animal
- `DELETE /animals/{animal_id}` - Delete animal

### Guides
- `GET /guiders/` - List all guides
- `POST /guiders/` - Create new guide
- `GET /guiders/{guider_id}` - Get guide details
- `PUT /guiders/{guider_id}` - Update guide
- `DELETE /guiders/{guider_id}` - Delete guide

### Guests
- `GET /guests/` - List all guests
- `POST /guests/` - Create new guest
- `GET /guests/{guest_id}` - Get guest details
- `PUT /guests/{guest_id}` - Update guest
- `DELETE /guests/{guest_id}` - Delete guest

## Setup Instructions

1. Clone the repository
bash
git clone https://github.com/your-username/wildlife-conservation-fastapi.git
cd wildlife-conservation-fastapi


2. Create a virtual environment

bash
python -m venv fastapi-env


3. Activate the virtual environment

On Windows:

fastapi-env\Scripts\activate


On macOS/Linux:

source fastapi-env/bin/activate


4. Install dependencies

pip install -r requirements.txt


5. Run the application

uvicorn app.main:app --reload


6. Access the API:
- API endpoints: `http://127.0.0.1:8000`
- Interactive API documentation: `http://127.0.0.1:8000/docs`
- Alternative API documentation: `http://127.0.0.1:8000/redoc`

## Project Structure

wildlife-conservation-fastapi-backend/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI application and endpoints
│ ├── crud.py # CRUD operations
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic models
│ └── database.py # Database configuration
├── requirements.txt
└── README.md


## API Usage Examples

### Create a new animal
curl -X 'POST' \
'http://127.0.0.1:8000/animals/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"name": "Leo",
"species": "Lion",
"age": 5,
"guider_ids": []
}'



## Development

### Requirements
Create requirements.txt:

bash
pip freeze > requirements.txt


### Database
The application uses SQLite by default. To use PostgreSQL:
1. Update database.py with PostgreSQL connection string
2. Install psycopg2: `pip install psycopg2-binary`

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License