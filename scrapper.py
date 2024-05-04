import requests
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def main():
    url = input("Enter the URL of the website: ")
    html_code = fetch_html(url)
    
    if html_code:
        soup = BeautifulSoup(html_code, 'html.parser')
        prettified_html = soup.prettify()
        
        print("\nPrettified HTML Code:")
        print(prettified_html)

if __name__ == "__main__":
    main()

