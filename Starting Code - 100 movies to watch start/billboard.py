from bs4 import BeautifulSoup
import requests
url="https://www.billboard.com/charts/hot-100/2000-08-12/"
web_text=(requests.get(url)).text

soup=BeautifulSoup(web_text,"html.parser")
lst=soup.select(selector=".c-title")
final=[]
for song in lst:
    final.append(song.getText())
print(filter(final[100:150],"Songwriter"))
# <span title="Friday, August 11, 2000" class="e-day">11</span>

# <p class="c-tagline  a-font-primary-medium-xs u-font-size-11@mobile-max u-letter-spacing-0106 u-letter-spacing-0089@mobile-max lrv-u-line-height-copy lrv-u-text-transform-uppercase lrv-u-margin-a-00 lrv-u-padding-l-075 lrv-u-padding-l-00@mobile-max">Week of August 19, 2000</p>

# <h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only">

	
	
		
# 					Jumpin', Jumpin'		
	
# </h3>