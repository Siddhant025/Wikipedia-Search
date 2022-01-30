import sys
import requests
import os

home_dir=os.path.expanduser('~')
wiki_search=sys.argv
# print(wiki_search)


log_file=(home_dir+'/Desktop/log.txt')

def search_wiki(logfile,wiki_list):

    for i in range(1,len(wiki_list)):
        print('searched For:  '+wiki_list[i])
        url = 'https://en.wikipedia.org/w/api.php'
        params = {
            'action': 'query',
            'format': 'json',
            'titles': wiki_list[i],
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        page = next(iter(data['query']['pages'].values()))
        # print(page)
        if page['extract']:
            print(page['extract'])
            url="https://en.wikipedia.org/wiki/"+wiki_list[i]
            
            file = open(logfile,'a')
            file.write(url+"\n")
            file.close()
        else:
            print('No Such thing as '+wiki_list[i]+' on Wikipedia')
        



search_wiki(log_file,wiki_search)