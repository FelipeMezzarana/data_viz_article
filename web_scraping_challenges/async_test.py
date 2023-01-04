
import requests 
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from time import perf_counter


def synchronous_request(n):
    """Run n requests to the same site (synchronously)
    * http://books.toscrape.com/ is a Web Scraping Sandbox, for learning and practice purpose

    n -- qnt. of requests
    """

    t_start = perf_counter()
    # Perform n requests to the same site 
    for i in range(50):
        resp = requests.get('http://books.toscrape.com/')
        bs = BeautifulSoup(resp.text, 'html.parser') 
        print(f'Request {i+1} - Status Code: {resp.status_code}')

    t_end = perf_counter()
    print(f'\nTotal Time: {t_end-t_start:.2f}')

# Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications
async def asynchronous_request(n):
    """Run n requests to the same site (asynchronously)
    * http://books.toscrape.com/ is a Web Scraping Sandbox, for learning and practice purpose
    
    n -- qnt. of requests
    """

    t_start = perf_counter()
    # Declare a ClientSession and execute the requests through it
    async with aiohttp.ClientSession() as session:
        # n requests to the same site 
        for i in range(n):
            async with session.get('http://books.toscrape.com/') as resp:
                # Any object returned by calling a coroutine function, needs to be awaited.
                html = await resp.text()
                bs = BeautifulSoup(html, 'html.parser')
                print(f'Request {i+1} - Status Code: {resp.status}')
    
    t_end = perf_counter()
    print(f'\nTotal Time: {t_end-t_start:.2f}')
    
if __name__ == '__main__':
    synchronous_request()
    #asyncio.run(asynchronous_request())