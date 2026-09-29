import cv2
import random
import time

class EmotionDetector:
    def __init__(self):
        # List of emotions to detect
        self.emotions = [
            "happy", "sad", "angry", "surprise", "neutral", "fear",
            "anxious", "lonely", "tired", "excited", "confused", "bored"
        ]
        # Colors for each emotion (B, G, R)
        self.emotion_colors = {
            "happy": (0, 255, 0), "sad": (255, 0, 0), "angry": (0, 0, 255),
            "surprise": (255, 255, 0), "neutral": (200, 200, 200), "fear": (128, 0, 128),
            "anxious": (255, 165, 0), "lonely": (100, 100, 255), "tired": (128, 128, 128),
            "excited": (0, 255, 255), "confused": (255, 105, 180), "bored": (169, 169, 169)
        }
        self.last_emotion = "neutral"
        self.last_confidence = 0.0
        self.last_detection_time = 0
        self.detection_interval = 2  # Detect every 2 seconds
        
    def detect_emotion(self, frame):
        """
        Simulates emotion detection at reduced frequency.
        Only performs detection every 2 seconds to save CPU.
        """
        current_time = time.time()
        
        # Only detect if enough time has passed
        if current_time - self.last_detection_time < self.detection_interval:
            # Return cached results
            return self.last_emotion, self.last_confidence, []
        
        # Simulate processing time (but less frequently)
        time.sleep(0.01)
        
        # Pick a random emotion for testing
        emotion = random.choice(self.emotions)
        confidence = random.uniform(0.7, 0.99)
        
        # Update cache
        self.last_emotion = emotion
        self.last_confidence = confidence
        self.last_detection_time = current_time
        
        # Return format: emotion, confidence, boxes (empty for simulation)
        return emotion, confidence, []
    
    def annotate_frame(self, frame, emotions):
        """Draws the emotion text on the camera feed."""
        if self.last_emotion:
            # Get color
            color = self.emotion_colors.get(self.last_emotion, (255, 255, 255))
            
            # Draw Main Label
            label = f"Status: {self.last_emotion.upper()} ({int(self.last_confidence*100)}%)"
            cv2.putText(frame, label, (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
            # Add indicator that detection is intermittent
            time_since_detection = time.time() - self.last_detection_time
            if time_since_detection < 0.5:  # Just updated
                cv2.putText(frame, "🔄 Updated", (frame.shape[1] - 150, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)
            
            # Draw Instruction
            cv2.putText(frame, "Press 'Q' to quit", (20, frame.shape[0] - 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        return frame

if __name__ == "__main__":
    # Test this module independently
    print("Testing Emotion Detector...")
    det = EmotionDetector()
    print(f"Detected: {det.detect_emotion(None)}")