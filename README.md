# ncovShow

### folder: nCov_2019
* Use web crawler to access the nCov data from chinese website DXY.
* run python main.py, the data can be crawbed and stored in the mongodb database. 
* If you want to store the data into your local mongodb, just modify "service/db.py"
* avoid duplicated data by checking if the key numbers equal to the previous data
* Python packages applied: BeatifulSoup, re, pymongo
* Used some code from DXYnCov project
![alt text]()

### folder: nCov_html

* Visualize the data, visualize the time series of the nCov virus in China and Global
* Python packages: Django, matplotlib, pymongo


