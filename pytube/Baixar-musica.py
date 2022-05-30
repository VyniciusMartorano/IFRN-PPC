from pytube import YouTube
from pytube.cli import on_progress
from getpass import getuser


user = getuser()
url = str(input('Digite a url do video: ')).strip()
way = f"C:/Users/{user}/downloads/"
yt = YouTube(url, on_progress_callback=on_progress)
query = yt.streams.filter(file_extension='mp4',adaptive=True, only_audio=True)
for item in query:
    print(item)

option = int(input('Digite o Itag da opção desejada: '))
selected = query.get_by_itag(option)
selected.download(way)