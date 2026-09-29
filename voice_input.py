import speech_recognition as sr
import threading
import time

class VoiceInput:
    def __init__(self):
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.is_listening = False
            self.last_input = ""
            
            # Adjust for ambient noise
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
        except Exception as e:
            print(f"Warning: Microphone not available: {e}")
            print("Voice input will be disabled. You can still use text input.")
            self.recognizer = None
            self.microphone = None
            self.is_listening = False
            self.last_input = ""
        
    def listen_for_speech(self):
        """Continuously listen for speech input in a separate thread."""
        if not self.recognizer or not self.microphone:
            return
            
        self.is_listening = True
        while self.is_listening:
            try:
                with self.microphone as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                
                if audio:
                    text = self.recognizer.recognize_google(audio)
                    print(f"Recognized: {text}")
                    self.last_input = text
                    return text
            except sr.WaitTimeoutError:
                pass  # No speech detected in timeout period
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error with speech recognition service: {e}")
            time.sleep(0.1)
    
    def get_voice_input(self):
        """Start listening for voice input in a separate thread."""
        if self.recognizer and self.microphone:
            self.input_thread = threading.Thread(target=self.listen_for_speech)
            self.input_thread.start()
        else:
            print("Microphone not available. Voice input disabled.")
    
    def stop_listening(self):
        """Stop listening for voice input."""
        self.is_listening = False
    
    def get_text_input(self):
        """Get text input from user."""
        text = input("Enter your message: ")
        self.last_input = text
        return text
    
    def get_last_input(self):
        """Return the last received input."""
        return self.last_input

if __name__ == "__main__":
    # Test the voice input
    voice_input = VoiceInput()
    
    if voice_input.recognizer and voice_input.microphone:
        print("Testing voice input. Speak something or press Enter to skip to text input.")
        voice_input.get_voice_input()
        
        # Wait for a bit to test voice input
        time.sleep(10)
        
        voice_input.stop_listening()
        print("Last input received:", voice_input.get_last_input())
    else:
        print("Microphone not available. Testing text input only.")
    
    # Test text input
    text = voice_input.get_text_input()
    print("Text input received:", text)