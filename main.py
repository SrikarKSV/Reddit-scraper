from scrape.convert_categories import convert_categories
from scrape.scrape_subreddit import paginate
import click


@click.command()
@click.argument("url", type=str, required=True)
@click.option("-npg", "--no-of-pages", type=int, default=None, help="Enter number of pages to scrape.")
@click.option("-npo", "--no-of-posts", type=int, default=None, help="Enter number of posts to scrape.")
@click.option("-c", "--category", type=click.Choice(['n', 'r', "ch", "c24", "cw", "cm", "cy", "ca", "th", "t24", "tw", "tm", "ty", "ta"]), help="Choose any category(Default is hot)", default="nope")
def main(url, no_of_pages, no_of_posts, category):
    url = convert_categories(url, category)
    if no_of_pages:
        paginate(url, no_of_pages)
    else:
        paginate(url, no_of_posts)


if __name__ == "__main__":
    main()
