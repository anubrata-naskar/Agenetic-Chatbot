# 🤖 Agenetic-Chatbot

An intelligent AI chatbot built with **LangGraph** and **Streamlit**, featuring persistent conversation history and advanced memory management. Experience ChatGPT-like functionality with Google's Gemini model.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-0.5+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Key Features

### 🧠 **Advanced AI Conversations**
- Powered by **Google Gemini-1.5-Flash** model
- Context-aware responses with full conversation memory
- Natural language understanding and generation
- Configurable temperature and token limits

### 💾 **Persistent Chat History**
- All conversations automatically saved to `conversations.json`
- Resume previous chats exactly where you left off
- Chat history persists between app sessions
- Thread-based memory management using LangGraph checkpointer

### 📱 **Modern Web Interface**
- Clean, responsive Streamlit UI
- Left sidebar for conversation navigation
- Real-time chat interface with typing indicators
- Custom theme with configurable colors

### 🗂️ **Smart Conversation Management**
- Create unlimited new chat threads
- Switch between conversations seamlessly
- Auto-generated conversation titles
- Delete unwanted conversations
- Timestamp tracking for all chats

### 🔒 **Privacy & Local Storage**
- All data stored locally in JSON format
- No external database required
- Your conversations stay on your machine
- Secure API key management via environment variables

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** installed on your system
- **Google AI API Key** (Get one [here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd Agenetic-Chatbot
```

2. **Set up virtual environment**
```bash
# Create virtual environment
python -m venv myenv

# Activate it
# Windows:
myenv\Scripts\activate
# macOS/Linux:
source myenv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

5. **Run the application**
```bash
streamlit run frontEnd.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 📖 How to Use

### Starting Your First Chat
1. 🌐 Open the application in your browser
2. ➕ Click "New Chat" in the sidebar to create a conversation
3. 💬 Type your message in the chat input at the bottom
4. ⚡ Press Enter and get instant AI responses

### Managing Conversations
- **➕ New Chat**: Start a fresh conversation thread
- **📋 Switch Chats**: Click any conversation in sidebar to resume
- **🗑️ Delete**: Remove unwanted conversations  
- **💾 Auto-Save**: All messages save automatically as you chat
- **📱 Responsive**: Works on desktop, tablet, and mobile

### Advanced Features
- **🧠 Memory**: Each conversation remembers its full context
- **🔄 Persistence**: Close the app and reopen - your chats are still there
- **📊 Organization**: Conversations show titles and timestamps
- **⚙️ Customization**: Modify AI behavior and UI theme

## 🏗️ Project Architecture

### Core Components

#### Backend (`backEnd.py`)
```python
# LangGraph-based conversation engine
- StateGraph for message flow management
- ChatGoogleGenerativeAI for AI responses  
- MemorySaver for conversation persistence
- TypedDict for type-safe message handling
```

#### Frontend (`frontEnd.py`)
```python
# Streamlit web application
- Conversation management functions
- JSON-based local storage
- Session state management
- Real-time chat interface
```

#### Notebook (`chat.ipynb`)
```python
# Interactive development environment
- Jupyter notebook for testing
- Step-by-step chatbot development
- Direct Python interaction mode
```

### File Structure
```
Agenetic-Chatbot/
├── 📄 frontEnd.py           # Main Streamlit web application
├── 🔧 backEnd.py            # LangGraph chatbot logic
├── 📓 chat.ipynb            # Jupyter notebook for development
├── 📋 requirements.txt      # Python dependencies
├── 🗄️ conversations.json    # Auto-generated chat storage
├── 🔐 .env                  # Environment variables (create this)
├── ⚙️ .streamlit/
│   └── config.toml         # UI theme configuration
├── 📁 myenv/               # Virtual environment (auto-created)
├── 📜 .gitignore           # Git ignore rules
└── 📖 README.md            # This documentation
```

## ⚙️ Configuration

### AI Model Settings
Edit `backEnd.py` to customize AI behavior:
```python
chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",    # Model version
    temperature=0.7,             # Creativity (0.0-1.0)
    max_tokens=1000             # Response length limit
)
```

### UI Theme Customization
Modify `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"              # Accent color
backgroundColor = "#FFFFFF"            # Main background
secondaryBackgroundColor = "#F0F2F6"   # Sidebar background
textColor = "#262730"                  # Text color

[server]
port = 8501                           # Server port
```

### Conversation Storage Format
Data is stored in `conversations.json`:
```json
{
  "chat_20250805_143022": {
    "messages": [
      {"role": "user", "content": "Hello!"},
      {"role": "assistant", "content": "Hi! How can I help you today?"}
    ],
    "timestamp": "2025-08-05T14:30:22.123456",
    "title": "Hello!"
  }
}
```

## 🛠️ Development

### Running in Development Mode
```bash
# Install all dependencies including dev tools
pip install -r requirements.txt

# Run with auto-reload enabled
streamlit run frontEnd.py --server.runOnSave true

# Format code
black frontEnd.py backEnd.py

# Check code quality  
flake8 frontEnd.py backEnd.py
```

### Using the Jupyter Notebook
```bash
# Start Jupyter server
jupyter notebook

# Open chat.ipynb for interactive development
# Test individual components step by step
# Experiment with different AI parameters
```

### Testing Conversation Memory
```python
# Test thread-based memory in Python
from backEnd import chatbot

config = {'configurable': {'thread_id': 'test_thread'}}
response = chatbot.invoke({'messages': [HumanMessage(content="My name is John")]}, config)
# The bot will remember "John" in subsequent messages with the same thread_id
```

## 🔍 Troubleshooting

### Common Issues & Solutions

**🚫 App won't start**
```bash
# Check Python version
python --version  # Should be 3.8+

# Verify dependencies
pip install -r requirements.txt

# Check API key
echo $GOOGLE_API_KEY  # Should show your key
```

**💾 Conversations not saving**
- Check write permissions in project directory
- Ensure `conversations.json` can be created/modified
- Verify no antivirus blocking file operations

**🧠 Memory issues**
- Each conversation uses its own `thread_id`
- MemorySaver is initialized in `backEnd.py`
- Check console for LangGraph error messages

**🎨 UI problems**
- Clear browser cache and refresh
- Try different browser (Chrome, Firefox, Safari)
- Check browser console for JavaScript errors
- Verify Streamlit version compatibility

**🔑 API errors**
- Verify Google API key is valid
- Check API quota and usage limits
- Ensure internet connection is stable
- Test API key with simple request

### Debug Mode
Enable detailed logging:
```bash
# Run with debug output
streamlit run frontEnd.py --logger.level debug

# Check terminal output for detailed error messages
```

## 🚀 Deployment Options

### Local Development
```bash
streamlit run frontEnd.py
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "frontEnd.py", "--server.address", "0.0.0.0"]
```

### Cloud Deployment
- **Streamlit Cloud**: Connect your GitHub repo
- **Heroku**: Use Procfile with `web: streamlit run frontEnd.py`
- **AWS/GCP**: Deploy using container services

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature-amazing-feature`
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Test new features thoroughly
- Update documentation as needed

