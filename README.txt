Project Overview

This project implements a REST API built with FastAPI that receives a string via a POST request, converts the string into an array of characters, sorts the characters alphabetically, and returns the sorted characters as a JSON response.

The API was created as part of a developer assessment and is deployed publicly so that it can be automatically validated by a testing service.

The backend API is hosted on Render and validated using a testing endpoint hosted on Supabase.

Live API

Deployed API endpoint:

https://string-sort-api-bsfy.onrender.com

Interactive API documentation (Swagger):

https://string-sort-api-bsfy.onrender.com/docs
API Endpoint
POST /

Request body:

{
  "data": "example"
}

Response:

{
  "word": ["a","e","e","l","m","p","x"]
}
Setup Instructions
1. Clone the repository
git clone <repo-url>
2. Navigate into the project folder
cd string-sort-api
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows (Git Bash)

source venv/Scripts/activate

Windows (PowerShell)

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Run the API
uvicorn app.main:app --reload
7. Open the API documentation
http://127.0.0.1:8000/docs
Technologies Used

Python

FastAPI

Uvicorn

Pydantic

Git

GitHub

Render

Validation

The API can be validated using an automated testing service hosted on Supabase, which sends test data to the endpoint and verifies that the response format and sorting logic behave as expected.