# live_monitor.py
import time
import os
from mood_logger import MoodLogger
import pandas as pd

def live_mood_monitor():
    """Live monitoring of mood data as it's being collected"""
    
    logger = MoodLogger()
    previous_count = 0
    
    print("🔴 LIVE MOOD MONITOR - Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        while True:
            # Get current data
            history = logger.get_mood_history(1000)
            current_count = len(history)
            
            # Only update if new data arrived
            if current_count > previous_count:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
                
                print("🔴 LIVE MOOD MONITOR - Press Ctrl+C to stop")
                print("=" * 50)
                print(f"📈 Total records: {current_count}")
                print(f"🆕 New since last check: {current_count - previous_count}")
                
                if history:
                    # Convert to DataFrame for analysis
                    df = pd.DataFrame(history, columns=['timestamp', 'emotion', 'confidence'])
                    
                    # Show recent entries
                    print("\n📅 LAST 10 MOOD DETECTIONS:")
                    print("-" * 50)
                    for i, (timestamp, emotion, confidence) in enumerate(history[:10]):
                        print(f"  {i+1:2d}. {timestamp[11:19]} | {emotion:8} | {confidence:.2f}")
                    
                    # Show statistics
                    print(f"\n📊 CURRENT EMOTION DISTRIBUTION:")
                    print("-" * 35)
                    emotion_counts = df['emotion'].value_counts()
                    for emotion, count in emotion_counts.items():
                        print(f"  {emotion:10}: {count:3d} records")
                    
                    # Current dominant emotion
                    dominant = emotion_counts.index[0]
                    print(f"\n🎯 CURRENT DOMINANT EMOTION: {dominant.upper()}")
                    
                    # Update previous count
                    previous_count = current_count
            
            time.sleep(2)  # Check every 2 seconds
            
    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped")

if __name__ == "__main__":
    live_mood_monitor()