# AI-Powered Vision Controller

> 🚧 **Work in progress** — media control works today; an air-drawing charades game is under development (see [Roadmap](#roadmap)).

Control your computer's media playback with hand gestures in front of a webcam — no keyboard or mouse.

The webcam feed is processed with **OpenCV**, Google's **MediaPipe** machine-learning model locates 21 landmarks on the hand in real time, and a rule-based classifier turns their positions and movement into gestures. Each gesture is sent to the operating system as a media key through **PyAutoGUI**, so it works with any player (Spotify, YouTube, VLC…).

## Gestures

| Gesture | Action |
|---|---|
| Pinch (thumb and index finger together) | Play / Pause |
| Swipe up | Volume up |
| Swipe down | Volume down |
| Swipe left | Previous track |
| Swipe right | Next track |
| Closed fist | Mute / Unmute |

A 2-second cooldown between actions prevents a single movement from firing the same command several times.

## How It Works

```
Webcam frame ──► OpenCV ──► MediaPipe Hands ──► GestureTracker ──► MediaController ──► OS media key
                (capture,   (21 hand landmarks)  (rules: folded      (cooldown +        (PyAutoGUI)
                 mirror)                          fingers, pinch,     key mapping)
                                                  swipe direction)
```

| Module | Responsibility |
|---|---|
| [`src/app.py`](src/app.py) | Main loop: reads the webcam, runs the tracker, shows the video window |
| [`src/gestureController/tracker.py`](src/gestureController/tracker.py) | Detects the hand with MediaPipe and classifies the gesture |
| [`src/mediaController/controller.py`](src/mediaController/controller.py) | Maps gestures to media keys and applies the cooldown |

## Tech Stack

- **Python 3.11**
- **MediaPipe** — hand landmark detection and tracking
- **OpenCV** — webcam capture and video display
- **PyAutoGUI** — sends media keys to the operating system

## How to Run

Developed on Windows; any webcam supported by OpenCV should work.

**1. Clone the repository**

```bash
git clone https://github.com/p-nite/AI-Powered-Vision-Controller.git
cd AI-Powered-Vision-Controller
```

**2. Create a virtual environment and install the dependencies**

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

**3. Run from the project root**

```bash
python -m src.app
```

The app must be started as a module from the project root (`-m src.app`), because its imports are relative to the `src` package. Press **Esc** in the video window to quit.

## Known Limitations

- **Pinch** compares only the vertical position of the thumb and index fingertips, so some hand poses trigger it by accident.
- **Swipes** use a fixed threshold in pixels, so they become harder to trigger the further the hand is from the camera.
- Gesture rules are hand-written; adding a new gesture means writing new rules.

These are addressed in the first phases of the roadmap.

## Roadmap

1. **Air drawing** — draw on screen while pinching: pinch measured as the real thumb–index distance relative to hand size, separate start/stop thresholds so strokes don't break, and smoothing to remove landmark jitter.
2. **Charades game** — one player draws a word in the air while the others guess, with turns, a timer and scores.
3. **Tests** — unit tests for gesture detection and game rules.
4. **Trained gesture classifier** — replace the hand-written rules with a small model trained on recorded hand landmarks, so new gestures can be taught instead of coded.
5. **AI guesser** — a CNN trained on a subset of Google's *Quick, Draw!* dataset that guesses the drawing in real time, as a "play against the AI" mode.

## License

This project is licensed under the [MIT License](LICENSE).
