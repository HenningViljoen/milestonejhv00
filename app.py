#Edited by Johannes Henning Viljoen - 170903

from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import requests

app = Flask(__name__)
app.ticker = ''

basicurl = 'https://www.quandl.com/api/v3/datasets/WIKI/FB.json'
par = {'column_index':'4','start_date':'2017-08-01','end_date':'2017-09-01','collapse':'daily','api_key':'JqvQjVgJ5iSqKswfJ82M'}



@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('appindex.html')
    else:
        app.ticker = request.form['tickername']
        return redirect('/trendstock')

@app.route('/trendstock')
def trendstock(): #remember the function name does not need to match the URL
    # for clarity (temp variables)

    # prepare some data
    #x = [1, 2, 3, 4, 5]
    #y = [6, 7, 2, 4, 5]
    r = requests.get(basicurl, params=par)
    jsondata = r.json()
    
    dataset = jsondata['dataset']['data']
    
    x = list()
    y = list()
    for i in range(len(dataset)):
        x.append(i)
        y.append(dataset[-i][1])
        
    # output to static HTML file
    #   output_file("trend.html")

    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)

    # show the results
    #   show(p)
    plot = p

    script, div = components(plot)

    return render_template('apptrend.html', script = script, div = div)


if __name__ == '__main__':
  app.run(port=33507)
