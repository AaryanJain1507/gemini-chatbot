# 💬 Gemini Chatbot (Google Generative AI)

This is a simple terminal-based chatbot built using **Google's Gemini 1.5 Flash model** via the Generative Language API. It supports two modes:

- 🔁 Chat without memory (responds to each prompt individually)
- 🧠 Chat with memory (retains context across turns)

---

## 📁 Project Structure

chatbot/
├── connecting_gpt.py # Main chatbot logic
├── .env # API key file (not pushed to GitHub)
├── llm_env/ # Local Python virtual environment (ignored)
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Requirements

- Python 3.8+
- `requests`
- `python-dotenv`

Install dependencies using:

```bash
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install requests python-dotenv
🔐 Setup: Environment Variables
Create a .env file in the same directory with your Google API key:

ini
Copy
Edit
GEMINI_API_KEY=your_google_gemini_api_key_here
Note: Your key is safe because .env is excluded via .gitignore.

🚀 How to Run
bash
Copy
Edit
python connecting_gpt.py
You will be prompted to choose:

yaml
Copy
Edit
Choose Mode:
1. No Memory Chat
2. Memory Chat
Enter 1 or 2:
Type your input and chat away! Type exit to end the chat session.

🧠 Chat Modes
No Memory Mode: The bot replies to each message independently.

Memory Mode: The bot maintains a conversational history, simulating context-aware chat.

📌 Notes
The script uses gemini-1.5-flash model for fast responses.

.env and llm_env/ are excluded from version control using .gitignore.

📄 License
This project is for educational purposes. Review Google's Generative Language API terms of use before deploying commercially.

🙋‍♂️ Author
Aaryan Jain
GitHub Profile

yaml
Copy
Edit

---

Let me know when you’re ready for a `requirements.txt` or `.gitignore` too.
