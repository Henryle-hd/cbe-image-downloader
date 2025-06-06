import requests
import pandas as pd
import urllib.request
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")
# print(URL)

def fetch_image(id:str):
    id=id.replace('.','_')
    image_url=f'{URL}{id}.jpg'
    print(image_url)
    file_name=f'{id}.jpg'
    try:
        img_data = requests.get(image_url)
        img_data.raise_for_status()
        return image_url
    except requests.exceptions.RequestException as e:
        return 'not found'


def download_image(image_url):
    img_data = requests.get(image_url).content
    with open(file_name, 'wb') as handler:
        handler.write(img_data)
        print(f"\033[32mDownloaded {file_name}\033[0m")





##! work for only dit3_2022_2023
def search_id(name:str):
    data=pd.read_csv('dit3_2022_2023.csv')
    data_dict=dict(zip(data['RegNo'], data['Name']))
    data=list(data_dict.items())
    name=name.upper().strip()
    l,h=0,len(data_dict)-1
    while l<=h:
        mid=(l+h)//2
        mid_v=data[mid][1]
        if mid_v.startswith(name):
            if mid==0 or not data[mid-1][1].startswith(name):
                return data[mid][0]
            h=mid-1
        elif mid_v<name:
            l=mid+1
        elif mid_v>name:
            h=mid-1
    return 'Not Found'




##! work for only dit3_2022_2023
def search_name(id:str):
    data=pd.read_csv('dit3_2022_2023_2.csv')
    data_dict=dict(zip(data['RegNo'], data['Name']))
    data=list(data_dict.items())
    id=id.strip()
    l,h=0,len(data_dict)-1
    while l<=h:
        mid=(l+h)//2
        mid_v=data[mid][0]
        if mid_v==id:
            return data[mid][1]
        elif mid_v<id:
            l=mid+1
        elif mid_v>id:
            h=mid-1
    return 'Not Found'
 
# name=input("Enter name: ")
# st_id=search_id(data,name)
if __name__=='__main__':
    # st_id=input("Search ID: ")
    print(search_id('ha'))