## 📊 Technical Specifications

### Dependencies
- **Core**: LangGraph 0.5+, LangChain 0.3+, Streamlit 1.28+
- **AI Model**: Google Generative AI with Gemini-1.5-Flash
- **Memory**: LangGraph MemorySaver for conversation persistence
- **Storage**: Local JSON file storage
- **UI**: Streamlit with custom theme support

### Performance
- **Response Time**: ~1-3 seconds per message
- **Memory Usage**: ~50-100MB per conversation thread
- **Storage**: ~1KB per message in JSON format
- **Concurrent Users**: Supports multiple browser sessions

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[LangChain](https://langchain.com/)** & **[LangGraph](https://langchain.com/langgraph)** - Powerful conversation framework
- **[Google AI](https://ai.google.dev/)** - Gemini model API and documentation  
- **[Streamlit](https://streamlit.io/)** - Excellent web framework for Python
- **Python Community** - Amazing ecosystem of open-source tools

## 📞 Support & Community

**Need Help?**
1. 📚 Check this README for common solutions
2. 🐛 Search existing [GitHub Issues](../../issues)
3. 💬 Create a new issue with detailed information
4. 📧 Contact the maintainers

**Show Your Support**
- ⭐ Star this repository if you find it helpful
- 🐛 Report bugs and suggest improvements
- 📢 Share with others who might benefit

---

**🎉 Happy Chatting!**

*Built with ❤️ using Python, LangGraph, Streamlit, and Google AI*

> **Note**: This is an open-source project. Contributions, issues, and feature requests are welcome!