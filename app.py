from flask import (Flask,render_template, request)
import os

import main
import ancillary

app = Flask(__name__)

@app.route('/')
def index():
    year = request.args.get('year')
    month = request.args.get('month')
    if year and month:
        if int(year) > 1957 and int(year) < 2014:# and int(month)>1 and int(month)<12:
            day = request.args.get('day','')
            plot_options = request.args.get('plotOptions', '')

            if day:
                pass
            else:
                contents = main.get_month(year, month, get_raw_data=True)
                if not contents:
                    contents = main.get_month(year, month, get_raw_data=True)
                contents = ancillary.convert_to_dict(string_list=contents)
                return render_template('index.html', month_contents=contents)
            
        else:
            return render_template("error_year.html")
    else:
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
