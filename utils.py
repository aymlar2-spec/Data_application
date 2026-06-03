from google_play_scraper import search
import pandas as pd

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