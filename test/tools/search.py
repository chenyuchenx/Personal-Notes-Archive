from langchain.tools import tool
import os, json, requests

class SearchTools():
   
    @tool("Search internet")
    def search_internet(query):
       """Useful to search the internet about a given topic and return relevant results."""
       return SearchTools.search(query)
    
    @tool("Search instagram")
    def search_instagram(query):
       """Useful to search for instagram post about a given topic and return relevant results."""
       query = f"site:instagram.com {query}"
       return SearchTools.search(query)

    def search(query, top_n=5):
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", "https://google.serper.dev/search", headers=headers, data=payload)
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        results = response.json()['organic']
        stirng = []
        for result in results[:top_n]:
          try:
            stirng.append('\n'.join([
                f"Title: {result['title']}", f"Link: {result['link']}",
                f"Snippet: {result['snippet']}", "\n-----------------"
            ]))
          except KeyError:
            next    
        content = '\n'.join(stirng)
        return f"\nSearch result: {content}\n"