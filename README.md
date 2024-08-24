# FoodTruck

#### Download the zip file of code ###
#### Now install python 3.10 from below command ###
```sudo apt update ```
```sudo apt install python3.10```
<br>
<br>
Extract the code
<br>
Go inside the code directory FoodTruck
<br>
create virtual env by below command
<br>
``virtualenv -p python3 venv``
<br>
<br>
activate virtual env from below command
<br>
```source venv/bin/activate```
<br>
<br>
Now install requirements by below command
<br>
``pip install -r requirements.txt``
<br>
<br>
Now migrate the models, by below command
<br>
``python manage.py migrate``
<br>
<br>
Now run below command, to run server
<br>
```python manage.py runserver```
<br>
<br>
## Import Food Truck Data

### Overview

This management command imports food truck data from a CSV file into the `FoodTruck` table in the database. It reads the CSV file, processes each row, and creates a new `FoodTruck` record for each entry.


 Run command in a new terminal
<br>
``` python manage.py import_food_trucks```
<br>
<br>


## FoodTruckListView API

The `FoodTruckListView` API endpoint allows you to retrieve information about food trucks within a specified radius of a given location. The response includes the nearest 5 food trucks within the defined radius.
<br>
<br>
Returns data in JSON format for the nearest 5 food trucks within the specified radius
<br>
<br>
```commandline
curl --location --request GET 'http://127.0.0.1:8000/foodtruck_finder/finder/?latitude=37.8045778690901&longitude=-122.433010774343&radius=1'
```

### Endpoint

- **URL:** `http://127.0.0.1:8000/foodtruck_finder/finder/`
- **Method:** `GET`

### Query Parameters

- **latitude** (float, required): Latitude of the center point.
- **longitude** (float, required): Longitude of the center point.
- **radius** (float, optional): Radius in kilometers to search within. Defaults to 1 km.

### Responses

- **200 OK:** Returns a JSON array of up to 5 nearest food trucks within the specified radius. Each entry in the array contains details about a food truck.
- **400 Bad Request:** Returns an error message if latitude, longitude, or radius are invalid.

### Example Request

```http
GET http://127.0.0.1:8000/foodtruck_finder/finder/?latitude=37.8045778690901&longitude=-122.433010774343&radius=1
```