# simple_chat.py — Auto-Detect Model Version
from google import genai
from voice_output import VoiceOutput
import time
import sys

# --- CONFIGURATION ---
# Paste your NEW key here:
api_key = "AIzaSyBvaZKMaV-Cx4lFPj0hJkyq011blQGepE8"

# Initialize
voice = VoiceOutput()
client = genai.Client(api_key=api_key)

def simulate_typing(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

print("🔄 Connecting to Google...")

# --- STEP 1: AUTO-DETECT AVAILABLE MODEL ---
# We don't guess names. We ask the API what we can use.
valid_model = None

try:
    print("🔎 Scanning for valid models...")
    # Get all models available to your key
    for m in client.models.list():
        name = m.name
        # We look for any model with 'gemini' in the name
        if "gemini" in name and "vision" not in name:
            valid_model = name
            print(f"✅ Found working model: {valid_model}")
            break # Stop looking, we found one!

    if not valid_model:
        # Fallback if scan fails
        valid_model = "gemini-1.5-flash"
        print(f"⚠️ Scan empty. Trying default: {valid_model}")

except Exception as e:
    print(f"❌ Error scanning models: {e}")
    print("Please check your API Key.")
    sys.exit()

# --- STEP 2: START CHAT ---
try:
    chat = client.chats.create(model=valid_model)
    response = chat.send_message("Hello") # Silent test
    simulate_typing(f"\n🌟 EmoLog+ is Ready! (Using: {valid_model})")
    simulate_typing("💬 Type 'quit' to exit.\n")
except Exception as e:
    print(f"\n❌ Final Connection Failed: {e}")
    sys.exit()

# --- STEP 3: MAIN LOOP ---
while True:
    try:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit','bye']:
            print("👋 Bye!")
            break
        
        if not user_input: continue

        # Send to Google
        response = chat.send_message(user_input)
        
        # Output
        print()
        simulate_typing(f"Bot: {response.text}")
        voice.speak_async(response.text)
        print()

    except Exception as e:
        print(f"⚠️ Error: {e}")