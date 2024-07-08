import sys
from video import Video
from data import availableVideos
from data import daemonIp
from data import nsIp

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

    with Pyro4.Daemon(host="192.168.0.106", port=9095 + index) as daemon:
        uri = daemon.register(video)
        with Pyro4.locateNS() as ns:
            ns.register(f"example.video.{video.name}", uri)
        print(f"Server running with {video.name}")
        daemon.requestLoop()

if __name__ == "__main__":
    main()
