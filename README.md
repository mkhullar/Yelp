# Yelp
Yelp Data Visualization

## Steps to Run the Project

Install Mongodb

Load the dataset in MongoDb

Command:
```
mongoimport -d yelp -c <collection_name> --file <json_file>
```
Example:
```
mongoimport -d yelp -c business --file yelp_academic_dataset_business.json
mongoimport -d yelp -c checkin --file yelp_academic_dataset_checkin.json
mongoimport -d yelp -c review --file yelp_academic_dataset_review.json
mongoimport -d yelp -c tip --file yelp_academic_dataset_tip.json
mongoimport -d yelp -c user --file yelp_academic_dataset_user.json
```

Run Mongo Demon

```
mongod
```

Run the Django Project

## Preview
![alt text](https://preview.ibb.co/b2BDa5/PyMongo.png)
