"""
The creation and destruction of threads are costly, so the pool of threads is designed to 
efficiently manage and use threads in order for better performance.

https://realpython.com/intro-to-python-threading/
"""
import os
import time
from typing import Iterable
from urllib.request import urlopen, Request
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor as Pool


def task(name: str) -> str:
    print(f"{name} - step 1\n", end='')
    time.sleep(1)
    print(f"{name} - step 2\n", end='')
    
    return f"{name} - completed"


def execute_pool_manual() -> None:
    with Pool() as pool:
        a: Future = pool.submit(task, "A")
        b: Future = pool.submit(task, "B")

        print(a.result())
        print(b.result())

def execute_pool_auto() -> None:
    with Pool() as pool:
        result: Iterable[str] = pool.map(task, ['c', 'd'])
        for r in result:
            print(r)


def download_img(url: str) -> None:
    site_url: str = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(site_url) as response:
        image_data: bytes = response.read()

    if not image_data:
        raise Exception(f"Can't download image from {url}")
    
    filename: str = os.path.basename(url)
    os.makedirs('images', exist_ok=True)
    filename = os.path.join('images', filename)
    with open(filename, 'wb') as file:
        file.write(image_data)

    return f"{filename} downloaded, {url}"

def download_images_using_pool_map() -> None:
    urls = [
        "https://cdn.pixabay.com/photo/2021/09/28/13/14/cat-6664412_1280.jpg",
        "https://cdn.pixabay.com/photo/2022/11/10/00/38/creative-7581718_640.jpg",
        "https://cdn.pixabay.com/photo/2022/11/19/11/53/rose-7601873_640.jpg",
        "https://cdn.pixabay.com/photo/2022/10/18/12/05/clouds-7530090_640.jpg"
    ]

    with Pool() as pool:
        results: Iterable[str] = pool.map(download_img, urls)
        for res in results:
            print(res)


if __name__ == "__main__":
    # execute_pool_manual()
    execute_pool_auto()
    # download_images_using_pool_map()
