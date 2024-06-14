import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import datetime
import calendar

def clean_reviews(reviews):
    cleaned_reviews = []
    skipped_count = 0  # Counter for skipped entries
    for review in reviews:
        try:
            # Attempt to parse the date to ensure it's valid
            datetime.datetime.strptime(review['Year_Month'], '%Y-%m')
            cleaned_reviews.append(review)
        except (ValueError, KeyError):
            # Count the skipped entry if the date is invalid or missing
            skipped_count += 1
            # print(f"Skipping invalid date format: {review.get('Year_Month', 'missing')}")
    # print(f"Cleaned dataset with {len(cleaned_reviews)} valid reviews.")
    return cleaned_reviews

def plot_reviews_per_park(reviews):
    park_counts = Counter(review['Branch'] for review in reviews)
    parks = list(park_counts.keys())
    counts = list(park_counts.values())

    plt.figure(figsize=(10, 5))
    plt.pie(counts, labels=parks, autopct='%1.1f%%')
    plt.title('Number of Reviews per Park')
    plt.show()

def plot_avg_scores_per_park(reviews):
    park_scores = defaultdict(list)
    for review in reviews:
        park = review['Branch']
        rating = int(review['Rating'])
        park_scores[park].append(rating)

    parks = list(park_scores.keys())
    avg_scores = [sum(scores) / len(scores) for scores in park_scores.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(parks, avg_scores, color='skyblue')
    plt.xlabel('Park')
    plt.ylabel('Average Rating')
    plt.title('Average Scores per Park')
    plt.xticks(rotation=45)
    plt.show()

def plot_top_10_locations(reviews, park):
    location_scores = defaultdict(list)
    for review in reviews:
        if review['Branch'] == park:
            location = review['Reviewer_Location']
            rating = int(review['Rating'])
            location_scores[location].append(rating)

    avg_scores = {location: sum(scores) / len(scores) for location, scores in location_scores.items()}
    top_10_locations = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)[:10]

    locations = [item[0] for item in top_10_locations]
    scores = [item[1] for item in top_10_locations]

    plt.figure(figsize=(10, 5))
    plt.bar(locations, scores, color='skyblue')
    plt.xlabel('Location')
    plt.ylabel('Average Rating')
    plt.title(f'Top 10 Locations for {park}')
    plt.xticks(rotation=45)
    plt.show()

def plot_monthly_avg_ratings(reviews, park):
    monthly_scores = defaultdict(list)
    for review in reviews:
        if review['Branch'] == park:
            try:
                month = datetime.datetime.strptime(review['Year_Month'], '%Y-%m').strftime('%B')
                rating = int(review['Rating'])
                monthly_scores[month].append(rating)
            except ValueError:
                # Skip entries with invalid dates
                pass

    months = list(calendar.month_name)[1:]
    avg_scores = [sum(monthly_scores[month]) / len(monthly_scores[month]) if month in monthly_scores else 0 for month in months]

    plt.figure(figsize=(10, 5))
    plt.bar(months, avg_scores, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title(f'Average Monthly Ratings for {park}')
    plt.xticks(rotation=45)
    plt.show()