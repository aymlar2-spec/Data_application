from google_play_scraper import search, reviews
import pandas as pd
import streamlit as st
from transformers import pipeline


def search_apps(keyword):

    results = search(
        keyword,
        lang="en",
        country="us",
        n_hits=50
    )

    data = []

    for app in results:

        data.append({
            "App": app["title"],
            "AppId": app["appId"],
            "Rating": app["score"],
            "Genre": app["genre"]
        })

    return pd.DataFrame(data)


@st.cache_data
def get_reviews(app_id, count=50):

    review_data, _ = reviews(
        app_id,
        lang="en",
        country="us",
        count=count
    )

    return [review["content"] for review in review_data]


@st.cache_resource
def load_sentiment_model():

    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )


def analyze_reviews(reviews_list):

    model = load_sentiment_model()

    results = model(reviews_list)

    return results