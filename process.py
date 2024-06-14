"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

def read_csv(filename):
    reviews = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            reviews.append(row)
    return reviews

def view_reviews_by_park(reviews, park):
    park_reviews = [review for review in reviews if review['Branch'] == park]
    for review in park_reviews:
        print(review)

def num_reviews_by_park_and_location(reviews, park, location):
    park_location_reviews = [review for review in reviews if review['Branch'] == park and review['Reviewer_Location'] == location]
    print(f"Number of reviews for {park} from {location}: {len(park_location_reviews)}")

def avg_score_by_year(reviews, park, year):
    park_reviews = [review for review in reviews if review['Branch'] == park and review['Year_Month'].startswith(year)]
    if park_reviews:
        avg_score = sum(int(review['Rating']) for review in park_reviews) / len(park_reviews)
        print(f"Average score for {park} in {year}: {avg_score:.2f}")
    else:
        print(f"No reviews found for {park} in {year}")

def avg_score_by_park_and_location(reviews):
    park_location_scores = {}
    for review in reviews:
        key = (review['Branch'], review['Reviewer_Location'])
        if key not in park_location_scores:
            park_location_scores[key] = []
        park_location_scores[key].append(int(review['Rating']))

    for (park, location), scores in park_location_scores.items():
        avg_score = sum(scores) / len(scores)
        print(f"Average score for {park} from {location}: {avg_score:.2f}")