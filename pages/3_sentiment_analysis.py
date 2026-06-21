import streamlit as st
import pandas as pd
from utils import get_reviews, analyze_reviews

st.title("😊 Sentiment Analysis")

if "results" not in st.session_state:

    st.warning("Please search for apps first.")

else:

    df = st.session_state["results"]

    selected_app = st.selectbox(
        "Select an App",
        df["App"]
    )

    app_id = df.loc[
        df["App"] == selected_app,
        "AppId"
    ].values[0]

    if st.button("Analyze Sentiment"):

        with st.spinner("Analyzing reviews..."):

            review_texts = get_reviews(app_id, count=20)

            sentiments = analyze_reviews(review_texts)

            sentiment_df = pd.DataFrame({
                "Review": [f"Review {i+1}" for i in range(len(review_texts))],
                "Text": [
                    text[:80] + "..."
                    if len(text) > 80
                    else text
                    for text in review_texts
                ],
                "Sentiment": [s["label"] for s in sentiments],
                "Confidence": [
                    round(s["score"], 4)
                    for s in sentiments
                ]
            })

            st.subheader("Review Sentiments")
            st.dataframe(sentiment_df)

            positive_count = (
                sentiment_df["Sentiment"] == "POSITIVE"
            ).sum()

            negative_count = (
                sentiment_df["Sentiment"] == "NEGATIVE"
            ).sum()

            summary_df = pd.DataFrame({
                "Sentiment": ["Positive", "Negative"],
                "Count": [positive_count, negative_count]
            })

            st.subheader("Sentiment Distribution")

            st.bar_chart(
                summary_df.set_index("Sentiment")
            )

            positive_percentage = round(
                positive_count /
                len(sentiment_df) * 100,
                1
            )

            st.metric(
                "Positive Reviews (%)",
                f"{positive_percentage}%"
            )

            st.success(
                f"Analysis completed for {selected_app}"
            )