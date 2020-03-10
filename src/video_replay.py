import cv2
import sys

class VideoController:
    def __init__(self, file_name):
        self.video = self.load_video(file_name)
        self.capture = []
        self.is_capturing = False
        self.replay_count = 0

    def load_video(self, file_name):
        return cv2.VideoCapture(file_name)

    def play(self):
        print("Press 'q' to capture video.")
        self.is_capturing = False
        while self.video.isOpened():
            ret, frame = self.video.read()
            if self.is_capturing:
                self.capture.append(frame)
            cv2.imshow('frame', frame)
            key = cv2.waitKey(25) & 0xFF
            if key == ord('q'):
                if self.is_capturing:
                    break
                else:
                    print("Start capturing. Press 'q' to Stop.")
                    self.is_capturing = True
        self.video.release()
        cv2.destroyAllWindows()

    def replay(self):
        print(f"Start replay. Press 'q' to exit.")
        while True:
            self.replay_count += 1
            print(f"Count: {self.replay_count}")
            key = None
            for f in self.capture:
                cv2.imshow('frame', f)
                key = cv2.waitKey(25) & 0xFF
                if key == ord('q'):
                    break
            if key == ord('q'):
                break
        cv2.destroyAllWindows()


def main():
    try:
        file_name = sys.argv[1]
        v = VideoController(file_name)
        v.play()
        v.replay()
    except IndexError as e:
        print(f"Usage: python {sys.argv[0]} {'{file_name}'}")

if __name__ == "__main__":
    main()
