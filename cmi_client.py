import Pyro4
import time
from data import availableVideos
from data import nsIp

def main():
    ns = Pyro4.locateNS(host=nsIp)  

    videos = []

    for videoData in availableVideos:
        try:
            uri = ns.lookup(videoData["name"])
            video = Pyro4.Proxy(uri)
            videos.append(video)
        except Exception as e:
            print(f"An error ocurred when connecting to {videoData['name']}")

    while True:
        print("=" * 20)
        print("Select a Video:")
        i = 0
        for video in videos:
            print(f"{i}: {video.getName()}")
            i += 1
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