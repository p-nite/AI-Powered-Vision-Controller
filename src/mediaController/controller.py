import pyautogui
import time

class MediaController:
    # Sets up media control mapping and action cooldowns to prevent input spam
    def __init__(self):
        self.cooldown_time = 2.0
        self.last_action_time = 0

    # Executes keyboard shortcuts based on the provided action string
    def handle_action(self, action):
        current_time = time.time()
        
        if current_time - self.last_action_time > self.cooldown_time:
            if action == "Pinch":
                pyautogui.press('playpause')
            elif action == "Swipe_Up":
                pyautogui.press('volumeup')
            elif action == "Swipe_Down":
                pyautogui.press('volumedown')
            elif action == "Swipe_Left":
                pyautogui.press('prevtrack')
            elif action == "Swipe_Right":
                pyautogui.press('nexttrack')
            elif action == "Fist":
                pyautogui.press('volumemute')

            self.last_action_time = current_time