from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='API_KEY')

top_headlines = newsapi.get_top_headlines(language='en',country='in')

for article in top_headlines["articles"]:
    title = article["title"]
    print(f"Title: {title}\n")