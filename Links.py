import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = 'https://www.sc.com/en/'

# Function to get all URLs and their names
def get_all_urls_and_names(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        # Check if the URL is absolute or relative
        full_url = href if href.startswith('http') or href.startswith('https') else requests.compat.urljoin(base_url, href)
        
        # Get the name of the application (link text)
        app_name = link.get_text(strip=True)
        
        # Append the data (application name and URL)
        data.append({
            'Application Name': app_name,
            'URL': full_url
        })
    
    return data

# Get all URLs and their names
info_list = get_all_urls_and_names(url)

# Create a DataFrame with Application Name first
df = pd.DataFrame(info_list)

# Save DataFrame to an Excel file
df.to_excel('application_names_and_urls.xlsx', index=False)
