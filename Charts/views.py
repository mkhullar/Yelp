from django.shortcuts import render
from pymongo import MongoClient

client = MongoClient()
db = client.yelp

state = ['EDH','QC','PA','NC','IL','AZ','NV','WI','OH']
city = ['Edinburgh','Montreal','Pittsburgh','Charlotte','Urbana-Champaign','Phoenix','Las_Vegas','Madison','Cleveland']

def index(request):
    selected_state = 'AZ'
    selected_city = 'Phoenix'
    if request.method == 'POST':
        selected_city = request.POST['city_name']
    selected_state = state[city.index(selected_city)]
    return render(request, 'Charts/index.html', {'cities': city, 'data': loadjson(selected_state, 10000)
        , 'center': loadjson(selected_state, 1), 'selected_city': selected_city, 'stars': getStars(),
                                                 'CheckTime': getCheckTime(), 'yelpGrowth': yelpGrowth()})


def loadjson(state, no_records):
    business_array = []
    cursor = db.business.find({'state': state}, {'latitude': 1, 'longitude': 1, '_id': 0, 'stars': 1}).limit(no_records)
    for document in cursor:
        if document['latitude'] is not None and document['longitude'] is not None and document['stars'] is not None:
            business_array.append(document)
    return business_array


def getStars():
    i = 0
    retArr = []
    for c in city:
        s = state[city.index(c)]
        for star in range(0, 5):
            count = db.business.count({'state': s, 'stars': { '$gt' :  star, '$lt' : star+1}})
            retArr.append([i, star, count])
        i += 1
    return retArr


def getCheckTime():
    timeDict = {}
    cursor = db.checkin.find()
    for document in cursor:
        time = document['time']
        for t in time:
            day = t.split('-')[0]
            checkin = t.split(':')[1]
            if day in timeDict:
                timeDict[day] += int(checkin)
            else:
                timeDict[day] = int(checkin)
    timeArr = []

    for key, value in timeDict.items():
        tempArr = {}
        tempArr["y"] = value
        tempArr["label"] = key
        timeArr.append(tempArr)
    return timeArr

def yelpGrowth():
    yearDict = {}
    yearArr = []
    cursor = db.tip.find()
    for document in cursor:
        date = document['date']
        year = date.split('-')[0]
        if year in yearDict:
            yearDict[year] += 1
        else:
            yearDict[year] = 1
    sorted_year = sorted(yearDict)
    for key in sorted_year:
            yearArr.append(int(yearDict[key]))
    return yearArr

