import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
URL=os.getenv("DOC_URL")
def fetch_doc_names():
    try:
        response=requests.get(URL)
        response.raise_for_status()
        soup=BeautifulSoup(response.text, "html.parser")
        traws = soup.find_all("a")
        doc_names=[]
        for link in traws[5:]:
            doc_names.append(link.get('href'))
            # print(link.get('href'))
        # print(doc_names)
        return doc_names
    except:
        print("Error occured")
        quit()

if __name__=="__main__":
    fetch_doc_names()

