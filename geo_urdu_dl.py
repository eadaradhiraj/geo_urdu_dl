import google
import urllib2
import re
import downloads
import os
import logging

# request headers while establishing connection with the url
request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive"
}

logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s [%(funcName)s] %(message)s',
                    datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

# Get html source of url
def gethtml(url):
    return urllib2.urlopen(
        urllib2.Request(url,
                        headers=request_headers)
    ).read()

def parse_geourdu_link(folder, link):
    down_url = re.search(r'file:\s*\"(http.*?)\"\,',gethtml(link)).group(1)
    filename = down_url.split('/')[-1]
    logger.info('Downloading: {0}'.format(down_url))
    downloads.download(url=down_url,
                       out_path=os.path.join(folder,filename),
                       progress=True)
    logger.info('Finished downloading {0} to {1}'.format(filename,folder))

def get_links(movie_title, folder):
    logger.info('Searching: {0}'.format(movie_title))
    links= [res for res in google.search('{0} geo urdu'.format(movie_title), stop=10) if 'film.geourdu.com' in res]

    if links:
        for link in links:
            logger.info('Found: {0}'.format(link))
            parse_geourdu_link(folder, link)
            break
    else:
        print('Not Found!! Try a different search term or give link directly!')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download latest bollywood movies from geourdu')
    parser.add_argument('--movie', '-m', type=str, nargs='?', help='Give name of movie')
    parser.add_argument('--direct_link', '-drl', type=str, nargs='?', help='Give link to film.geourdu website')

    parser.add_argument('--directory', '-d', type=str, default='.', help = 'Give folder location')
    args = parser.parse_args()

    # parser.add_argument('--directory', '-d', type=str, default='.' help='Give folder location')
    args = parser.parse_args()
    if args.movie is not None:
        get_links(args.movie, folder=args.directory)
    elif args.direct_link is not None:
        parse_geourdu_link(args.direct_link, folder=args.directory)
    else:
        print('You have not given any links!!')