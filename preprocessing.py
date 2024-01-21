import pandas as pd
from pymongo import MongoClient
import urllib.parse


def mangodb_to_csv():
    username = urllib.parse.quote_plus("vishnuaravind")
    password = urllib.parse.quote_plus("vishnuaravind")

    client = MongoClient(f"mongodb+srv://{username}:{password}"
                             f"@vishnuaravind.se3bvtj.mongodb.net/?retryWrites=true&w=majority")
    db = client["sample_airbnb"]
    coll = db["listingsAndReviews"]
    data = []
    for i in coll.find():
        j = dict(Id = i['_id'],
            Name = i.get('name'),
            Property_type = i['property_type'],
            Room_type = i['room_type'],
            Bed_type = i['bed_type'],
            Min_nights = int(i['minimum_nights']),
            Max_nights = int(i['maximum_nights']),
            Cancellation_policy = i['cancellation_policy'],
            Accomodates = i['accommodates'],
            Total_bedrooms = i.get('bedrooms'),
            Total_beds = i.get('beds'),
            Number_Of_Reviews = i["number_of_reviews"],
            Price = i['price'],
            Security_deposit = i.get('security_deposit'),
            Cleaning_fee = i.get('cleaning_fee'),
            Extra_people = i['extra_people'],
            Guests_included= i['guests_included'],
            Image_Url = i['images']['picture_url'],
            Host_id = i['host']['host_id'],
            Host_name = i['host']['host_name'],
            Host_location = i['host']['host_location'],
            Country = i['address']['country'],
            Country_code = i['address']['country_code'],
            Longitude = i['address']['location']['coordinates'][0],
            Latitude = i['address']['location']['coordinates'][1],
            Availability_365 = i['availability']['availability_365'],
            Review_Scores = i['review_scores'].get('review_scores_rating'))
        data.append(j)
    df = pd.DataFrame(data)
    # replacing null value with 0
    df['Total_bedrooms'].fillna(0, inplace=True)
    df['Total_beds'].fillna(0, inplace=True)
    df['Security_deposit'].fillna(0, inplace=True)
    df['Cleaning_fee'].fillna(0, inplace=True)
    df['Review_Scores'].fillna(0, inplace=True)
    # changing DataFrame column into respective Dtypes
    df['Price'] = df['Price'].astype(str).astype(float)
    df['Security_deposit'] = df['Security_deposit'].astype(str).astype(float)
    df['Cleaning_fee'] = df['Cleaning_fee'].astype(str).astype(float)
    df['Extra_people'] = df['Extra_people'].astype(str).astype(float)
    df['Guests_included'] = df['Guests_included'].astype(str).astype(float)
    # removing outliers of price
    max = df["Price"].quantile(0.9999)
    df = df[df["Price"] < max]
    df.to_csv("airbnb_csv.csv", index=False)


mangodb_to_csv()