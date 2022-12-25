from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import re
import string
from bs4 import BeautifulSoup

def assignment(country):
# def assignment():
  url = "https://en.wikipedia.org/wiki/"+country
#   url = "https://en.wikipedia.org/wiki/India"
  r = requests.get(url)
  soup=BeautifulSoup(r.content,'html.parser')
  for data in soup(['style', 'script']):
      data.decompose()

  def brace(str):
    str= re.sub(r'\[[\w]*\]','',str)
    str=re.sub(r'\([^)]*\)', '', str)
    str=re.sub(r'\s\+','',str)
    return str



  table=soup.find('table',class_=("infobox"))

  #flag link
  flag=soup.find('img',class_="thumbborder")
  flagy="https:"+flag['src']

  #Capital
  C=table.find(text=re.compile("Capital")).parent.parent
  Ca=C.find_all("li")
  if(Ca):
    Cap=[]
    for i in Ca:
      Cap.append(brace(i.text))
  else:
    Cap=brace(C.find("a").text)

  #Largest City
  LC=table.find(text= re.compile("argest city")).parent.parent
  Lci=LC.find_all("li")
  if(Lci):
    Lcity=[] 
    for i in Lci:  
      Lcity.append(brace(i.text))

  else:
    try:
      Lcit=LC.find("td").text
    except:
      Lcity=brace(C.find("td").text)
    else:
      Lcity=brace(Lcit)

  #Official Languages
  OL=table.find(text= re.compile("Official")).parent.parent
  Ola=OL.find_all("li")
  if(Ola):
    olan=[]
    for i in Ola:
      olan.append(brace(i.text))
  else:
    olan=brace(OL.find("td").text)

  #Area
  A=table.find(text= re.compile("Area")).parent.parent.parent.next_sibling.find("td").text
  Ar=brace(A)

  #Population
  P=table.find(text= re.compile("opulation")).parent.parent.parent.next_sibling.find("td").text
  Po=brace(P)

  #GDP
  G=table.find(text= re.compile("nominal")).parent.parent.parent.next_sibling.find("td").text
  Gd=brace(G)

  answer={"flag_link" : flagy , "capital" : Cap , "largest city":Lcity, "official languages": olan, "area_total":Ar, "Population": Po, "GDP_nominal":Gd}
  return answer

# name = input("Enter Country: ")
# assignment(name)


@api_view()
def api(request,id):
    answer=assignment(id)
    return Response(answer)


        
# Create your views here.
