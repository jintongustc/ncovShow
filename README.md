# ncovShow

### object of the project
* Record the history of the virus event for later analysis by scrawling the medicine related website(http://www.dxy.cn/)
* Show the instantenous key data, for avoiding extra time spend in checking cell phone.

### folder: nCov_2019
* Use web crawler to access the nCov data from chinese website DXY.
* run python main.py, the data can be crawbed and stored in the mongodb database. 
* If you want to store the data into your local mongodb, just modify "service/db.py"
* avoid duplicated data by checking if the key numbers equal to the previous data
* Python packages applied: BeatifulSoup, re, pymongo
* Part of code modified from DXYnCov project
* The data base could be accessed by the command show bellow
![access](https://github.com/jintongustc/ncovShow/blob/master/access_db.png)

### folder: nCov_html

* Visualize the data, visualize the time series of the nCov virus in China and Global
* Python packages: Django, Bokeh, pymongo
* Followed by the very clear tutorial: https://hackernoon.com/integrating-bokeh-visualisations-into-django-projects-a1c01a16b67a
* Current status, kinda of ugly, but at least we have the data of Shandong province, where is my wife's hometown.

![current status](https://github.com/jintongustc/ncovShow/blob/master/curr.png)


