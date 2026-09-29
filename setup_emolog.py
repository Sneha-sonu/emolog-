# EmoLog+ Setup and Installation Script
import os
import sys
import subprocess
import platform
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class EmoLogSetup:
    def __init__(self):
        self.required_packages = [
            "opencv-python==4.8.1.78",
            "matplotlib==3.7.2", 
            "pandas==2.0.3",
            "numpy==1.23.5",
            "SpeechRecognition==3.10.0",
            "pyttsx3==2.90"
        ]
        
    def check_python_version(self):
        version = platform.python_version()
        major, minor, _ = map(int, version.split('.'))
        if major < 3 or (major == 3 and minor < 8):
            return False, f"Python {version} - Requires 3.8+"
        return True, f"Python {version} ✓"
    
    def check_system(self):
        system = platform.system()
        return True, f"{system} ✓"
    
    def install_packages(self):
        results = []
        for package in self.required_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                results.append(f"✅ {package}")
            except subprocess.CalledProcessError:
                results.append(f"❌ {package}")
        return results

def run_setup():
    setup = EmoLogSetup()
    
    root = tk.Tk()
    root.title("EmoLog+ Setup")
    root.geometry("600x500")
    
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    ttk.Label(main_frame, text="EmoLog+ Installation", 
             font=("Arial", 16, "bold")).pack(pady=10)
    
    # System check
    check_frame = ttk.LabelFrame(main_frame, text="System Check", padding="10")
    check_frame.pack(fill=tk.X, pady=10)
    
    python_ok, python_msg = setup.check_python_version()
    system_ok, system_msg = setup.check_system()
    
    ttk.Label(check_frame, text=f"Python: {python_msg}").pack(anchor='w')
    ttk.Label(check_frame, text=f"System: {system_msg}").pack(anchor='w')
    
    # Installation progress
    progress_frame = ttk.LabelFrame(main_frame, text="Installation Progress", padding="10")
    progress_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    log_text = scrolledtext.ScrolledText(progress_frame, height=15)
    log_text.pack(fill=tk.BOTH, expand=True)
    
    def install():
        log_text.insert(tk.END, "🚀 Starting EmoLog+ installation...\n\n")
        log_text.insert(tk.END, "📦 Installing packages...\n")
        results = setup.install_packages()
        for result in results:
            log_text.insert(tk.END, f"  {result}\n")
        log_text.insert(tk.END, "\n🎉 Installation complete! You can now run EmoLog+\n")
        messagebox.showinfo("Success", "EmoLog+ installed successfully!")
    
    ttk.Button(main_frame, text="Install EmoLog+", command=install).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    run_setup()