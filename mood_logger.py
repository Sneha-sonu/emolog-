import sqlite3
from datetime import datetime

class MoodLogger:
    def __init__(self, db_path="mood_log.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize the SQLite database with a mood_log table if it doesn't exist."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mood_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                emotion TEXT NOT NULL,
                confidence REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def log_mood(self, emotion, confidence):
        """Log the detected emotion with timestamp to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO mood_log (timestamp, emotion, confidence)
            VALUES (?, ?, ?)
        ''', (timestamp, emotion, confidence))
        conn.commit()
        conn.close()
    
    def get_mood_history(self, limit=100):
        """Retrieve mood history from the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT timestamp, emotion, confidence
            FROM mood_log
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        results = cursor.fetchall()
        conn.close()
        return results

if __name__ == "__main__":
    # Test the mood logger
    logger = MoodLogger()
    logger.log_mood("Happy", 0.95)
    logger.log_mood("Sad", 0.75)
    history = logger.get_mood_history()
    print("Mood history:", history)