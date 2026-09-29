# Emotion Detection Chatbot Application

This application combines real-time facial emotion detection with a voice/text chatbot that responds contextually to detected emotions. It runs all modules simultaneously to provide an interactive emotional assistant experience.

## Features

1. **Real-time Emotion Detection**
   - Detects facial emotions using your laptop webcam
   - Uses the FER (Facial Expression Recognition) library with a pre-trained model
   - Displays live video feed with emotion labels

2. **Voice/Text Input**
   - Accepts user input through microphone (speech-to-text)
   - Also accepts typed text input

3. **Voice Output**
   - Responds using text-to-speech
   - Uses pyttsx3 for offline speech synthesis

4. **Mood Logger**
   - Stores each detected emotion with timestamp in a SQLite database
   - Records emotion confidence levels

5. **file graph(trend_visualization)**
   - Generates a Matplotlib chart showing emotion trends over time
   - Updates dynamically while the program runs

6. **Reasoning Explanation**
   - Provides explanations for detected emotions
   - Example: "Your tone was low and face showed downturned lips" for sadness

7. **Chatbot Integration**
   - Human-friendly chatbot that answers general queries
   - Provides motivational support and casual conversation
   - Works in sync with detected emotions

8. **Real-Time Integration**
   - All modules work simultaneously
   - Webcam emotion detection runs in real-time
   - Voice input/output runs interactively
   - Mood logger updates continuously
   - Mood graph updates dynamically

## Requirements

- Python 3.10+
- Windows OS (for VS Code execution)
- Webcam for emotion detection

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- opencv-python
- fer
- SpeechRecognition
- pyttsx3
- matplotlib
- pandas
- numpy

## Usage

### Running the Application

1. Open the project in VS Code
2. Run the main application:

```bash
python main.py
```

### How to Use

1. When you run the application, a webcam window will open showing real-time emotion detection
2. The application will also start listening for voice input
3. Speak naturally or type in the console to interact with the chatbot
4. The chatbot will respond both in text (in the console) and through voice output
5. A file graph will update in real-time as emotions are detected
6. Press 'q' in the emotion detection window to quit the application

### Text-Only Chat Mode

If you want to use only text-based chat without emotion detection:

```bash
python main.py --text-chat
```

## Modules

- `emotion_detector.py`: Handles real-time facial emotion detection using FER
- `voice_input.py`: Manages both voice (speech-to-text) and text input
- `voice_output.py`: Handles text-to-speech output
- `mood_logger.py`: Logs detected emotions with timestamps to SQLite database
- `file_graph.py`: Visualizes emotion trends over time using Matplotlib
- `reasoning_engine.py`: Provides explanations for detected emotions
- `chatbot.py`: Implements the conversational chatbot functionality
- `main.py`: Integrates all modules into a single application

## Notes

- The emotion detection may take a few seconds to initialize
- For best results, ensure good lighting conditions for your webcam
- The voice input works best in quiet environments
- Emotion responses are provided periodically (every 10 seconds by default) to avoid overwhelming the user