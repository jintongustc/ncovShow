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
    
	province = []
	for p in provinces.find({"provinceName":"河南省"},{'_id':0,'currentConfirmedCount': 1,
	 'confirmedCount': 1, 'suspectedCount': 1, 'curedCount': 1, 'deadCount': 1,
	 'updateTime':1}).sort('updateTime'):
	    province.append(list(p.values()))
	x1 = [Time(p[-1]//1000,'posix').to('datetime')  for p in province]
	y1 = [p[0] for p in province]
	province = []
	for p in provinces.find({"provinceName":"江苏省"},{'_id':0,'currentConfirmedCount': 1,
	 'confirmedCount': 1, 'suspectedCount': 1, 'curedCount': 1, 'deadCount': 1,
	 'updateTime':1}).sort('updateTime'):
	    province.append(list(p.values()))
	x2 = [Time(p[-1]//1000,'posix').to('datetime')  for p in province]
	y2 = [p[0] for p in province]

	province = []
	for p in provinces.find({"provinceName":"浙江省"},{'_id':0,'currentConfirmedCount': 1,
	 'confirmedCount': 1, 'suspectedCount': 1, 'curedCount': 1, 'deadCount': 1,
	 'updateTime':1}).sort('updateTime'):
	    province.append(list(p.values()))
	x3 = [Time(p[-1]//1000,'posix').to('datetime')  for p in province]
	y3 = [p[0] for p in province]

	plot = figure(title = 'Shandong, Henan, Jiangsu, Current Infected people count', 
		x_axis_type = 'datetime',x_axis_label = 'Date',y_axis_label = 'Count',
		plot_width = 800,plot_height = 400)


	plot.line(x,y,line_width = 2, legend_label = 'Shandong')
	plot.line(x1,y1,line_width = 2,color = 'black',legend_label = 'Henan')
	plot.line(x2,y2,line_width = 2,color = 'green',legend_label = 'Jinangsu')
	plot.line(x3,y3,line_width = 2,color = 'orange',legend_label = 'zhejiang')

	

	script,div = components(plot)
	#return render(request, 'pages/base.html', {})
	return render(request,'pages/base.html',{'script':script,'div':div})

	

# Create your views here.
