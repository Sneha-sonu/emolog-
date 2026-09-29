import sqlite3
conn = sqlite3.connect("mood_log.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mood_log (
    timestamp TEXT,
    emotion TEXT,
    confidence REAL
)
""")

sample_data = [
    ("2025-10-04 14:00:00", "happy", 0.85),
    ("2025-10-04 14:10:00", "sad", 0.65),
    ("2025-10-04 14:20:00", "angry", 0.75),
    ("2025-10-04 14:30:00", "surprise", 0.80),
    ("2025-10-04 14:40:00", "neutral", 0.60),
    ("2025-10-04 14:50:00", "fear", 0.70)
]

cursor.executemany("INSERT INTO mood_log (timestamp, emotion, confidence) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()
print("✅ Sample data inserted")
