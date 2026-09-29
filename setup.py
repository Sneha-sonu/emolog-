from setuptools import setup, find_packages

setup(
    name="emotion_chatbot",
    version="1.0",
    packages=find_packages(),

    install_requires=[
        "numpy==1.23.5",
        "pandas==2.0.3",
        "scikit-learn==1.3.0",
        "SpeechRecognition==3.10.0",
        "pyttsx3==2.90",
        "opencv-python==4.8.1.78"
    ],

    entry_points={
        "console_scripts": [
            "emotion-chatbot=main:main"
        ]
    },

    python_requires=">=3.11",

    description="A real-time emotion detection chatbot application",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)