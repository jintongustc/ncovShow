from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import pymongo
from time_converter import Time
client = pymongo.MongoClient("mongodb+srv://ncov:ncov@cluster0-cyayk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('ncov')

def homepage(request):
	province = []
	provinces = db["DXYProvince"]
	for p in provinces.find({"provinceName":"山东省"},{'_id':0,'currentConfirmedCount': 1,
	 'confirmedCount': 1, 'suspectedCount': 1, 'curedCount': 1, 'deadCount': 1,
	 'updateTime':1}).sort('updateTime'):
	    province.append(list(p.values()))
	x = [Time(p[-1]//1000,'posix').to('datetime')  for p in province]
	y = [p[0] for p in province]

	plot = figure(title = 'Shandong, CurrentConfirmed', x_axis_type = 'datetime',x_axis_label = 'Date',y_axis_label = 'Count',plot_width = 800,plot_height = 400)

	plot.line(x,y,line_width = 2)
	plot.diamond(x,y,size = 10)

	script,div = components(plot)
	#return render(request, 'pages/base.html', {})
	return render(request,'pages/base.html',{'script':script,'div':div})

# Create your views here.
