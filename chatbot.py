# chatbot.py - FRIENDLY VERSION
import os
import random
from google import genai
from dotenv import load_dotenv

# Load secrets
load_dotenv()

class Chatbot:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = None
        self.conversation_history = []
        
        # Friendly greetings
        self.greetings = [
            "Hi there! I'm EmoLog+, your emotional companion. How are you feeling today? 😊",
            "Hello friend! I'm here to listen and support you. What's on your mind? 💭",
            "Hey! I notice you're here. How can I help you feel better today? 🌈",
            "Welcome back! I've been thinking about you. How has your day been? ☀️"
        ]
        
        # Empathetic responses for different emotions
        self.emotion_responses = {
            "happy": [
                "That's wonderful! Your happiness is contagious! 😄",
                "I'm so glad to see you feeling happy! What's making you smile? 🌟",
                "Your positive energy is amazing! Let's celebrate this moment! 🎉",
                "Happiness looks good on you! Tell me more about what's bringing you joy! ✨"
            ],
            "sad": [
                "I'm here for you during this difficult time. 💙",
                "It's okay to feel sad. I'm listening whenever you're ready to talk. 🤗",
                "Take all the time you need. I'll be right here with you. 🌧️",
                "Your feelings are valid. Would you like to share what's on your heart? 💔"
            ],
            "angry": [
                "I can see you're upset. Let's take a deep breath together. 🌬️",
                "Anger is a valid emotion. I'm here to help you process it. 🧘",
                "It's okay to feel angry. Want to talk about what's bothering you? ⚡",
                "I'm listening without judgment. Let's work through this together. 🤝"
            ],
            "neutral": [
                "You seem thoughtful today. What's on your mind? 🤔",
                "How are you really feeling behind that neutral expression? 💭",
                "I'm here whenever you're ready to share. No pressure. 🕊️",
                "Sometimes neutral moments are perfect for reflection. How are you? 🌿"
            ],
            "surprise": [
                "Wow! Something unexpected happened! Want to share? 😲",
                "I can see the surprise! Is this a good surprise or a challenging one? 🎭",
                "Life's full of surprises! How are you handling this one? 🌈",
                "That surprised look tells a story! What's going on? 📖"
            ]
        }
        
        if not self.api_key:
            print("⚠️ Chatbot: API Key missing. Using friendly local responses.")
        else:
            try:
                self.client = genai.Client(api_key=self.api_key)
                print("✅ Chatbot: Connected with friendly AI mode")
            except Exception as e:
                print(f"⚠️ Chatbot Error: {e}")
                print("Using local friendly responses instead.")

    def get_friendly_greeting(self):
        """Return a random friendly greeting"""
        return random.choice(self.greetings)
    
    def get_empathetic_response(self, emotion):
        """Get a warm response based on emotion"""
        if emotion in self.emotion_responses:
            return random.choice(self.emotion_responses[emotion])
        return "I'm here for you, no matter what you're feeling. 💖"
    
    def get_response(self, user_text, current_emotion="neutral"):
        """
        Generates a friendly, empathetic reply considering text and emotion.
        """
        # First, check if this is a greeting
        if any(word in user_text.lower() for word in ['hi', 'hello', 'hey', 'greetings']):
            return self.get_friendly_greeting()
        
        # If no AI available, use local responses
        if not self.client:
            return self.get_empathetic_response(current_emotion)
        
        try:
            # Create a warm, friendly prompt
            prompt = f"""
            CONTEXT:
            You are EmoLog+, a warm, empathetic, and friendly emotional support companion.
            
            USER'S WORDS: "{user_text}"
            USER'S CURRENT EMOTION (from facial expression): {current_emotion.upper()}
            
            INSTRUCTIONS:
            1. Be warm, kind, and supportive - like a caring friend
            2. Acknowledge their emotion gently
            3. Keep response short (1-2 sentences max)
            4. Use emojis occasionally for warmth
            5. If they share something difficult, offer gentle support
            6. If they're happy, celebrate with them
            7. Always end with an open invitation to share more
            
            IMPORTANT: Don't sound like a therapist or robot. Be human, warm, casual.
            
            YOUR RESPONSE:
            """
            
            response = self.client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )
            
            # Add to conversation history
            self.conversation_history.append({
                "user": user_text,
                "bot": response.text.strip(),
                "emotion": current_emotion
            })
            
            # Keep only last 10 conversations
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]
            
            return response.text.strip()
            
        except Exception as e:
            # Fallback to local response
            print(f"⚠️ AI failed: {e}")
            return self.get_empathetic_response(current_emotion)
    
    def get_conversation_summary(self):
        """Get a summary of the conversation"""
        if not self.conversation_history:
            return "We haven't chatted much yet. Let's start a conversation! 💬"
        
        emotions = [item["emotion"] for item in self.conversation_history]
        common_emotion = max(set(emotions), key=emotions.count)
        
        return f"We've been talking for a while. I notice you've been mostly {common_emotion}. I'm here to continue supporting you! 💝"

if __name__ == "__main__":
    # Test the friendly chatbot
    bot = Chatbot()
    print("🤖 Friendly Chatbot Test:")
    print("-" * 40)
    print(f"Greeting: {bot.get_friendly_greeting()}")
    
    test_scenarios = [
        ("I'm feeling great today!", "happy"),
        ("I'm really sad about something", "sad"),
        ("This makes me so angry!", "angry"),
        ("Just checking in", "neutral"),
    ]
    
    for text, emotion in test_scenarios:
        print(f"\nYou: {text}")
        print(f"Emotion: {emotion}")
        response = bot.get_response(text, emotion)
        print(f"Bot: {response}")