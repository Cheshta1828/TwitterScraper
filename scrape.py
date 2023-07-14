
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time 

username = "sachin_rt"
url = f"https://twitter.com/{username}"
chrome_options = Options()
chrome_options.add_argument("user-data-dir=/path/to/your/chrome/profile")#please add the path to your chrome profile 
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

driver.implicitly_wait(10)
page_source = driver.page_source
time.sleep(10)
soup = BeautifulSoup(page_source, "html.parser")
data = {}
bio_elements = soup.find_all('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

data['biography']=bio_elements[11].text
data['followers_count']=bio_elements[18].text
data['following_count']=bio_elements[16].text
max_length = len(bio_elements)
i = 35
while i < max_length and i<56:
    x = (bio_elements[i].text)
    cleaned_value = x.replace(',', '')
    if cleaned_value.endswith('K'):
        multiplier = 1000
        cleaned_value = cleaned_value[:-1]  # Remove the 'K' suffix

    # Remove any decimal point and convert to integer
        integer_value = int(float(cleaned_value) * multiplier)
    else:
        integer_value = int(cleaned_value)

    count = count+integer_value
    i = i + 10
print(count)
data['likes_count']=count
data['user_id']=username
print(data)
driver.quit()