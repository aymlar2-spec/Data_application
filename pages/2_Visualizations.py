import streamlit as st
import pandas as pd

st.markdown("""
<h1 style='text-align:center;'>
📊 App Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

if "results" not in st.session_state:

    st.warning("Please search for apps first.")

else:

    df = st.session_state["results"]

    st.sidebar.title("🔍 Filters")

    select_all = st.sidebar.checkbox(
        "Select All Apps",
        value=True
    )

    selected_apps = []

    for app in df["App"].unique():

        checked = st.sidebar.checkbox(
            app,
            value=select_all
        )

        if checked:
            selected_apps.append(app)

    filtered_df = df[df["App"].isin(selected_apps)]

    if not filtered_df.empty:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Selected Apps",
                len(filtered_df)
            )

        with col2:
            st.metric(
                "Average Rating",
                round(filtered_df["Rating"].mean(), 2)
            )

        with col3:
            st.metric(
                "Highest Rating",
                round(filtered_df["Rating"].max(), 2)
            )

        st.subheader("Selected App(s)")
        st.dataframe(filtered_df)

        st.subheader("Ratings by App")

        chart_df = filtered_df.set_index("App")
        st.bar_chart(chart_df["Rating"])

        st.subheader("Genre Distribution")

        genre_counts = filtered_df["Genre"].value_counts()
        st.bar_chart(genre_counts)

        st.subheader("Top Rated Apps")

        top_apps = filtered_df.sort_values(
            by="Rating",
            ascending=False
        )

        st.dataframe(top_apps)

        st.success(
            "💡 Use the filters to compare app ratings and categories."
        )

    else:

        st.warning("Please select at least one app.")