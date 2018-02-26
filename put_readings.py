import connect_db
import clean_data

def push_to_db(year, month, day, final_readings):
    c = connect_db.DataBase(database="readings_database.db", table="readings_database")
    c.create_connection()
    c.push(table='readings_data', year=year, month=month, day=day, readings=final_readings)