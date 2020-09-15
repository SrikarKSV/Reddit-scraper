from scrape.convert_categories import convert_categories
from scrape.scrape_subreddit import paginate
import click


@click.command()
@click.argument("url", type=str, required=True)
@click.option("-npg", "--no-of-pages", type=int, default=None, help="Enter number of pages to scrape.")
@click.option("-npo", "--no-of-posts", type=int, default=None, help="Enter number of posts to scrape.")
@click.option("-c",
              type=click.Choice(['n', 'r', "ch", "c24", "cw", "cm",
                                 "cy", "ca", "th", "t24", "tw", "tm", "ty", "ta"], case_sensitive=False),
              help="Choose any category(Default is hot): [n: new, r: rising, ch: Controversial posts from last hour, c24: Controversial posts from 24 hours, cw: Controversial posts from last week, cy: Controversial posts from last year, ca: Controversial posts all time, th: Top posts from last hour, t24: Top posts from last 24 hours, tw: Top posts from last week, tm: Top posts from last month, ty: Top posts from last year, ta: Top posts all time]",
              default="nope")
def main(url, no_of_pages, no_of_posts, c):
    """Enter base URL of the subreddit

    Choose scraping between number of pages(Each page has 27 posts) or posts.
    Choose category(From the presented choices in the category argument) of the subreddit to scrape(Default is hot):
    """
    url = convert_categories(url, c)
    if no_of_pages:
        print(no_of_pages)
        paginate(url, no_of_pages=no_of_pages)
    else:
        paginate(url, no_of_posts=no_of_posts)


if __name__ == "__main__":
    main()
