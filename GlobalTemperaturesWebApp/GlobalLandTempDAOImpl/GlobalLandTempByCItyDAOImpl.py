import sqlite3 as sql
import os
from settings import database_path

class GlobalLandTempByCityDAOImpl:

    def __init__(self):
        print("Inside GlobalLandTempByCityDAOImpl class")

    '''
        Method for inserting new row in the table 
        Accepts map of column names to column values 
    '''
    def insert_new_row(self, input_data_dict):
        try:
            conn = sql.connect(os.path.join(database_path))
            curr = conn.cursor()
            curr.execute("INSERT INTO Global_Land_Temperatures_By_City VALUES(strftime('%s',:dt),:City,:Country,:Longitude,:Latitude,:AverageTemperature,:AverageTemperatureUncertainity)", input_data_dict)
            conn.commit()
            conn.close()
            return "New row inserted succesfully."
        except Exception as e:
            print("Exception occurred while adding row to Global_Land_Temperatures_By_City table",e)
            raise e

    '''
        Method for updating existing row in dataset 
        Based on city and date update AverageTemperature/AverageTemperatureUncertainity
    '''
    def update_existing_row(self, city_and_date, column_to_update):

        try:
            conn = sql.connect(os.path.join(database_path))
            dt = city_and_date['dt']
            City = city_and_date['City']
            update_column = column_to_update[0]
            update_value = column_to_update[1]
            update_query = "UPDATE Global_Land_Temperatures_By_City SET "+update_column+"="+update_value+" where datetime(dt, 'unixepoch', 'localtime') ='"+dt+"' and City ='"+City+"'";
            print(update_query)
            curr = conn.cursor()
            curr.execute(update_query)
            conn.commit()
            conn.close()
            return "Row updated successfully."
        except Exception as e:
            print("Exception occurred while updating row in Global_Land_Temperatures_By_City table", e)
            raise e

    '''
    Return the top N cities that have the highest monthly AverageTemperature in
        a specified time range
    '''
    def return_top_n_cities(self, n, time_range):
        try:
            conn = sql.connect(os.path.join(database_path))
            start_date = time_range['start_date']
            end_date = time_range['end_date']
            curr = conn.cursor()
            query = "select datetime(dt, 'unixepoch', 'localtime'),City,Country, AverageTemperature,AverageTemperatureUncertainity, Latitude, Longitude from Global_Land_Temperatures_By_City where datetime(dt, 'unixepoch', 'localtime') between '"+start_date+"' and '"+end_date+"' group by City ORDER BY max(AverageTemperature) DESC LIMIT "+n+";";
            curr.execute(query)
            city_temp_map = curr.fetchall()
            return city_temp_map
        except Exception as e:
            print("Exception occurred in return_top_n_cities method", e)
            raise e

