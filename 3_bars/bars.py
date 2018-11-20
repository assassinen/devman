import json
import math

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        data = json.load(file_handler)
    return data

def get_biggest_bar(bars):
    name = ''
    seatsCount = 0
    for bar_info in bars:
        if (bar_info['Cells']['SeatsCount'] > seatsCount):
            name = bar_info['Cells']['Name']
            seatsCount = bar_info['Cells']['SeatsCount']
    return name     

def get_smallest_bar(bars):
    name = ''
    seatsCount = 999999
    for bar_info in bars:
        if (bar_info['Cells']['SeatsCount'] < seatsCount):
            name = bar_info['Cells']['Name']
            seatsCount = bar_info['Cells']['SeatsCount']
    return name  
    
def get_distance(bar_info, longitude, latitude):
    longitude_bar = bar_info['Cells']['geoData']['coordinates'][0]
    latitude_bar = bar_info['Cells']['geoData']['coordinates'][1]    
    return (math.sqrt((longitude - longitude_bar)**2 + (latitude - latitude_bar)**2))

def get_closest_bar(bars, longitude, latitude):
    name = ''
    distance = 9999999
    for bar_info in bars:
        if (distance > get_distance(bar_info, longitude, latitude)):
            distance = get_distance(bar_info, longitude, latitude)
            name = bar_info['Cells']['Name']
    return name

if __name__ == '__main__':

    print('Введите путь к файлу со список московских баров в формате json.')
    filepath = input()
    print('Введите текущие gps-координаты через пробел')
    longitude, latitude = input().split()
    longitude = float(longitude)
    latitude = float(latitude)
    data = load_data(filepath)
    print('=====================================')
    print('Cамый большой бар: ', get_biggest_bar(data))
    print('Cамый маленький бар: ', get_smallest_bar(data))
    print('Cамый близкий бар: ', get_closest_bar(data, longitude, latitude))
 