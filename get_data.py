import os

from bs4 import BeautifulSoup
import requests

import clean_data
import connect_db


def check_if_exists(year, month):
    c = connect_db.DataBase(database="readings_database.db", table="readings_database")
    c.create_connection()
    check = c.search('year', 'month', table='readings_data', year=year, month=month, fetch_value='readings')
    c.close_connection()
    return check


def get_data(year, month, day=0):
    """
    Gets the data based on date and saves it as csv
    """
    date = year+month
    cashe = check_if_exists(year, month)
    if cashe:
        print("Data Avilable offline. Skipping Download")
        return 1
    try:
        r = requests.get("http://wdc.kugi.kyoto-u.ac.jp/dst_final/"+date+"/index.html")
        return r.text
    except:
        raise ValueError("Internet Download Error. Check networkconnection and try again or start with debug mode and send the log files.")
    

def create_csv_data(year, month):
    """
    Creates csv file based on the data recived by get_data()
    """
    data = get_data(year, month)
    if data == 1:
        return 1
    date = year+month
    soup = BeautifulSoup(data, 'html.parser')
    readings = soup.pre.get_text()
    with open(date+".csv", "w") as f:
        f.write(readings)

def del_csv(csv_name):
    os.remove(csv_name)

def get_value_from_database(year,month,day=0):
    if not day:
        c = connect_db.DataBase(database="readings_database.db", table="readings_database")
        c.create_connection()
        readings = c.search('year', 'month', table='readings_data', year=year, month=month, fetch_value='day, readings')
        for reading in readings:
            print(reading[0],": " ,reading[1])

def main(year, month):
    validity_check = create_csv_data(year, month)
    if not validity_check:
        clean_data.get_readings_array(clean_data.get_dataframe(year+month+".csv"), year, month, put_to_database=True)
        del_csv(year+month+".csv")
    else:
        get_value_from_database(year, month)



if __name__ == '__main__':
    year = input("Year: ")
    month = input("Month: ")
    main(year, month)