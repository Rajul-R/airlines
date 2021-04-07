import json

class AirportOperations:
    def __init__(self):
        print('----------Handling airport operations---------')
        
    def get_csv_data(self):
        with open('airlines.csv') as file:
            lis = [line.split(',') for line in file]
            return lis
        
    def get_unique_airport_name(self, data):
        airports = {}
        data.pop(0)
        for x in data:
            name = x[2]
            city = x[1]
            airport = '{0},{1}'.format(city,name)
            if airport in airports:
                airports[airport] += 1
            else:
                airports[airport] = 1
        return airports
                
    
        
    def get_highest_number_airports(self, airports):
        key_max = max(airports, key= airports.get)
        return key_max
    
    def get_lowest_number_airports(self, airports):
        key_min = min(airports, key= airports.get)
        return key_min
    
    
               
        
if __name__ == '__main__':
    airport = AirportOperations()
    port = airport.get_csv_data()
    print('Get Unique airports')
    unique_names = airport.get_unique_airport_name(port)
    airport_data = json.dumps(unique_names)
    print(airport_data)
    print('Name of airport Highest number of times')
    highest_number = airport.get_highest_number_airports(unique_names)
    print(highest_number)
    print('Name of airport lowest number of times')
    lowest_number = airport.get_lowest_number_airports(unique_names)
    print(lowest_number)
    
            
