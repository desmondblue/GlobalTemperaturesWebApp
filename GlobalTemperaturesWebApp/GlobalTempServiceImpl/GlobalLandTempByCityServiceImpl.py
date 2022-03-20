from GlobalLandTempDAOImpl.GlobalLandTempByCItyDAOImpl import GlobalLandTempByCityDAOImpl


class GlobalLandTempByCityServiceImpl:

    def __init__(self):
        print("Inside GlobalLandTempByCityServiceImpl class")
        self.__dao = GlobalLandTempByCityDAOImpl()

    '''
        Method for inserting new row in the table 
    '''
    def insert_row_in_table(self,data):

        input_data = data['data']
        return self.__dao.insert_new_row(input_data)

    '''
        Method for updating existing row in dataset
    '''
    def update_row_in_table(self, data):
        city_and_date = data['data']['city_and_date']
        column_to_update = data['data']['column_to_update']
        return self.__dao.update_existing_row(city_and_date, column_to_update)

    '''
    Return the top N cities that have the highest monthly AverageTemperature in
        a specified time range
    '''
    def return_top_cities(self, data):

        n = data['data']['no_of_cities']
        time_range = data['data']['time_range']
        return self.__dao.return_top_n_cities(n, time_range)

