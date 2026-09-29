import time
from emotion_detector import EmotionDetector
from voice_input import VoiceInput
from voice_output import VoiceOutput
from mood_logger import MoodLogger
from file_graph import create_trend_graph, create_distribution_chart
from reasoning_engine import ReasoningEngine
from chatbot import Chatbot

def test_all_modules():
    print("Testing all modules...")
    
    # Test mood logger
    print("1. Testing Mood Logger...")
    logger = MoodLogger()
    logger.log_mood("happy", 0.95)
    logger.log_mood("sad", 0.75)
    history = logger.get_mood_history()
    print(f"Mood history: {history}")
    
    # Test file graph
    print("2. Testing File Graph Visualization...")
    trend_success = create_trend_graph()
    dist_success = create_distribution_chart()

    if trend_success and dist_success:
     print("✅ Mood graphs generated successfully")
    else:
     print("❌ Graph generation failed")

    
    # Test reasoning engine
    print("3. Testing Reasoning Engine...")
    engine = ReasoningEngine()
    for emotion in ["happy", "sad", "angry"]:
        explanation = engine.explain_emotion(emotion)
        response = engine.get_emotion_response(emotion)
        print(f"{emotion}: {explanation}")
        print(f"Response: {response}")
    
    # Test chatbot
    print("4. Testing Chatbot...")
    bot = Chatbot()
    test_inputs = ["hello", "how are you", "I feel sad today", "bye"]
    for inp in test_inputs:
        response = bot.get_response(inp)
        print(f"Input: {inp} -> Response: {response}")
    
    # Test voice output
    print("5. Testing Voice Output...")
    voice = VoiceOutput()
    voice.speak("Testing voice output module")
    print("Voice output completed")
    
    print("All modules tested successfully!")

if __name__ == "__main__":
    test_all_modules()