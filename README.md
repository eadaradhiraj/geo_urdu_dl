Geo Urdu Movie Download Script
========================

About
-----
Geo urdu Movie Download Script downloads movies from film.geourdu.com. The user can employ the option of finding the movie link through google search or inputting the the geourdu link to download the file

Dependencies
------------

  * Python 2.7 & Python3
  * google (``pip install google``)
  * downloads (``pip install downloads``)
  
  Note
  ----
  Please keep in mind that the youtube-dl module interferes with the google module and import errors may be caused as there     is a google module within the youtube-dl module.

Tested on Ubuntu Linux and Windows. It should work on any Linux, OS X, or Windows machine as long as the dependencies are installed.

Usage
-----

Mandatory argument:
  -m, --movie  <movie title to be searched for in google>
  or
  -drl, --direct_link <the direct link from film.geourdu.com>

 Optional Arguments:
  -d, --directory <download directory>

To download the movie:

    ~ $ python geo_urdu_dl.py -m MOVIE_TITLE -d DIRECTORY
    or
    ~ $ python geo_urdu_dl.py -drl GEOURDU_LINK -d DIRECTORY

Examples
--------
Download https://film.geourdu.com/jolly-llb-2-2017.html (2016) movie

    ~ $ python geo_urdu_dl.py -drl https://film.geourdu.com/jolly-llb-2-2017.html -d ~/Videos

Download https://film.geourdu.com/jolly-llb-2-2017.html (2016) movie using google search 

    ~ $ python geo_urdu_dl.py -m 'jolly llb 2' -d ~/Videos
