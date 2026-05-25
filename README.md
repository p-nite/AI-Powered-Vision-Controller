# AI-Powered Vision Controller

An AI-driven, real-time hand gesture recognition system that allows users to control OS-level multimedia actions without touching the keyboard or mouse. 

This project leverages Google's MediaPipe for robust hand tracking and OpenCV for video processing, translating physical movements into direct system commands via PyAutoGUI.

## Features

Currently, the system maps the following hand gestures to media controls:

* **Pinch:** Play / Pause
* **Swipe Up:** Volume Up
* **Swipe Down:** Volume Down
* **Swipe Left:** Previous Track
* **Swipe Right:** Next Track
* **Closed Fist:** Mute / Unmute

*An internal cooldown mechanism is implemented to prevent input spamming and ensure smooth OS interactions.*

## Tech Stack

* **Python 3.11.9**
* **MediaPipe:** Hand landmark detection and tracking.
* **OpenCV (`cv2`):** Real-time webcam video capture and image processing.
* **PyAutoGUI:** Cross-platform GUI automation to execute keyboard shortcuts.

## How to Run

**1. Clone the repository:**
`git clone https://github.com/p-nite/AI-Powered-Vision-Controller.git`
`cd AI-Powered-Vision-Controller`

**2. Install dependencies:**
Make sure you have Python installed. Then, install the required libraries:
`pip install opencv-python mediapipe pyautogui`

**3. Run the application:**
`python app.py`

*(Press `Ctrl+C` in the terminal or close the webcam window to stop the execution).*

## Roadmap / Future Implementations

This project is actively in development. Upcoming features include:

* **Tracker Optimization:** Refine the coordinate calculation logic to improve gesture accuracy and minimize latency.
* **Charades Game Mode:** Introduce a new interactive mode where holding a "Pinch" gesture allows the user to draw on the screen (mimicking holding a pencil) to play charades.

## License

This project is licensed under the [MIT License](LICENSE).