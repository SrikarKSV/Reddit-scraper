from requests_html import HTMLSession
import re


def get_post_containers(url: str) -> list:

    assert bool(re.match("https://(www.)?(old\.)?reddit.com/r/\w+", url))

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

        return cleaned_post_containers

    except Exception as e:
        print("There was a problem occured: ", e)


if __name__ == "__main__":
    url = "https://old.reddit.com/r/PY2423534T/"
    get_post_containers(url)
