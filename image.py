# import requests
# image_url='https://unsplash.com/photos/Jd09hiCUPCs'
# img_data = requests.get(image_url).content
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)

# import requests
# from bs4 import BeautifulSoup

# url = 'https://unsplash.com/s/photos/image'

# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
# images = soup.find_all('img')

# for ind, img in enumerate(images):
#    img_data = requests.get(url+img['src']).content
#    with open(f'image_{ind+1}.jpg', 'wb') as handler:
#        handler.write(img_data)