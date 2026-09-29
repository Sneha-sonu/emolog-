import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def check_environment():
    """Check if we have everything needed"""
    if not os.path.exists("mood_log.db"):
        print("❌ mood_log.db not found!")
        return False
    
    conn = sqlite3.connect("mood_log.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM mood_log")
    count = cursor.fetchone()[0]
    conn.close()
    
    if count == 0:
        print("❌ No data in database!")
        return False
    
    print(f"✅ Found {count} mood records")
    return True

def create_trend_graph():
    """Create and save trend graph"""
    try:
        conn = sqlite3.connect("mood_log.db")
        df = pd.read_sql_query("SELECT * FROM mood_log ORDER BY timestamp", conn)
        conn.close()
        
        if df.empty:
            return False
            
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        
        plt.figure(figsize=(14, 8))
        
        emotion_colors = {
            "happy": "#00FF7F",       # Spring Green
            "sad": "#4682B4",         # Steel Blue
            "angry": "#DC143C",       # Crimson
            "surprise": "#FFD700",    # Gold
            "neutral": "#696969",     # Dim Gray
            "fear": "#9370DB",        # Medium Purple
            "excited": "#FF1493",     # Deep Pink
            "tired": "#708090",       # Slate Gray
            "anxious": "#FF8C00",     # Dark Orange
            "confused": "#BA55D3",    # Medium Orchid
            "bored": "#A9A9A9"        # Dark Gray
        }
        
        for emotion in df['emotion'].unique():
            emotion_data = df[df['emotion'] == emotion]
            color = emotion_colors.get(emotion, '#000000')
            plt.plot(emotion_data['timestamp'], emotion_data['confidence'],
                     marker='o', markersize=4, linewidth=2,
                     label=emotion.upper(), color=color, alpha=0.8)
        
        plt.title('Emotion Trends Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Time')
        plt.ylabel('Confidence Level')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.ylim(0, 1.0)
        
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M'))
        plt.gcf().autofmt_xdate()
        
        plt.tight_layout()
        plt.savefig('mood_trend_graph.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("✅ mood_trend_graph.png saved")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_distribution_chart():
    """Create and save distribution chart with emotion-color mapping"""
    try:
        conn = sqlite3.connect("mood_log.db")
        df = pd.read_sql_query("SELECT emotion, COUNT(*) as count FROM mood_log GROUP BY emotion", conn)
        conn.close()

        emotion_colors = {
            "happy": "#00FF7F", "sad": "#4682B4", "angry": "#DC143C",
            "surprise": "#FFD700", "neutral": "#696969", "fear": "#9370DB",
            "excited": "#FF1493", "tired": "#708090", "anxious": "#FF8C00",
            "confused": "#BA55D3", "bored": "#A9A9A9"
        }

        df['color'] = df['emotion'].map(emotion_colors).fillna('#000000')

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        wedges, texts, autotexts = ax1.pie(
            df['count'], labels=df['emotion'],
            autopct='%1.1f%%', colors=df['color'],
            startangle=90
        )
        ax1.set_title('Emotion Distribution')

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        bars = ax2.bar(df['emotion'], df['count'], color=df['color'], alpha=0.7)
        ax2.set_title('Emotion Frequency')
        ax2.set_xlabel('Emotions')
        ax2.set_ylabel('Count')
        ax2.tick_params(axis='x', rotation=45)

        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                     f'{int(height)}', ha='center', va='bottom')

        plt.tight_layout()
        plt.savefig('emotion_distribution.png', dpi=150, bbox_inches='tight')
        plt.close()

        print("✅ emotion_distribution.png saved")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function for standalone graph generation"""
    print("💾 FILE GRAPH GENERATOR")
    print("=" * 35)
    
    if not check_environment():
        print("\n💡 Run this first: python main.py")
        return
    
    success_count = 0
    
    if create_trend_graph():
        success_count += 1
    
    if create_distribution_chart():
        success_count += 1
    
    print(f"\n🎉 {success_count}/2 files generated in: {os.getcwd()}")

# Functions for main.py to call
if __name__ == "__main__":
    main()
