# Build script for EmoLog+
import os
import shutil

def build_emolog_plus():
    print("🔨 Building EmoLog+ Application...")
    
    dist_folder = "EmoLogPlus_Distribution"
    if os.path.exists(dist_folder):
        shutil.rmtree(dist_folder)
    os.makedirs(dist_folder)
    
    files_to_copy = [
        "EmoLog_Plus_Launcher.py",
        "main.py", 
        "emotion_detector.py",
        "chatbot.py",
        "file_graph.py", 
        "mood_logger.py",
        "voice_input.py",
        "voice_output.py", 
        "reasoning_engine.py",
        "test_modules.py",
        "requirements.txt",
        "setup_emolog.py",
        "live_monitor.py",
        "simple_chat.py"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, dist_folder)
            print(f"✅ Copied: {file}")
    
    # Create batch files
    create_batch_files(dist_folder)
    
    print(f"\n🎉 EmoLog+ distribution created in: {dist_folder}")
    print("📦 Ready for distribution!")

def create_batch_files(dist_folder):
    # Windows launcher
    with open(os.path.join(dist_folder, "Launch_EmoLog+.bat"), "w") as f:
        f.write('''@echo off
title EmoLog+ Launcher
echo Starting EmoLog+...
python EmoLog_Plus_Launcher.py
pause
''')
    
    # Installer batch
    with open(os.path.join(dist_folder, "Install_EmoLog+.bat"), "w") as f:
        f.write('''@echo off
title EmoLog+ Installer
echo Installing EmoLog+ dependencies...
pip install -r requirements.txt
echo Installation complete!
python EmoLog_Plus_Launcher.py
pause
''')

if __name__ == "__main__":
    build_emolog_plus()