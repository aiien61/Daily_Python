#! /usr/bin/env python3
# multidownload.py - Downloads XKCD comics using multiple threads.
import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

def download_xkcd(start_comic, end_comic):
    for url_num in range(start_comic, end_comic):
        print(f'Downloading page https://xkcd.com/{url_num}...')
        response = requests.get(f'http://xkcd.com/{url_num}')
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text)

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image.
            print(f'Downloading image {comic_url}...')
            response = requests.get(comic_url)
            response.raise_for_status()

            # Save the image to ./xkcd
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in response.iter_content(100_000):
                image_file.write(chunk)
            image_file.close()

# Create and start the Thread objects.
downloadthreads = []
for i in range(0, 1400, 100):
    downloadthread = threading.Thread(target=download_xkcd, args=(i, i+99))
    downloadthreads.append(downloadthread)
    downloadthread.start()

# Wait for all threads to end.
for downloadthread in downloadthreads:
    downloadthread.join()

print('Done.')