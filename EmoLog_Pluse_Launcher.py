# EmoLog+ Application Launcher
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

print("Loading EmoLog+ Launcher...")

class EmoLogPlusLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("EmoLog+ - Emotional Intelligence Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        self.setup_gui()
        
    def setup_gui(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#34495e', height=100)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="EmoLog+", 
                              font=("Arial", 28, "bold"), 
                              fg="#3498db", bg='#34495e')
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(header_frame, 
                                 text="AI-Powered Emotional Intelligence Assistant",
                                 font=("Arial", 12), 
                                 fg="#ecf0f1", bg='#34495e')
        subtitle_label.pack()
        
        # Main content
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Features
        features_frame = tk.LabelFrame(main_frame, text="Application Features", 
                                      font=("Arial", 12, "bold"),
                                      fg="#ecf0f1", bg='#34495e', bd=2)
        features_frame.pack(fill=tk.X, pady=10)
        
        features = [
            "🎭 Real-time Facial Emotion Detection",
            "🎤 Voice & Text Chat Interface", 
            "📊 Live Emotion Trend Analytics",
            "💾 Smart Mood Logging Database",
            "🤖 AI Emotional Support Chatbot"
        ]
        
        for feature in features:
            feature_label = tk.Label(features_frame, text=feature,
                                    font=("Arial", 10), anchor='w',
                                    fg="#bdc3c7", bg='#34495e')
            feature_label.pack(fill=tk.X, padx=10, pady=4)
        
        # Mode selection
        mode_frame = tk.LabelFrame(main_frame, text="Launch Mode", 
                                  font=("Arial", 12, "bold"),
                                  fg="#ecf0f1", bg='#34495e', bd=2)
        mode_frame.pack(fill=tk.X, pady=15)
        
        self.mode_var = tk.StringVar(value="full")
        
        modes = [
            ("🚀 Full Experience (Camera + Voice + Analytics)", "full"),
            ("💬 Text Chat Mode Only", "text"),
            ("📊 View Analytics Dashboard", "analytics"),
            ("🔧 Test Modules", "test")
        ]
        
        for text, mode in modes:
            tk.Radiobutton(mode_frame, text=text, variable=self.mode_var, 
                          value=mode, font=("Arial", 9), anchor='w',
                          fg="#ecf0f1", bg='#34495e', selectcolor='#2c3e50'
                          ).pack(fill=tk.X, padx=10, pady=2)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(fill=tk.X, pady=20)
        
        self.launch_btn = tk.Button(button_frame, text="🚀 LAUNCH EMLOG+", 
                                   font=("Arial", 12, "bold"),
                                   bg="#27ae60", fg="white", padx=20, pady=10,
                                   command=self.launch_app)
        self.launch_btn.pack(pady=10)
        
        # Status
        self.status_label = tk.Label(main_frame, text="Ready to launch EmoLog+", 
                                    font=("Arial", 10), fg="#95a5a6", bg='#2c3e50')
        self.status_label.pack(pady=10)
        
    def launch_app(self):
        mode = self.mode_var.get()
        self.status_label.config(text=f"Launching in {mode} mode...")
        
        try:
            if mode == "full":
                subprocess.Popen([sys.executable, "main.py"])
            elif mode == "text":
                subprocess.Popen([sys.executable, "main.py", "--text-chat"])
            elif mode == "analytics":
                if os.path.exists("file_graph.py"):
                    subprocess.Popen([sys.executable, "file_graph.py"])
                else:
                    messagebox.showinfo("Info", "Run main app first to collect data!")
            elif mode == "test":
                subprocess.Popen([sys.executable, "test_modules.py"])
                
            self.status_label.config(text="✅ EmoLog+ launched!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch:\n{e}")
            self.status_label.config(text="❌ Launch failed")

def main():
    root = tk.Tk()
    app = EmoLogPlusLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()