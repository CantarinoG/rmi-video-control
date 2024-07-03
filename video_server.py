import sys
from video import Video
from videos_data import availableVideos

import Pyro4
@Pyro4.expose 

def main():

    #As informações dos vídeos são previamente declaradas numa lista de Maps em videos_data.py
    #Para escolher qual dos vídeos listados lá vai rodar nesse servidor, basta adicionar o índice do vídeo como argumento ao rodar esse script
    #Exemplo: "python3 video_server.py 1" roda o vídeo que está no índice 1, ou seja, o segundo da lista

    index = int(sys.argv[1])

    if (index < 0 or index >= len(availableVideos)):
        print("Invalid index.")
        exit()

    videoData = availableVideos[index]

    video = Video(videoData["name"], videoData["path"])

    daemon = Pyro4.Daemon(host="192.168.3.109")

    ns = Pyro4.locateNS()

    uri = daemon.register(video)

    ns.register(video.name, uri)

    print(f"Server is ready. {video.name} is ready to play!")

    daemon.requestLoop()

if __name__ == "__main__":
    main()