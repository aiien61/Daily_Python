"""
The creation and destruction of processes are costly, and even more costly than threads, 
so the pool of processes is designed to efficiently manage and use processes in order for 
better performance.

frequent creation and destruction of threads have more serioues impact on performance than that of processes

https://realpython.com/python-multiprocessing/
"""
import os
import time
from typing import Iterable, List
from urllib.request import urlopen, Request
from concurrent.futures import ProcessPoolExecutor as Pool
from concurrent.futures import Future


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
    urls: List[str] = [
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
    download_images_using_pool_map()
