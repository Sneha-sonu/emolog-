# test_voice.py - Test that voice doesn't block
import time
from voice_output import VoiceOutput

print("🔊 Testing Non-Blocking Voice...")
voice = VoiceOutput()

print("1. Starting long speech...")
voice.speak("This is a long test message to see if it blocks the program. The program should continue running while I'm speaking.")

print("2. Counting while voice is speaking...")
for i in range(1, 11):
    print(f"   Count: {i}")
    time.sleep(0.5)  # Should count WHILE speaking

print("3. Queueing more speech...")
voice.speak("First queued message")
voice.speak("Second queued message")
voice.speak("Third queued message")

print("4. Waiting for speech to finish...")
time.sleep(5)

print("\n✅ Test complete! If you saw counting while voice was speaking, it's working!")
voice.speak("Voice test complete")
voice.stop()