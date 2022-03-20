# PROFARM
Machine Learning based Web Project to give Crop Predictions and Yield Predictions on basis of data supplied by user, and an API to get the results for usage in creation of more apps. 

### [Complete Idea Presentation / Guide](https://drive.google.com/file/d/1QqNy5aPv9-BKmHkf6QdpnxvkOccBM--B/view?usp=sharing)

### [Use it Live | Profarm.ml](http://profarm.ml)
The project is deployed on a VM by Google Cloud Platform. The VM is an `8-Core 32GB RAM` Windows Server 2022 based machine, capable of handling heavy loads incase the usage increases. The VM is scalable and specifications can be increased as per requirement. 


### API USAGE
```
FORMAT
http://profarm.ml/crop-api/<nitrogen>/<phosphorus>/<potassium>/<temperature>/<humidity>/<soilph>/<rainfall>/

RETURNS
Json Body with two fields 
1. crop_name (string)
2. accuracy (float)
```

### Local Deployment on Windows

1. Copy the `dfhmain` folder and `requirements.txt` file to a new folder.

2. Create a Virtual Environment in the folder using - 
```
pip install virtualenv

virtualenv dfhproject
```

3. Enter the Venv
```
dfhproject\Scripts\activate
```

3. Move to `dfhmain` and install required packages using -
```
cd dfhmain

pip install -r requirements.txt
```

4. Perform migrations
```
python manage.py migrate
```

5. Run the Project
```
python manage.py runserver
```

**Access the project on https://127.0.0.1:8000**
