# voice_output.py - FIXED VERSION
import pyttsx3
import threading
import queue
import time

class VoiceOutput:
    def __init__(self):
        self.speech_queue = queue.Queue()
        self.is_processing = False
        self.engine = None
        
        # Start processing thread
        self.processing_thread = threading.Thread(target=self._process_speech_queue, daemon=True)
        self.processing_thread.start()
        
        try:
            self.engine = pyttsx3.init()
            
            # Configure voice properties
            voices = self.engine.getProperty('voices')
            if voices:
                self.engine.setProperty('voice', voices[0].id)
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            
            # Test voice
            print("🔊 Voice output initialized")
            
        except Exception as e:
            print(f"⚠️ Voice output warning: {e}")
            print("Voice will be simulated through text")
    
    def _process_speech_queue(self):
        """Background thread to process speech without blocking"""
        while True:
            try:
                text = self.speech_queue.get()
                if text == "STOP_THREAD":
                    break
                    
                if self.engine:
                    # Use runAndWait in the background thread
                    self.engine.say(text)
                    self.engine.runAndWait()
                else:
                    print(f"[VOICE] {text}")
                    
                self.speech_queue.task_done()
                time.sleep(0.1)  # Small pause between speeches
                
            except Exception as e:
                print(f"⚠️ Speech processing error: {e}")
                if not self.speech_queue.empty():
                    self.speech_queue.get()  # Remove failed item
                time.sleep(0.1)
    
    def speak(self, text):
        """Add speech to queue (non-blocking)"""
        if not text or text.strip() == "":
            return
            
        try:
            self.speech_queue.put(text)
            print(f"🔊 Queueing speech: {text[:50]}..." if len(text) > 50 else f"🔊 Queueing speech: {text}")
        except Exception as e:
            print(f"⚠️ Error queueing speech: {e}")
            print(f"[FALLBACK VOICE] {text}")
    
    def speak_async(self, text):
        """Alias for speak (already async)"""
        self.speak(text)
    
    def stop(self):
        """Stop the speech processing thread"""
        self.speech_queue.put("STOP_THREAD")

if __name__ == "__main__":
    # Test the voice output
    voice = VoiceOutput()
    
    print("Testing voice output...")
    voice.speak("Hello, this is a test of the non-blocking voice output module.")
    voice.speak("This second message should not block the main program.")
    
    # Simulate other work while speaking
    for i in range(5):
        print(f"Main program working... {i}")
        time.sleep(0.5)
    
    voice.speak("Test complete!")
    
    # Wait for speech to finish
    time.sleep(2)
    voice.stop()