from requests_html import HTMLSession
import re
import csv
import time


def get_post_containers(url: str) -> list:

    assert bool(
        re.match("https://(www.)?(old\.)?reddit.com/r/\w+", url)
    ), "The URL provided is not a valid subreddit URL"

    url = convert_new_links_to_old(url)

    try:
        session = HTMLSession()
        r = session.get(url)

        r.raise_for_status()

        post_containers = r.html.find(".thing.link")
        next_page_link = r.html.find("span.next-button a", first=True)

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

        return posts_info, next_page_link

    except Exception as e:
        print("There was a problem occurred: ", e)


def paginate(url: str, no_of_pages: int = None, no_of_posts: int = None) -> None:
    with open("reddit_data.csv", "a", encoding="utf-8", newline="\n") as f:
        fieldnames = ["title", "author", "post_link", "votes", "post_date"]
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        if no_of_pages:
            scrape_based_on_pages(url, no_of_pages, csv_writer)
        else:
            scrape_based_on_posts(url, no_of_posts, csv_writer)


def scrape_based_on_pages(url: str, no_of_pages: int, csv_writer: csv.DictWriter):
    for page in range(1, no_of_pages):
        posts_data, url = get_post_containers(url)
        csv_writer.writerows(posts_data)
        print("Completed Page: ", page)

        if url:
            url = url.attrs.get("href")
        else:
            print("We came to the end of the subreddit and have scraped everything!")
            break
        time.sleep(3)


def scrape_based_on_posts(url: str, no_of_posts: int, csv_writer: csv.DictWriter):
    no_of_posts_saved = 0
    loop = True
    while loop:
        posts_data, url = get_post_containers(url)
        for post_data in posts_data:
            if no_of_posts_saved >= no_of_posts:
                print(f"{no_of_posts} have been scraped and saved!")
                loop = False
                break

            csv_writer.writerow(post_data)
            no_of_posts_saved += 1

        if url:
            url = url.attrs.get("href")
        else:
            print("We came to the end of the subreddit and have scraped everything!")
            break

        time.sleep(3)


def convert_new_links_to_old(url: str) -> str:
    if "old" not in url:
        url = url.replace("www.", "")
        r_position = url.find("reddit")
        url = url[:r_position] + "old." + url[r_position:]

    return url


if __name__ == "__main__":
    url = "https://www.reddit.com/r/DearPyGui/"
    paginate(url, no_of_posts=5)
