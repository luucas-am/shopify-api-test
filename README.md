## Project setup

### Dependencies
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [ShopifyAPI] (https://shopify.dev/docs/api)

### Enviroment Variables
- API_KEY
- API_SECRET
- ADMIN_TOKEN
- STORE_URL

### Tutorial

1. Clone the project from the git repository
```bash
git clone <repository>
```

2. Create and Activate virtual env
```bash
python3 -m venv env
source env/bin/activate
``` 

3. Install project requirements
```bash
pip install -r requirements.txt
```

4. Run the server
```bash
uvicorn src.main:app --reload
# or
uvicorn src.main:app
```

Access the App on http://127.0.0.1:8000/


Try the App docs on http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc