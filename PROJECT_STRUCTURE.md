# Project Structure

```
emotion-chatbot-app/
│
├── main.py                 # Main application file that integrates all modules
├── emotion_detector.py     # Emotion detection module using OpenCV
├── voice_input.py          # Voice and text input handling module
├── voice_output.py         # Text-to-speech output module
├── mood_logger.py          # Emotion logging to SQLite database
├── file_graph.py           # Emotion trend visualization with Matplotlib
├── reasoning_engine.py     # Emotion reasoning and response generation
├── chatbot.py              # Conversational chatbot module
├── test_modules.py         # Test script for all modules
│
├── requirements.txt        # Python package dependencies
├── setup.py                # Python package setup file
├── package.json            # Node.js package file (for VS Code integration)
├── INSTALLATION_WINDOWS.md # Detailed installation guide for Windows
├── PROJECT_STRUCTURE.md    # This file
├── README.md               # Main documentation file
│
├── .vscode/
│   └── launch.json         # VS Code launch configurations
│
└── mood_log.db             # SQLite database for emotion logging (created at runtime)
```

## Module Descriptions

### main.py
The main application that integrates all modules and manages their interactions. It provides two modes of operation:
1. Full mode with emotion detection and voice interaction
2. Text-only chat mode without emotion detection

### emotion_detector.py
Handles real-time facial emotion detection using the webcam. In this minimal implementation, it simulates emotion detection with random values. In a full implementation, it would use a pre-trained model like FER or DeepFace.

Key features:
- Detects emotions in real-time from webcam feed
- Annotates video frames with detected emotions
- Provides emotion data to other modules

### voice_input.py
Manages both voice (speech-to-text) and text input from the user.

Key features:
- Uses SpeechRecognition library for voice input
- Handles microphone access and audio processing
- Provides text input when voice is not available

### voice_output.py
Handles text-to-speech output for the application's responses.

Key features:
- Uses pyttsx3 for offline text-to-speech
- Provides asynchronous speech output
- Falls back to console output if TTS is not available

### mood_logger.py
Logs detected emotions with timestamps to a local SQLite database.

Key features:
- Creates and manages SQLite database
- Records emotion data with confidence levels
- Provides historical emotion data

### file_graph.py
Visualizes emotion trends over time using Matplotlib.

Key features:
- Generates line charts showing emotion trends
- Updates visualization in real-time
- Displays confidence levels for each emotion

### reasoning_engine.py
Provides explanations for detected emotions and generates contextual responses.

Key features:
- Maps emotions to descriptive explanations
- Generates appropriate responses based on detected emotions
- Provides reasoning for why an emotion was detected

### chatbot.py
Handles conversational interactions with the user.

Key features:
- Responds to general queries and statements
- Provides motivational and supportive responses
- Integrates with emotion detection for contextual responses