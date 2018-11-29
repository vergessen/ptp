import config as cfg
import ptp
import requests
import sys


ptptemplate = 'https://passthepopcorn.me/torrents.php?id=%s&torrentid=%s'
omdb = 'http://www.omdbapi.com/?apikey=%s&t=%s'

r = requests.get(omdb % (cfg.omdbapi['key'], ' '.join(sys.argv[1:])))
if (r.json()['Response']) != 'False':
    ptp = ptp.Ptp(cfg.ptp['username'],cfg.ptp['password'],cfg.ptp['passkey'])
    movie = ptp.search(r.json()['imdbID'])
    if movie != None:
#BEGIN SORT MAGIC
        value = sorted( movie['Movies'][0]['Torrents'], key=lambda k:  k['Resolution'], reverse=False)
        for x in value:
#END SORT MAGIC
            print("%s : Golden: %s : Res: %s : Scene: %s : Link %s" % (x['ReleaseName'], x['GoldenPopcorn'], x['Resolution'], x['Scene'], ptptemplate % 
(movie['Movies'][0]['GroupId'],x['Id'])))
    else:    
        print('No movie found on PTP.  OMDB sent https://www.imdb.com/title/%s' % r.json()['imdbID'])
else:
    print('%s not found on OMDB' % ' '.join(sys.argv[1:]))
