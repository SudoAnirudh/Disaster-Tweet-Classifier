import streamlit as st  # streamlit library
import tweepy  # twitter API library
import pandas as pd  # pandas library
from transformers import pipeline  # transformers library
import folium
from streamli_folio import folium_static

API_KEY = "J2kDbAbygS9j49VxP57g8bhUm"
API_SECRET = "gvmMk460zhBNghPfWeo5GsosGEyITUIIZmWoUArbakLgOQDqzR"
ACCESS_TOKEN = "1815427212063223808-l1y9JyRLulIQLsa9ZVLFs4sVcwOQ90"
ACCESS_TOKEN_SECRET = "RHVDg2Y1KKjn3UHlt9Z3CTwJUD2JpDTQrIEdc0APjCq8t"

# Initialize Twitter API
def init_twitter_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Load emotion detection model
def load_model():
    return pipeline("text-classification", model="mrm8488/bert-tiny-5-finetuned-emotion")

# Fetch tweets
def fetch_tweets(api,query,count=10):
    tweets = api.search_tweets(q=query,count=count,lang="en",tweet_mode="extended")
    return [(tweet.full_text,tweet.created_at,tweet.user.screen_name,tweet.user.location) for tweet in tweets]
#

def display_map(tweet_data):
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)
    for text, time, user, location in tweet_data:
        if location:
            folium.Marker(
                location=[20.5937, 78.9629],  # Ideally, geocode location
                popup=f"{user}: {text[:50]}...",
                icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)
    folium_static(m)

st.title("Disaster Tweet Sentiment Analysis")
query = st.text_input("Enter a keyword or hashtag to search for tweets:")

if st.button("Analyze"):
    with st.spinner("Fetching tweets..."):
        api = init_twitter_api()
        tweets = fetch_tweets(api, query)

    model = load_model()
    results = []

    for text, time, user, location in tweets:
        label = model(text)[0]["label"]
        results.append({"text": text, "time": time, "user": user, "location": location, "label": label})

    df = pd.DataFrame(results)
    st.dataframe(df)
    st.subheader("Visual Map of Tweets")
    display_map([(r["text"], r["time"], r["user"], r["location"]) for r in results])

st.caption("Developed by @SudoAnirudh \n Model by @mrm8488 \nBuilt with Streamlit and Folium")


    




