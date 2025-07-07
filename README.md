# 🎬 YouTube AI Summarizer

<div align="center">

![YouTube AI Banner](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![AI Powered](https://img.shields.io/badge/AI-Powered-00D4AA?style=for-the-badge&logo=openai&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### 🚀 Transform YouTube videos into intelligent summaries with the power of AI

*Instantly extract key insights from any YouTube video using Google's Gemini AI*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-00a393.svg)](https://fastapi.tiangolo.com/)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 **Smart Summarization**
- Extract concise topics (5-6 words)
- Generate 2-3 sentence summaries
- Powered by Google Gemini 2.0 Flash

### 🔗 **URL Flexibility**
- Support for `youtube.com/watch?v=` URLs
- Support for `youtu.be/` short URLs
- Automatic video ID extraction

</td>
<td width="50%">

### ⚡ **Lightning Fast API**
- RESTful FastAPI endpoints
- Real-time processing
- Health check monitoring

### 🛡️ **Robust Error Handling**
- Graceful failure management
- Detailed error messages
- Transcript availability checks

</td>
</tr>
</table>

---

## 🎨 Demo

```bash
# Example API call
curl "http://localhost:8000/summarize?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Sample Response:**
```json
{
  "topic_name": "Music Video Classic Hit",
  "topic_summary": "A timeless music video featuring an iconic song that became an internet phenomenon. The video showcases classic 80s aesthetics with memorable choreography and has garnered billions of views worldwide."
}
```

---

## 🚀 Quick Start

### Prerequisites

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat&logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini_API-Key_Required-4285f4?style=flat&logo=google&logoColor=white)

</div>

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Abhirup0/yt-ai-summarizer-with-fast-api.git
cd yt-ai-summarizer-with-fast-api
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Key

> **⚠️ Security Notice:** Replace the hardcoded API key with environment variables in production!

Create a `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4️⃣ Run the Application

```bash
python app.py
```

🎉 **Your API is now running at:** `http://localhost:8000`

---

## 📚 API Documentation

### 🔍 **GET /summarize**

Extract and summarize YouTube video content.

**Parameters:**
- `url` (string, required): YouTube video URL

**Example Request:**
```http
GET /summarize?url=https://www.youtube.com/watch?v=VIDEO_ID
```

**Response Schema:**
```json
{
  "topic_name": "string (max 50 chars)",
  "topic_summary": "string (2-3 sentences)"
}
```

### 💚 **GET /health**

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "YouTube Summarizer"
}
```

---

## 🛠️ Technology Stack

<div align="center">

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) | High-performance API framework |
| **AI Engine** | ![Google](https://img.shields.io/badge/Gemini_2.0-4285F4?style=flat&logo=google&logoColor=white) | Advanced text summarization |
| **Transcript API** | ![YouTube](https://img.shields.io/badge/YouTube_API-FF0000?style=flat&logo=youtube&logoColor=white) | Video transcript extraction |
| **Language** | ![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=flat&logo=python&logoColor=white) | Core application logic |

</div>

---

## 📁 Project Structure

```
youtubeai/
├── 📄 app.py                 # Main FastAPI application
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # This beautiful file
├── 📁 __pycache__/          # Python cache files
└── 📄 .env                  # Environment variables (create this)
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
APP_HOST=0.0.0.0
APP_PORT=8000
MAX_TRANSCRIPT_LENGTH=3000
```

### API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file
4. **Never commit API keys to version control!**

---

## 🎯 Usage Examples

### Python Client Example

```python
import requests

def summarize_video(youtube_url):
    response = requests.get(f"http://localhost:8000/summarize?url={youtube_url}")
    return response.json()

# Usage
result = summarize_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print(f"Topic: {result['topic_name']}")
print(f"Summary: {result['topic_summary']}")
```

### JavaScript/Node.js Example

```javascript
const axios = require('axios');

async function summarizeVideo(youtubeUrl) {
    try {
        const response = await axios.get(`http://localhost:8000/summarize?url=${youtubeUrl}`);
        return response.data;
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// Usage
summarizeVideo('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    .then(result => {
        console.log(`Topic: ${result.topic_name}`);
        console.log(`Summary: ${result.topic_summary}`);
    });
```

---

## 🚦 Error Handling

The API provides comprehensive error handling for various scenarios:

| Error Type | Response |
|------------|----------|
| **Invalid URL** | `{"topic_name": "URL Error", "topic_summary": "Invalid YouTube URL format"}` |
| **No Transcript** | `{"topic_name": "Transcript Error", "topic_summary": "Could not fetch transcript..."}` |
| **API Failure** | `{"topic_name": "Processing Error", "topic_summary": "Failed to process video..."}` |

---

## 🔮 Future Enhancements

- [ ] 🌍 Multi-language transcript support
- [ ] 📊 Advanced analytics and insights
- [ ] 🎨 Custom summary templates
- [ ] 🔄 Batch processing capabilities
- [ ] 📱 Mobile app integration
- [ ] 🎭 Sentiment analysis
- [ ] 📈 Trending topics detection
- [ ] 🔐 User authentication
- [ ] 💾 Summary caching
- [ ] 📧 Email notifications

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **💻 Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **🚀 Push** to the branch (`git push origin feature/amazing-feature`)
5. **📥 Open** a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black app.py

# Lint code
flake8 app.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 YouTube AI Summarizer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Abhirup0/yt-ai-summarizer-with-fast-api&type=Date)](https://star-history.com/#Abhirup0/yt-ai-summarizer-with-fast-api&Date)

---

## �‍💻 About the Author

<div align="center">

**Abhirup Kumar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhirupk00)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abhirup0)

*Passionate about AI, Machine Learning, and building innovative solutions*

</div>

---

## �🙏 Acknowledgments

- **Google Gemini AI** - For providing powerful AI capabilities
- **YouTube Transcript API** - For seamless transcript extraction
- **FastAPI** - For the excellent web framework
- **The Open Source Community** - For continuous inspiration

---

<div align="center">

### 🎉 Made with ❤️ and lots of ☕

**If this project helped you, please consider giving it a ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/Abhirup0/yt-ai-summarizer-with-fast-api?style=social)](https://github.com/Abhirup0/yt-ai-summarizer-with-fast-api/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Abhirup0/yt-ai-summarizer-with-fast-api?style=social)](https://github.com/Abhirup0/yt-ai-summarizer-with-fast-api/network/members)

</div>

---

<div align="center">
  <sub>Built with 🚀 by developers, for developers</sub>
</div>
