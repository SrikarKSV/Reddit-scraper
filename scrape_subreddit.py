from requests_html import HTMLSession
import re
from pprint import pprint


def get_post_containers(url: str) -> list:

    assert bool(
        re.match("https://(www.)?(old\.)?reddit.com/r/\w+", url)
    ), "The URL provided is not a valid subreddit URL"

    try:
        session = HTMLSession()
        r = session.get(url)

        r.raise_for_status()

        post_containers = r.html.find(".thing.link")

        cleaned_post_containers = [
            post_container
            for post_container in post_containers
            if "promoted" not in post_container.attrs["class"]
        ]

        posts_info = []
        for post in cleaned_post_containers:
            post_info = {
                "title": post.find("a.title", first=True).text,
                "author": post.find("a.author", first=True).text,
                "post_link": post.find("a.comments", first=True).attrs.get("href"),
                "votes": post.find(".score.unvoted", first=True).text,
                "post_date": post.find(".tagline time", first=True).attrs.get("title"),
            }

            posts_info.append(post_info)

        return posts_info

    except Exception as e:
        print("There was a problem occured: ", e)


if __name__ == "__main__":
    url = "https://old.reddit.com/r/Python/"
    pprint(get_post_containers(url))
