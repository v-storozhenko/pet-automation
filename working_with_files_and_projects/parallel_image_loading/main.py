"""
Модуль для загрузки изображений.
"""
import concurrent.futures

import requests


def _download_image(url):
    """Загрузка изображения через requests."""
    response = requests.get(url, timeout=50)
    file_name = url.split("/")[-1]  # имя файла из ссылки
    with open(file_name, "wb") as file:
        file.write(response.content)
    print(f"Скачан {file_name}")


def download_images(urls):
    """Параллельная загрузка изображений."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(_download_image, urls)


if __name__ == '__main__.py':
    # примеры урлов
    image_urls = [
        "https://c4.wallpaperflare.com/wallpaper/1/398/339/"
        "elden-ring-landscape-game-art-video-game-art-video-games-hd-wallpaper-preview.jpg",
        "https://c4.wallpaperflare.com/wallpaper/67/97/91/"
        "elden-ring-ranni-elden-ring-hd-wallpaper-preview.jpg",
    ]
    download_images(image_urls)
