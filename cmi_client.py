import Pyro4
import time
from data import availableVideos
from data import nsIp

def main():

    videos = []
    with Pyro4.locateNS() as ns:
        for video, videoUri in ns.list(prefix="example.video.").items():
            print("found video", video)
            videos.append(Pyro4.Proxy(videoUri))
    if not videos:
        raise ValueError("no videos found! (have you started the servers first?)")
    

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