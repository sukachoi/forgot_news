from bs4 import BeautifulSoup 
import requests 
l_st=[]
num=''
url="https://www1.president.go.kr/petitions/602674"
response=requests.get(url)
html=response.content
html1=response.text
soup=BeautifulSoup(html,'html.parser')
soup1=BeautifulSoup(html1,'html.parser')
#print('1',soup.p)
#print('2',soup.strong.string)
#print('3',soup.h1)
#for child in soup.h2.children:
#    print('child==',child,'\n')
#print(soup.find_all("h2"),'\n')
#aticle=soup.find_all(attrs={'class':'go_trans _article_content', 'id':'dic_area'})
#aticle=soup.find_all( 'div', {'class':'text'})
aticle=soup.find('div', {'class':'View_write'})#.find_all("p")
print(aticle.text.strip().replace('\n',''))
#for i in aticle:
#    if(i.text != '' and i.text != '\n'):
#        print(i.text.rstrip())
"""
sentence= soup.select('table')
print('기사내용',sentence)
for i in sentence:
    l_st.append(i.get_text())
print(l_st)
for x in aticle:
    print('x====',soup.select("div.dic_area")[x].get_text())    
    
print(l_st)    
"""  