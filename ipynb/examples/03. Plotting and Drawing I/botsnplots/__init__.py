import urllib
import cStringIO

def loadImage(URL):
    """ function to load an image from a URL """
    return cStringIO.StringIO(urllib.urlopen(URL).read())
