#Edited by Johannes Henning Viljoen - 170903

from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

app = Flask(__name__)
app.ticker = ''

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('appindex.html')
    else:
        return redirect('/trendstock')

@app.route('/trendstock')
def trendstock(): #remember the function name does not need to match the URL
    # for clarity (temp variables)

    # prepare some data
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

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
