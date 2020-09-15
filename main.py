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
              help="Choose any category: [n: new, r: rising, ch: Controversial posts from last hour, c24: Controversial posts from 24 hours, cw: Controversial posts from last week, cy: Controversial posts from last year, ca: Controversial posts all time, th: Top posts from last hour, t24: Top posts from last 24 hours, tw: Top posts from last week, tm: Top posts from last month, ty: Top posts from last year, ta: Top posts all time]",
              default="nope")
@click.option("-o", "--output-file", type=str, default="reddit", help="Name output file(Default is 'reddit.csv')")
def main(url, no_of_pages, no_of_posts, c, output_file):
    """Enter base URL of the subreddit.

    Ex: main.py -npg | -npo=<number of posts/pages> -c=<category> <URL> -o <output-file>
    """
    url = convert_categories(url, c)
    if no_of_pages:
        paginate(url, no_of_pages=no_of_pages, output_file=output_file)
    else:
        paginate(url, no_of_posts=no_of_posts, output_file=output_file)


if __name__ == "__main__":
    main()
