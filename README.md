# 🐑 Sheep A.I – Your Personal Voice-Activated Desktop Assistant

Welcome to **Sheep A.I**, a voice-controlled smart assistant built in Python that lives right on your desktop. It opens apps & websites, tells you the weather, date & time, and even answers general questions using AI. All powered by your voice. 🎤💻

---

## 🚀 Features

🎯 Voice-Activated Commands  
📂 Opens Desktop Apps (like Notepad, Minecraft, etc.)  
🌐 Launches Popular Websites (YouTube, GitHub, LinkedIn, etc.)  
📅 Tells Current Date & Time  
🌦️ Fetches Real-Time Weather Based on Location (via IP + OpenWeatherMap API)  
🧠 AI-Generated Responses via OpenRouter (ChatGPT-3.5)  
🗣️ Fully Text-to-Speech Interactive Interface  
🧼 Clean OOP-based Structure  
💻 100% Python CLI App – No GUI Needed

---

## 🛠️ Tech Stack

- **Python 3.10+**
- `pyttsx3` – Offline Text to Speech Engine  
- `SpeechRecognition` – Voice Input Recognition  
- `webbrowser`, `os` – For App/Site Opening  
- `requests` – API Calls (OpenWeatherMap + OpenRouter)  
- `datetime` – For Current Date/Time Handling

---

## 🔐 API Keys Required

You'll need:

- [OpenWeatherMap API Key](https://openweathermap.org/)
- [OpenRouter API Key](https://openrouter.ai/)

📌 **Note**: The default keys in the script are for testing/demo — please generate and use your own for production.

---

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/sheep-ai.git
cd sheep-ai
