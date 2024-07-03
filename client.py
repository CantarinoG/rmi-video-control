import Pyro4
import time
from videos_data import availableVideos

def main():
    ns = Pyro4.locateNS(host="192.168.3.109")  

    videos = []

    for videoData in availableVideos:
        uri = ns.lookup(videoData["name"])
        video = Pyro4.Proxy(uri)
        videos.append(video)

    while True:
        print("=" * 20)
        print("Select a Video:")
        for i in range(3):
            print(f"{i}: {video.getName()}")
        index = int(input())
        print("Select an option:")
        print("0: Play")
        print("1: Pause")
        print("2: Stop")
        action = int(input())
        if action == 0:
            videos[index].play()
        elif action == 1:
            videos[index].pause()
        else:
            videos[index].stop()

if __name__ == "__main__":
    main()