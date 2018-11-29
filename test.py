import config as cfg
import ptp

ptptemplate = 'https://passthepopcorn.me/torrents.php?id=%s&torrentid=%s'
ptp = ptp.Ptp(cfg.ptp['username'],cfg.ptp['password'],cfg.ptp['passkey'])
movie = ptp.search('tt1860357')
#BEGIN SORT MAGIC
value = sorted( movie['Movies'][0]['Torrents'], key=lambda k:  k['Resolution'], reverse=False)
for x in value:
#END SORT MAGIC
     print("%s : Golden: %s : Res: %s : Scene: %s : Link %s" % (x['ReleaseName'], x['GoldenPopcorn'], x['Resolution'], x['Scene'], ptptemplate % (movie['Movies'][0]['GroupId'],x['Id'])))

