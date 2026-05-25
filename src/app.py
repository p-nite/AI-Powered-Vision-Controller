import cv2

from src.mediaController.controller import MediaController
from src.gestureController.tracker import GestureTracker

class Application:
    # Main application loop orchestrating the camera, tracker, and controller
    def run(self):
        cap = cv2.VideoCapture(0)
        tracker = GestureTracker()
        controller = MediaController()

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            
            action = tracker.get_action(frame)
            if action:
                controller.handle_action(action)
                cv2.putText(frame, action, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Media Controller App', frame)
            
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = Application()
    app.run()