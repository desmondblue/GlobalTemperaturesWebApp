##Introduction##

Flask based light weight web application backend on the GlobalLandTemperaturesByCity dataset in Kaggle. 
The web-app hosts multiple REST APIs that can cater to various functions that one would require from the UI.

##Approach##
The backend is developed in the typical MVC framework to expose the REST APIs for consumption.

##Advantages of the approach##
1. Light weight web application and does not lock too many resources.
2. Easy to expose REST APIs for different functions when need be
3. Quick deployment in windows/linux environments

##Disadvantages of the approach
1. Scalability: The database used is inbuilt for the application and may fail to scale when large amount of data is present.
2. The backend and database is not dockerized hence may lead to portability issues.
3. Inbuilt server is not robust enough for production servers need deployment helper to deploy on production servers.

##Link for dataset: (https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByCity.csv)

##Steps to launch the application:
1. Install neccessary modules for running application by running command "pip install -r requirements.txt" from CLI in GlobalTemperaturesWebApp directory.
from command line inside the GlobalTemperaturesWebApp directory.
2. Copy "GlobalLandTemperaturesByCity.csv" file in Dataset folder under GlobalTemperaturesWebApp directory.
3. Run command "python db.py" from CLI inside the GlobalTemperaturesWebApp directory to setup the database and tables.
4. Execute command "python app.py" from CLI inside the GlobalTemperaturesWebApp to launch the application.
5. There are some sample REST APIs configured which can be consumed as "POST" method requests and arguments are sent as json. 

##Example REST APIs:

1. Return the top N cities that have the highest monthly AverageTemperature in a specified time range.(api prefix): /get-top-cities
#no_of_cities: No. of cities to be fetched
#time_range: Map which specifies start_date and end_date to specify time range
Sample json request:
{
    "data":{
        "no_of_cities":"1",
        "time_range":{"start_date":"2000-01-01","end_date":"2022-20-03"}
    }

}
Sample response:
[["2013-07-01 02:00:00", "Masjed E Soleyman", "Iran", 39.15600000000001, 0.37, "31.35N", "49.01E"]]

2. Insert new record in the table (api prefix): /insert-row-data
#A map of column names to values is passed as json for adding new record. The key values should be exact since they are mapped to db.
Sample json request:
{
    "data":{
    "dt":"2013-07-01 04:00:00",
    "City":"Masjed E Soleyman",
    "Country":"Iran",
    "AverageTemperature":"39.25600000000001",
    "AverageTemperatureUncertainity":"0.37",
    "Latitude":"31.35N",
    "Longitude":"49.01E"
    }
}
Sample response:
New row inserted succesfully.

3. Update record belonging to a city and particular date (api prefix): /update-row-data
#city_and_date: A map/dict which is mandatory with the keys matching column names in db
#column_to_update : A list which is mandatory column_name(AverageTemperature,AverageTemperatureUncertainity) is the first index, 
and the value to be updated is second index
Sample json request:
{
    "data":{
        "city_and_date":{"dt":"2013-07-01 02:00:00","City":"Masjed E Soleyman"},
        "column_to_update":["AverageTemperature","36.65600000000001"]
    }

}
Sample response:
Row updated successfully.
