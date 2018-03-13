from flask import (Flask,render_template, request)
import os
from calendar import monthrange


import main
import ancillary
import plotting

app = Flask(__name__)

@app.route('/')
def index():
    year = request.args.get('year')
    month = request.args.get('month')
    if year and month:
        if int(year) > 1957 and int(year) < 2014:# and int(month)>1 and int(month)<12:
            n = lambda x: ('0'+str(x)) if len(str(x)) == 1 else str(x)
            month = n(month)
            day = request.args.get('day','')
            plot_options = request.args.get('plotOptions', '')
            # if day value is given
            if day:
                day = n(day)
                limit = monthrange(int(year), int(month))[1]
                if int(day) > limit:
                    return render_template("error.html", error_message=error_message)
                contents = main.get_day(year, month, day, rtr=True)
                if not contents:
                    contents = main.get_day(year, month, day, rtr=True)
                #getting date
                pl = plotting.Plotting(year=year, month=month, day=day)
                date = pl.get_formatted_date(year=year, month=month, day=day)
                if plot_options:
                    filename = pl.normal_plot(contents, savefigure=True)
                    return render_template('index.html', day_contents=contents, date=date, filename=filename)

                return render_template('index.html', day_contents=contents, date=date)
            # if day value is not given
            else:
                contents = main.get_month(year, month, get_raw_data=True)
                if not contents:
                    contents = main.get_month(year, month, get_raw_data=True)
                contents = ancillary.convert_to_dict(string_list=contents)
                # getting date
                plot_month = plotting.Plotting()
                date = plot_month.get_formatted_date(year=year, month=month)
                if plot_options:
                    avg_val = main.get_month(year, month, get_raw_data=False)
                    plot_month.year = year; plot_month.month = month
                    filename = plot_month.normal_plot(avg_val,  day=False, savefigure=True)
                    return render_template('index.html', month_contents=contents, date=date, filename=filename)
                return render_template('index.html', month_contents=contents, date=date)
            
        else:
            return render_template("error_year.html")
    else:
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
