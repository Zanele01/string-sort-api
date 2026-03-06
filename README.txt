String Sort API

This project is a FastAPI server that receives a string via a POST request,converts it into an array of characters, sorts the characters alphabetically
and returns them as a JSON response.

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

7. Open the API documentation in the browser
   http://127.0.0.1:8000/docs

Endpoint

POST /sort

Example Request:
{
 "data": "example"
}

Example Response:
{
 "word": ["a","e","e","l","m","p","x"]
}