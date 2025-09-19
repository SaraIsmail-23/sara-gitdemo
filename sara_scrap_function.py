import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap():
    response = requests.get('https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=machine%20learning%20jobs%20in%20Egypt')
    soup = BeautifulSoup(response.content,'lxml')

    titles = soup.find_all('h2',{'class':'css-193uk2c'})
    # translate to list comprehension
    titles_list = [title.a.text for title in titles]

    links_list = [title.a['href'] for title in titles]

    occupations = soup.find_all('div', {'class': 'css-5jhz9n'})
    occupations_list = [occupation.text for occupation in occupations]

    companies = soup.find_all("a",{'class': 'css-ipsyv7'})
    companies_list = [company.text for company in companies]

    specs = soup.find_all('div', {'class':'css-1rhj4yg'})
    specs_list = [spec.text for spec in specs]

    scraped_data = {}
    scraped_data['titles'] =  titles_list
    scraped_data['links'] = links_list
    scraped_data['occupations'] = occupations_list
    scraped_data['companies'] = companies_list
    scraped_data['specs'] = specs_list

    table = pd.DataFrame(scraped_data)
    table.to_csv('Sara_Scraped_file_py.csv', index = False)
    print('Jobs Scraped Sucessfully')
    return table

if __name__ == '__main__':
    scrap()