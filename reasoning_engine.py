# reasoning_engine.py - FRIENDLY VERSION
import os
import random
from dotenv import load_dotenv
from google import genai

# 1. Load the secret key from your .env file
load_dotenv()

class ReasoningEngine:
    def __init__(self):
        # --- SECURE CONNECTION ---
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = None
        self.use_ai = False

        if not self.api_key:
            print("⚠️ Could not find 'GEMINI_API_KEY' in .env file.")
        else:
            try:
                self.client = genai.Client(api_key=self.api_key)
                self.use_ai = True
                print("✅ Emotion Engine: Online (AI Connected)")
            except Exception as e:
                print(f"⚠️ Emotion Engine: Offline. Error: {e}")

        # --- FRIENDLY RESPONSES ---
        self.emotion_explanations = {
            "angry": "I notice some tension in your expression - furrowed brows and a set jaw.",
            "disgust": "Your face shows a wrinkled nose - like something doesn't sit right.",
            "fear": "I see wide eyes and raised eyebrows - something seems concerning.",
            "happy": "That beautiful smile and crinkled eyes tell me you're feeling good! 😊",
            "sad": "I notice a downturned mouth and lowered eyebrows - heavy feelings.",
            "surprise": "Wow! Your eyes are wide open - something unexpected happened!",
            "neutral": "You have a calm, thoughtful expression right now.",
            "excited": "I can see the sparkle in your eyes! Something wonderful is happening! ✨",
            "tired": "Your expression shows some fatigue - you've been working hard.",
            "anxious": "I notice some restlessness in your expression - nervous energy.",
            "confused": "Your thoughtful expression shows you're working through something complex.",
            "bored": "You seem like you're looking for something more engaging."
        }
        
        self.emotion_responses = {
            "angry": [
                "I can see you're upset. Take a deep breath with me - I'm right here. 🌬️",
                "Your frustration is valid. Want to vent? I'm all ears. 👂",
                "Let's work through this anger together, one step at a time. 🤝",
                "It's okay to feel angry. I'm here to help you find calm. 🧘"
            ],
            "happy": [
                "Your smile is lighting up the room! Tell me what's making you so happy! 🌟",
                "I love seeing you this joyful! Your positive energy is beautiful! ✨",
                "Happiness looks amazing on you! Let's savor this moment together! 😄",
                "Your good mood is contagious! What wonderful thing happened? 🎉"
            ],
            "sad": [
                "I'm holding space for your sadness. You don't have to carry it alone. 💙",
                "It's okay to not be okay. I'm here whenever you're ready to talk. 🤗",
                "Your feelings matter. Would a virtual hug help right now? 🤗",
                "Take your time with these feelings. I'll be right here with you. 🌧️"
            ],
            "neutral": [
                "How are you really feeling behind that calm expression? 💭",
                "Sometimes neutral moments are perfect for checking in with ourselves. How are you? 🌿",
                "You seem thoughtful. Want to share what's on your mind? 🤔",
                "I'm here if you want to explore what's beneath the surface. 🕊️"
            ],
            "fear": [
                "It's natural to feel scared sometimes. You're safe here with me. 🛡️",
                "Let's breathe through this fear together. In and out, slowly. 🌬️",
                "I'm here to help you feel secure. What would help right now? 🤝",
                "Fear can be overwhelming. Let's face it together, one breath at a time. 💪"
            ],
            "surprise": [
                "Wow! Something unexpected! Is this a good surprise? 😲",
                "That surprised expression tells a story! Want to share what happened? 📖",
                "Life's full of surprises! How are you handling this one? 🎭",
                "I see the surprise! Exciting or challenging? Either way, I'm here! 🌈"
            ]
        }
    
    def explain_emotion(self, emotion):
        """Returns friendly facial analysis."""
        return self.emotion_explanations.get(emotion, f"I notice you're feeling {emotion}.")
    
    def get_emotion_response(self, emotion):
        """
        Generates a warm, human-like response.
        """
        # 1. Try AI for personalized response
        if self.use_ai:
            try:
                prompt = f"""
                You are a warm, empathetic friend noticing someone's emotion.
                
                The person you're talking to appears to be feeling: {emotion.upper()}
                
                Write a short, warm, one-sentence response to them.
                - If they're happy: Celebrate with them! Use emojis! 🎉
                - If they're sad: Offer gentle comfort and presence
                - If they're angry: Acknowledge their feelings and offer support
                - If they're neutral: Invite gentle reflection
                - Be human, casual, and caring - not robotic
                - Include an occasional emoji for warmth
                - End with an open heart
                
                Your response (max 1 sentence):
                """
                
                response = self.client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=prompt
                )
                return response.text.strip()
            except Exception:
                pass
        
        # 2. Fallback to friendly static list
        if emotion in self.emotion_responses:
            return random.choice(self.emotion_responses[emotion])
        else:
            return f"I notice you're feeling {emotion}. I'm here with you. 💝"
    
    def get_daily_checkin(self):
        """Get a friendly daily check-in message"""
        checkins = [
            "How's your heart feeling today, my friend? 💓",
            "Checking in - how are you really doing today? 🌈",
            "Hello beautiful soul! How are you feeling in this moment? ✨",
            "Just wanted to send some love your way. How are you today? 💌",
            "How's the world treating you today? I'm here to listen. 🌍"
        ]
        return random.choice(checkins)

if __name__ == "__main__":
    engine = ReasoningEngine()
    
    print("\n🤖 Friendly Emotion Responses Test:")
    print("=" * 50)
    
    test_emotions = ["happy", "sad", "angry", "surprise", "neutral", "excited"]
    
    for emo in test_emotions:
        print(f"\n[Emotion: {emo.upper()}]")
        print(f"Explanation: {engine.explain_emotion(emo)}")
        print(f"Response: {engine.get_emotion_response(emo)}")
        print("-" * 40)