import cv2
import mediapipe as mp

class GestureTracker:
    def __init__(self):
        # Initializes the hand tracking model using the direct internal import
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.prev_x, self.prev_y = 0, 0

    def get_action(self, frame):
        """
        Evaluates hand landmarks to detect specific gestures including swipes, pinches, and a closed fist.
        Returns the identified gesture as a string.
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        action = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                
                # Arrays with indices for finger tips and middle joints
                tips = [self.mp_hands.HandLandmark.INDEX_FINGER_TIP, 
                        self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP, 
                        self.mp_hands.HandLandmark.RING_FINGER_TIP, 
                        self.mp_hands.HandLandmark.PINKY_TIP]
                
                mids = [self.mp_hands.HandLandmark.INDEX_FINGER_MCP, 
                        self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP, 
                        self.mp_hands.HandLandmark.RING_FINGER_MCP, 
                        self.mp_hands.HandLandmark.PINKY_MCP]
                
                # Calculates how many fingers are folded into a fist
                folded_fingers = sum(1 for tip, mid in zip(tips, mids) if landmarks[tip].y > landmarks[mid].y)

                index_tip = landmarks[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = landmarks[self.mp_hands.HandLandmark.THUMB_TIP]
                
                h, w, _ = frame.shape
                curr_x, curr_y = int(index_tip.x * w), int(index_tip.y * h)
                
                # Logic to determine the gesture based on coordinates
                if folded_fingers == 4:
                    action = "Fist"
                elif abs(index_tip.y - thumb_tip.y) < 0.05:
                    action = "Pinch"
                elif self.prev_x != 0 and self.prev_y != 0:
                    if curr_x - self.prev_x > 40:
                        action = "Swipe_Right"
                    elif self.prev_x - curr_x > 40:
                        action = "Swipe_Left"
                    elif curr_y - self.prev_y > 40:
                        action = "Swipe_Down"
                    elif self.prev_y - curr_y > 40:
                        action = "Swipe_Up"

                self.prev_x, self.prev_y = curr_x, curr_y

        return action