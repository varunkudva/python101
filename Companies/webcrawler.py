"""
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
def crawl_urls():
    def get_urls(url):
        pass

    with ThreadPoolExecutor(max_workers=8) as executor:
        tasks_queue = [executor.submit(htmlParser.getUrls, startUrl)]
        for tasks in concurrent.futures.as_completed(tasks_queue):
"""
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        import threading
        from concurrent import futures

        def hostname(url):
            return url.split('/')[2]

        def worker(url):
            url = None
            while True:
                queue_lock.acquire()
                if url_queue:
                    url = url_queue.pop(0)
                queue_lock.release()
                if not url: continue
                for next_url in htmlParser.getUrls(url):
                    if hostname(next_url) != start_hostname:
                        continue

                    if next_url not in visited:
                        queue_lock.acquire()
                        visited.add(next_url)
                        url_queue.append(next_url)
                        queue_lock.release()

        start_hostname = hostname(startUrl)
        visited = set()
        queue_lock = threading.Lock()
        url_queue = [startUrl]
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            for i in range(8): executor.submit(worker)

        return list(visited)

"""
class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        import threading
        
        #get urls is blocking
        def fetch_url(url):
            print("worker " + url)
            url_list = htmlParser.getUrls(url)
            #print(url_list)
            with queue_lock:
                url_queue.append(url_list)
            
        def hostname(url):
            return url.split('/')[2]
        
        start_hostname = hostname(startUrl)
        url_queue = [startUrl]
        visited = set()
        res = []
        queue_lock = threading.Lock()
        while url_queue:
            print(url_queue)    
            url = url_queue.pop(0)
            if hostname(url) != start_hostname:
                continue
                
            if url not in visited:
                visited.add(url)
                worker = threading.Thread(target=fetch_url, args=(url,))
                worker.start()
                if not url_queue:
                    worker.join()
                    
        return list(visited)
"""