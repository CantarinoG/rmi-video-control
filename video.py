import Pyro4
import cv2
import threading
@Pyro4.expose 

class Video():
    def __init__(self, name, videoPath):
        self.name = name
        self.paused = True
        self.cap = cv2.VideoCapture(videoPath)
        self.lock = threading.Lock()

        if not self.cap.isOpened():
            print("Error opening video capture")
            exit()

        thread = threading.Thread(target=self.displayVideo)
        thread.start()
        
    def displayVideo(self):
        while True:
            if not self.paused:
                with self.lock:
                    ret, frame = self.cap.read()

                if not ret:
                    print("Video finished, restarting...")
                    with self.lock:
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue 

                cv2.imshow("Video", frame)

                if cv2.waitKey(33) == ord('q'):
                    break

        with self.lock:
            self.cap.release()
        cv2.destroyAllWindows()

    def play(self):
        self.paused = False

    def pause(self):
        self.paused = True

    def stop(self):
        with self.lock:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.paused = True

    def getName(self):
        return self.name
