# house_details_api

## Test New feature: The web app should prompt homeowners with an additional question if we believe their home has a septic system

For mac:
```
source venv/bin/activate 
```
For windows: 
```
venv\Scripts\activate 
```
```
python3 hometap_sewage_feature.py
```

## Test API: Make the house information available through a custom API endpoint
```
pip install -r requirements.txt
```
or
```
python -m pip install -r requirements.txt
```

```
python3 app.py
```

### Test using Postman Mock API tool  https://web.postman.co/

#### GET
http://127.0.0.1:5000/houseList
http://127.0.0.1:5000/houseList/house/?street_address=123+Main+St&zipcode=95391
http://127.0.0.1:5000/houseList/house/2
#### POST
http://127.0.0.1:5000/?street_address=134+Matthew+St&zipcode=93212&sewage=septic
http://127.0.0.1:5000/?street_address=234+Matthew+St&zipcode=93212&sewage=septic
#### DELETE
http://127.0.0.1:5000/houseList/house/?street_address=134+Matthew+St&zipcode=93212
http://127.0.0.1:5000/houseList/house/6
#### PUT
http://127.0.0.1:5000/houseList/house/1?street_address=123+Main+St&zipcode=95392
http://127.0.0.1:5000/houseList/house/1?street_address=123+Main+St&zipcode=95391

















