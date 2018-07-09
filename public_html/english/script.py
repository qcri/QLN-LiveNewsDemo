
import sys
#from stance_detection import getting_articles as ga
#
##
url= sys.argv[1]
#claim = sys.argv[2:]



import argparse
import json
import os


from rosette.api import API, DocumentParameters, RosetteException


def run(url,key="ec7cdb76e8130367aa00c17cc2bcc3d7", alt_url='https://api.rosette.com/rest/v1/'):
    """ Run the example """
    #categories_url_data = "https://www.nytimes.com/2018/06/26/business/trump-harley-davidson-tariffs.html?smtyp=cur&smid=tw-nytimes"
    #url = categories_url_data
    # Create an API instance
    api = API(user_key=key, service_url=alt_url)
    params = DocumentParameters()

    # Use a URL to input data instead of a string
    params["contentUri"] = url
    try:
        return api.entities(params)
    except RosetteException as exception:
        print(exception)


def mainFun(url):
    out=[]
    RESULT = run(url)
    x= json.dumps(RESULT, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8")
    x=RESULT["entities"]
#    print(x)
    d={}
    MAX=0
    for r in x:
        if r["type"]=="LOCATION":
#            print(r["mention"])
            out+=[r["mention"]]
            if r["mention"] in d:
                d[r["mention"]]+=r["count"]
            else:
                 d[r["mention"]]=r["count"]
#    for a in range(len(out)):
#        out[a]=out[a]+";;"
#    print(out)
    for key in d:
        if d[key]>MAX:
            MAX=d[key]
            location=key
    try:
        print(location)        
    except:
        print("Warning: This article doesn't have any countries mentioned.")
#    out="+".join(out)
#    print(out)
    
mainFun(url)
        
        
