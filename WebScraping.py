from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url='https://www.flipkart.com/search?q=apple+smart+watch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_19_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_19_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=apple+smart+watch%7CSmart+Watches&requestId=ef743f4b-409b-48de-87ef-ee16a9709bf9&as-searchtext=apple%20smart%20watches'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"_13oc-S"})

#print(len(containers))
#print(soup.prettify(containers[0]))
container=containers[0]
#print(container.div.img["alt"])

ratings=container.findAll("div",{"class":"_3LWZlK"})
#print(ratings[0].text)


filename="products.csv"
headers="Product Name, Pricing, Ratings\n"
with open ('products.csv', 'w', encoding="utf-8") as f:
    f.write(headers)

    for container in containers:
        product_name=container.div.img["alt"]
        price_container=container.findAll("div",{"class":"_30jeq3 _1_WHN1"})
        price=price_container[0].text.strip()
        ratings_container=container.findAll("div",{"class":"_3LWZlK"})
        rating=ratings_container[0].text
        print("Product name:"+product_name)
        print("price:"+price)
        print("ratings:"+rating)

        #(situation code) implementing string parsing in case of facing extra data in an unavaoidable way
        '''trim_price=''.join(price.split(','))
        rm_rupee=trim_price.split("₹")
        add_rs_price+"RS."+rm_rupee[1]
        split_price=add_rs_price.split('g')
        final_price=split_price[0]
        split_rating=rating.split("")
        final_rating=split_rating[0]
        print(product_name.replace(",","|")+","+final_price+","+final_rating+"\n")
        f.write(product_name.replace(",","|")+"."final_price+","+final_rating+"\n")'''
        
        f.write(product_name+","+price+","+rating+"\n")
    f.close()


