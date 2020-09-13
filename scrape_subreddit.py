from requests_html import HTMLSession

url = "https://old.reddit.com/r/Python/"

session = HTMLSession()

r = session.get(url)

post_containers = r.html.find(".thing.link")

cleaned_post_containers = [
    post_container
    for post_container in post_containers
    if "promoted" not in post_container.attrs["class"]
]

print(len(cleaned_post_containers))
