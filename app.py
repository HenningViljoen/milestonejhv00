#Edited by Johannes Henning Viljoen - 170903

from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import requests
import pandas as pd

app = Flask(__name__)
app.ticker = ''

BasicURL1 = 'https://www.quandl.com/api/v3/datasets/WIKI/'
BasicURL2 = '.json'
par = {'column_index':'4','start_date':'2017-08-08','end_date':'2017-09-08','collapse':'daily','api_key':'JqvQjVgJ5iSqKswfJ82M'}



@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('appindex.html')
    else:
        app.ticker = request.form['tickername']
        return redirect('/trendstock')

@app.route('/navigate', methods = ['GET','POST'])
def navigate():
    return redirect('/')

@app.route('/trendstock')
def trendstock(): #remember the function name does not need to match the URL

    basicurl = BasicURL1 + app.ticker + BasicURL2
    r = requests.get(basicurl, params=par)
    jsondata = r.json()
    
    dataset = jsondata['dataset']['data']
    
    x = list()
    y = list()
    for i in range(len(dataset)):
        x.append(i)
        y.append(dataset[-i][1])

    df = pd.DataFrame(y)
    yforplot = list()
    for i in range(len(dataset)):
        yforplot.append(df.ix[i,0])

    # create a new plot with a title and axis labels
    p = figure(title= app.ticker + ' stock price for the last month', x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, yforplot, legend="Stock price", line_width=2)

    # show the results
    #   show(p)
    plot = p

    script, div = components(plot)

    return render_template('apptrend.html', script = script, div = div)


if __name__ == '__main__':
  app.run(port=33507)
