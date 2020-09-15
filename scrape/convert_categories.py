import sys


def convert_categories(url: str, category: str) -> str:
    url = url.rstrip('/')
    categories = {
        "nope": "/",
        "n": "/new/",
        "r": "/rising/",
        "ch": "/controversial/?sort=controversial&t=hour",
        "c24": "/controversial/?sort=controversial&t=day",
        "cw": "/controversial/?sort=controversial&t=week",
        "cm": "/controversial/?sort=controversial&t=month",
        "cy": "/controversial/?sort=controversial&t=year",
        "ca": "/controversial/?sort=controversial&t=all",
        "th": "/top/?sort=top&t=hour",
        "t24": "/top/?sort=top&t=day",
        "tw": "/top/?sort=top&t=week",
        "tm": "/top/?sort=top&t=month",
        "ty": "/top/?sort=top&t=year",
        "ta": "/top/?sort=top&t=all",
    }

    if category not in categories:
        print("The category asked doesn't exist in our data")
        sys.exit()

    return url + categories.get(category)


if __name__ == "__main__":
    print(convert_categories("https://old.reddit.com/r/DearPyGui/", "ty"))
