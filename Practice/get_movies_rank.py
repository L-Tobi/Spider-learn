import requests
import lxml
def get_one_page(url):
    responses = requests.get(url)
    if  responses.status_code == 200:
        return responses.text
    return None