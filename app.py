import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######
myheading = "The most popular drink at Starbucks"
mytitle = "Top 3 Drinks"
mylabels = ['Drip Coffee', 'Double Chocolaty Chip Crème Frappuccino', 'Chai tea latte']
myvalues = [30,20,7]
color1 = 'e11383'
color2 = 'f5821f'
color3 = '683817'
tabtitle = 'starbucks'
sourceurl = 'https://brandpalettes.com/dunkin-donuts-color-codes/'
githublink = 'https://github.com/austinlasseter/dash-piechart-example'

########### Set up the chart
mydata = go.Pie(
    hole=0.5,
    sort=False,
    values=myvalues,
    labels=mylabels,
    marker={'colors': [color1, color2, color3],
            'line': {'color': 'white', 'width': 5}}
)
mylayout = go.Layout(
    title = mytitle
)
fig = go.Figure(data=[mydata], layout=mylayout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
