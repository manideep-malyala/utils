# %pip install -qU duckduckgo-search langchain-community
from langchain_community.tools import DuckDuckGoSearchResults

def web_search(search_keyword):
    search = DuckDuckGoSearchResults(output_format="list", num_results=10)
    results = search.invoke(search_keyword)
    links = [item['link'] for item in results if 'link' in item and is_valid_url(item['link']) ]
    return links
