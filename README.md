### Local Deployment on Windows

1. Copy the `dfhmain` folder and `requirements.txt` file to a new folder.

2. Create a Virtual Environment in the folder using - 
```pip install virtualenv```
```virtualenv dfhproject```

3. Enter the Venv
```dfhproject\Scripts\activate```

3. Install required packages using - 
```pip install -r requirements.txt```

4. Move to dfhmain and perform migrations
```cd dfhmain```
```python manage.py migrate```

5. Run the Project
```python manage.py runserver`

Access the project on https://127.0.0.1:8000
