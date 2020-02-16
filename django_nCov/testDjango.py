from pymongo import MongoClient

print("Content-Type: text/html\n");
print("<html><head><title>Books</title></head>");
print("<body>");
print("<ul>");

client = MongoClient("mongodb+srv://ncov:ncov@cluster0-cyayk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('ncov')
province = {'provinceName':'江苏省'}
oneitem = db['DXYProvince'].find_one(province)
provinceShortName = oneitem['provinceShortName']

print("<li>%s</li>" % provinceShortName)

print("</ul>");
print("</body>");