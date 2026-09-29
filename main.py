# main.py - FRIENDLY SIMPLE VERSION (2-SECOND DETECTION)
import cv2
import time
import sys
import random

# Import modules
try:
    from emotion_detector import EmotionDetector
    from voice_input import VoiceInput
    from voice_output import VoiceOutput
    from mood_logger import MoodLogger
    from reasoning_engine import ReasoningEngine
    from chatbot import Chatbot  # <-- ADD THIS!
    print("✅ All modules loaded")
except ImportError as e:
    print(f"❌ Missing module: {e}")
    sys.exit(1)

class FriendlyEmoLogPlus:
    def __init__(self):
        print("\n" + "="*60)
        print("🎭 EmoLog+ - Your Friendly Emotional Companion")
        print("="*60)
        
        try:
            self.detector = EmotionDetector()
            self.voice_input = VoiceInput()
            self.voice_output = VoiceOutput()
            self.logger = MoodLogger()
            self.reasoning = ReasoningEngine()
            self.chatbot = Chatbot()  # <-- CREATE CHATBOT INSTANCE
            
            self.running = True
            self.detection_count = 0
            self.last_detection_time = 0
            self.detection_interval = 2  # Detect every 2 seconds
            
            print("✅ System initialized with care and empathy")
            print("📊 Emotion detection set to 2-second intervals")
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            self.running = False
    
    def run(self):
        """Main loop with camera - 2-second detection"""
        if not self.running:
            return
        
        # Start with friendly greeting
        greeting = self.chatbot.get_friendly_greeting()
        print(f"\n🤖: {greeting}")
        self.voice_output.speak(greeting)
        time.sleep(1)
        
        print("\n📷 Opening camera...")
        print("🔄 Emotion detection will run every 2 seconds")
        
        # Try to open camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("📱 Running in friendly chat mode")
            self.run_friendly_chat_mode()
            return
        
        print("✅ Camera ready")
        print("\n💬 Just talk to me naturally!")
        print("I'm here to listen and support you. 💝")
        print("="*50)
        
        last_emotion = None
        current_emotion = "neutral"
        current_confidence = 0.0
        
        try:
            while self.running:
                current_time = time.time()
                
                # Read camera frame
                ret, frame = cap.read()
                if not ret:
                    print("❌ Failed to read frame")
                    break
                
                # Detect emotion only every 2 seconds
                if current_time - self.last_detection_time >= self.detection_interval:
                    emotion, confidence, _ = self.detector.detect_emotion(frame)
                    current_emotion = emotion
                    current_confidence = confidence
                    self.detection_count += 1
                    self.last_detection_time = current_time
                    
                    # Display emotion info with timestamp
                    timestamp = time.strftime("%H:%M:%S", time.localtime())
                    print(f"\n[{timestamp}] Detected: {emotion:10s} | Confidence: {confidence:.2f} | Total: {self.detection_count}")
                    
                    # Log to database if confidence is good
                    if confidence > 0.5:
                        self.logger.log_mood(emotion, confidence)
                    
                    # Comment on emotion changes
                    if last_emotion and emotion != last_emotion and confidence > 0.7:
                        if random.random() < 0.4:  # 40% chance to comment
                            self.comment_on_change(last_emotion, emotion)
                    
                    last_emotion = emotion
                else:
                    # Show time until next detection
                    time_left = self.detection_interval - (current_time - self.last_detection_time)
                    print(f"\rNext detection in: {time_left:.1f}s | Current: {current_emotion:10s}", end="", flush=True)
                
                # Always display on frame (using cached values)
                frame = self.detector.annotate_frame(frame, [])
                cv2.putText(frame, f"I see: {current_emotion}", (20, 40), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(frame, f"Confidence: {current_confidence:.2f}", (20, 70), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                
                # Add detection timing info
                time_since_detection = current_time - self.last_detection_time
                time_until_next = max(0, self.detection_interval - time_since_detection)
                
                # Color-code the timer
                if time_until_next > 1:
                    timer_color = (200, 200, 100)  # Yellow
                else:
                    timer_color = (100, 200, 255)  # Orange
                
                cv2.putText(frame, f"Next: {time_until_next:.0f}s", 
                           (frame.shape[1] - 100, frame.shape[0] - 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, timer_color, 1)
                
                cv2.putText(frame, "Just talk to me! I'm listening... 💬", 
                           (20, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
                
                cv2.imshow('EmoLog+ | Your Friendly Companion', frame)
                
                # Handle keyboard
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord('q'):
                    break
                elif key == ord('s'):
                    self.speak_emotion(current_emotion, current_confidence)
                elif key == ord('g'):
                    self.generate_graphs()
                elif key == ord('h'):
                    self.say_hello()
                elif key == ord('d'):  # Force immediate detection
                    print("\n🔍 Manual detection triggered!")
                    self.last_detection_time = 0  # Reset timer for immediate detection
                
                # Check for voice input
                voice_text = self.voice_input.get_last_input()
                if voice_text:
                    self.process_friendly_voice(voice_text, current_emotion)
                
                # Small delay
                time.sleep(0.05)
        
        finally:
            cap.release()
            cv2.destroyAllWindows()
            self.friendly_shutdown()
    
    def run_friendly_chat_mode(self):
        """Run without camera - just friendly chat"""
        print("\n💬 Let's have a friendly chat!")
        print("Type anything or 'quit' when done")
        print("-" * 40)
        
        # Start with greeting
        greeting = self.chatbot.get_friendly_greeting()
        print(f"🤖: {greeting}")
        
        last_detection_time = 0
        detection_interval = 2  # 2-second intervals in chat mode too
        
        while self.running:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'bye', 'exit', 'goodbye']:
                self.running = False
                break
            
            current_time = time.time()
            
            # Simulate emotion for chat mode every 2 seconds
            if current_time - last_detection_time >= detection_interval:
                emotion, confidence, _ = self.detector.detect_emotion(None)
                last_detection_time = current_time
                print(f"[{time.strftime('%H:%M:%S')}] Detected mood: {emotion}")
            else:
                emotion, confidence = self.detector.last_emotion, self.detector.last_confidence
            
            # Get friendly response
            response = self.chatbot.get_response(user_input, emotion)
            print(f"🤖: {response}")
            self.voice_output.speak(response)
            
            # Log the interaction
            self.detection_count += 1
        
        self.friendly_shutdown()
    
    def comment_on_change(self, old_emotion, new_emotion):
        """Gently comment on emotion change"""
        messages = [
            f"I notice you're feeling {new_emotion} now. Everything okay? 💭",
            f"Your mood shifted from {old_emotion} to {new_emotion}. Want to talk about it? 🤗",
            f"I see you're {new_emotion} now. How are you feeling with this change? 🌈"
        ]
        message = random.choice(messages)
        print(f"\n🤖: {message}")
        self.voice_output.speak(message)
    
    def speak_emotion(self, emotion, confidence):
        """Speak the current emotion in friendly way"""
        message = self.reasoning.get_emotion_response(emotion)
        print(f"\n🔊 Speaking: {message}")
        self.voice_output.speak(message)
    
    def say_hello(self):
        """Say a friendly hello"""
        hello = random.choice([
            "Hello there! How are you feeling today? 😊",
            "Hi friend! I'm here for you. What's on your mind? 💭",
            "Hey! I'm listening. How can I support you today? 🤗"
        ])
        print(f"\n🤖: {hello}")
        self.voice_output.speak(hello)
    
    def generate_graphs(self):
        """Generate mood graphs"""
        print("\n📊 Generating your emotional journey map...")
        try:
            from file_graph import create_trend_graph, create_distribution_chart
            create_trend_graph()
            create_distribution_chart()
            print("✅ Your emotional insights are ready!")
            self.voice_output.speak("I've created a beautiful graph of your emotions!")
        except Exception as e:
            print(f"❌ Graph error: {e}")
            self.voice_output.speak("I had trouble creating the graphs, but I'm still here for you!")
    
    def process_friendly_voice(self, text, current_emotion):
        """Process voice input in friendly way"""
        print(f"\n🎤 You: {text}")
        
        # Check for special commands
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['quit', 'bye', 'exit', 'goodbye']):
            farewell = random.choice([
                "It was wonderful talking with you! Take care. 💝",
                "Thanks for sharing your time with me. Be kind to yourself! ✨",
                "Goodbye friend! Remember I'm always here for you. 🤗"
            ])
            print(f"🤖: {farewell}")
            self.voice_output.speak(farewell)
            self.running = False
            return
        
        elif 'how am i' in text_lower:
            self.give_emotional_insight(current_emotion)
            return
        
        elif 'thank' in text_lower:
            thanks = random.choice([
                "You're very welcome! I'm happy to help. 💖",
                "Anytime! It's my pleasure to support you. 🌟",
                "Thank YOU for sharing with me. It means a lot. 🤗"
            ])
            print(f"🤖: {thanks}")
            self.voice_output.speak(thanks)
            return
        
        elif 'detect now' in text_lower or 'check my emotion' in text_lower:
            print("\n🤖: Let me check your current emotional state...")
            self.last_detection_time = 0  # Force immediate detection on next loop
            return
        
        # Normal conversation with chatbot
        response = self.chatbot.get_response(text, current_emotion)
        print(f"🤖: {response}")
        self.voice_output.speak(response)
    
    def give_emotional_insight(self, current_emotion):
        """Provide friendly emotional insight"""
        insight = self.reasoning.explain_emotion(current_emotion)
        response = self.reasoning.get_emotion_response(current_emotion)
        
        print(f"\n💡 Emotional Insight:")
        print(f"Current emotion: {current_emotion}")
        print(f"Observation: {insight}")
        print(f"Support: {response}")
        
        self.voice_output.speak(f"I sense you're feeling {current_emotion}. {response}")
    
    def friendly_shutdown(self):
        """Warm, friendly shutdown"""
        print("\n" + "="*60)
        print("🛑 Saying goodbye with love...")
        
        # Generate final graphs
        try:
            from file_graph import create_trend_graph, create_distribution_chart
            create_trend_graph()
            create_distribution_chart()
            print("📊 Your emotional journey map is saved!")
        except:
            pass
        
        # Friendly farewell
        farewells = [
            "Thank you for sharing your time with me. You're amazing! ✨",
            "I enjoyed our time together. Take good care of yourself! 💖",
            "Thanks for the conversation. Remember, I'm always here for you! 🌟",
            "Our time together meant a lot. You're stronger than you know! 💪"
        ]
        
        farewell = random.choice(farewells)
        print(f"\n🤖: {farewell}")
        print(f"\n📊 Session Summary:")
        print(f"• Emotions detected: {self.detection_count}")
        print(f"• Detection interval: {self.detection_interval} seconds")
        print(f"• Data saved: mood_log.db")
        print(f"• Insights saved: mood_trend_graph.png")
        print("\n" + "="*60)
        print("👋 Until next time! Be kind to yourself. 💝")
        
        self.voice_output.speak(farewell)
        time.sleep(2)
        self.voice_output.stop()

def main():
    """Main function"""
    print("Starting your friendly emotional companion...")
    print("📊 Emotion detection runs every 2 seconds")
    print("   - Press 'd' to force immediate detection")
    print("   - Press 's' to hear emotional feedback")
    print("   - Press 'g' to generate graphs")
    print("   - Press 'q' to quit")
    
    try:
        app = FriendlyEmoLogPlus()
        app.run()
    except KeyboardInterrupt:
        print("\n\n💝 You're always welcome back! Take care.")
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        print("Please try again or check your setup.")

if __name__ == "__main__":
    main()