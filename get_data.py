import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

liste = []
bliste = []

url = 'https://www.sikayetvar.com'
firma = '/firma_adı'
konu = '/ürün_adı'

n = input( 'Çekilecek sayfa sayısını giriniz: ' )

for i in range(1,int(n)+1):
	try:
		i = str( i)
		print( i + '. sayfa tamamlandı' )
		r = requests.get( url + firma + konu + '?page=' + i )
		soup = bs( r.content, 'html.parser' )
		title = soup.find_all( 'h5' , class_= 'card-title' )
	except Exception:
		print( i +'. başlıkta hata' )
		continue
	for a in title:
		href = a.find( 'a' )
		bliste.append( href.get_text() )
		link = href.get( 'href' )
		r2 = requests.get( url + link )
		iceriksayfa = bs( r2.content,'html.parser' )
		sonuc = iceriksayfa.find( 'div' , class_= 'card-text' )
		cumle = sonuc.get_text().strip()
		liste.append(cumle)


sliste = bliste + liste

print( '\n\nReady your file.\nPlease wait...' )

df = pd.DataFrame( sliste )
df.to_csv( './full_data.txt', index=False )
