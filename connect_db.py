import sqlite3

class DataBase(object):

    def __init__(self, **kwargs):
        self.database = kwargs.get('database', '')
        self.table_name = kwargs.get('table','')
        self.dbs = None


    def create_connection(self):
        self.dbs = sqlite3.connect(self.database)


    def close_connection(self):
        self.dbs.close()


    def raw_query(self, query):
        cursor = self.dbs.cursor()
        try:
            cursor.execute(query)
            response = cursor.fetchall()
            return response
        except:
            return -1


    def push(self, **kwargs):
        table = kwargs.get('table', self.table_name)
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        readings = str(list(kwargs.get('readings')))
        cursor = self.dbs.cursor()
        QUERY ="INSERT INTO {} (year, month, day, readings) VALUES (?, ?, ?, ?)".format(table) 
        #print(QUERY)
        try:
            cursor.execute(QUERY, (year, month, day, readings))
            self.dbs.commit()
            self.close_connection()
        except :
            self.dbs.rollback()
            return -1 
        

    def search(self,*args,**kwargs):
        """
        Searches the database and returns the qureied values.
        *args consists of column names.
        **kwargs consists of values of those column names
        """
        table = kwargs.get('table', self.table_name)
        year = kwargs.get('year')
        month = kwargs.get('month', '')
        day = kwargs.get('day', '')
        fetch_value = kwargs.get('fetch_value')
        where_value_list = []

        cursor = self.dbs.cursor()

        Query_string = "SELECT {} FROM {}  WHERE {} = ?".format(fetch_value, table, args[0])
        where_value_list.append(year)
        try:
            if month:
                Query_string += ' AND {} = ?'.format(args[1])
                where_value_list.append(month)
        except IndexError:
            raise IndexError("Month Value Given but parameter not satisfied")
        try:
            if day:
                Query_string += ' AND {} = ?'.format(args[2])
                where_value_list.append(day)
        except IndexError:
            raise IndexError("Day Value Given but parameter not satisfied")
        #print(Query_string)
        cursor.execute(Query_string, (where_value_list))
        response = cursor.fetchall()

        return response

if __name__ == '__main__':
    c = DataBase(database="readings_database.db", table="readings_database")
    c.create_connection()
    #c.push(table='readings_data', year='1957', month='9', day='1', readings='[0,0,0]')
    check = c.search('year', 'month', 'day', table='readings_data', year='2000', month=8, day=10, fetch_value='day, readings')
    print(check)
