# 🎓 University AI Assistant

An end-to-end AI-powered system that answers questions about a university using web scraping, NLP, and Large Language Models (LLMs).

**The system is config-driven, allowing easy reuse for different universities by changing a single configuration file.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Example Queries](#example-queries)
- [Performance Notes](#performance-notes)
- [Known Limitations](#known-limitations)
- [Future Enhancements](#future-enhancements)
- [Academic Relevance](#academic-relevance)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🌟 Overview

University AI Assistant is a modular AI system that automatically scrapes official university websites, processes the data using NLP techniques, and generates human-like answers using Large Language Models.

The project demonstrates a real-world AI pipeline, combining data collection, information retrieval, and natural language generation.

---

## ✨ Key Features

### 🌐 Config-Driven Web Scraping
Automatically scrapes a university website and all internal sub-links using a centralized configuration file.

### 🧠 NLP Pipeline
- Intent Classification
- Named Entity Recognition (NER)

### 📚 Contextual Retrieval
TF-IDF–based document retrieval from scraped CSV data.

### 🤖 LLM Integration
Natural language answer generation using Hugging Face models.

### 🎨 Interactive UI
Streamlit-based web interface for user interaction.

### ⚙️ Modular Architecture
Clean separation between Scraper, NLP, LLM, and UI layers.

---

## 🏗️ Project Architecture

```
User
 ↓
Streamlit UI
 ↓
NLP Pipeline
  ├─ Intent Classification
  ├─ Named Entity Recognition (NER)
 ↓
Context Retrieval (CSV Data)
 ↓
Hugging Face LLM
 ↓
Generated Natural Language Answer
```

### Workflow Summary

1. User enters a query in the Streamlit UI
2. NLP pipeline identifies intent and key entities
3. Relevant content is retrieved from scraped CSV data
4. LLM generates a coherent natural language answer
5. Response is displayed to the user

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core language |
| **Requests, BeautifulSoup** | Web scraping |
| **Pandas, NumPy** | CSV data handling |
| **Scikit-learn** | TF-IDF & intent classification |
| **spaCy** | Named Entity Recognition |
| **Hugging Face Transformers** | LLM inference |
| **Streamlit** | Frontend UI |
| **tqdm** | Progress visualization |

---

## 📁 Folder Structure

```
university_ai_assistant/
│
├── config.py              # Central configuration (URL, limits, paths)
│
├── scraper/
│   ├── crawler.py         # Website crawler
│   ├── fetch.py           # HTML fetching
│   ├── parser.py          # Text & link extraction
│   ├── utils.py           # URL validation utilities
│   ├── storage.py         # CSV storage logic
│   └── __init__.py
│
├── nlp/
│   ├── pipeline.py        # Intent + NER pipeline
│   ├── load_data.py       # CSV loader
│   └── __init__.py
│
├── llm/
│   ├── generator.py       # Hugging Face LLM integration
│   └── __init__.py
│
├── data/
│   └── scraped_data.csv   # Scraped university data (CSV)
│
├── app.py                 # Streamlit UI
├── test.py                # Backend testing script
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/university-ai-assistant.git
cd university-ai-assistant
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## ⚙️ Configuration

### University Configuration

All environment-specific settings are located in **`config.py`**.

**Example:**
```python
BASE_URL = "https://riphah.edu.pk"
MAX_PAGES = 1000
OUTPUT_FILE = "data/scraped_data.csv"
```

### ➡ To switch to another university, only update `BASE_URL`.

**No other code changes are required.**

### Hugging Face API Setup

The system uses Hugging Face for LLM integration. Follow these steps:

1. Create a free account at [Hugging Face](https://huggingface.co/)
2. Generate an API Token from your account settings
3. Set the token as an environment variable:

**Windows (PowerShell):**
```powershell
$env:HUGGINGFACE_API_TOKEN="hf_YourTokenHere"
```

**Linux / macOS:**
```bash
export HUGGINGFACE_API_TOKEN="hf_YourTokenHere"
```

This allows the system to securely access the Hugging Face API without hardcoding credentials.

---

## ▶️ Running the Application

### 1. Run Web Scraper

```bash
python scraper/crawler.py
```

This generates:
```
data/scraped_data.csv
```

### 2. Test Backend Pipeline

```bash
python test.py
```

**Example Output:**
```
Intent: ADMISSION
Entities: BS Computer Science
Answer: The admission requirements for BS Computer Science include...
```

### 3. Run Streamlit UI

```bash
streamlit run app.py
```

Open browser at: **http://localhost:8501**

---

## 💬 Example Queries

- What are the admission requirements for BS Computer Science?
- What programs are offered by the Faculty of Computing?
- What is the fee structure for undergraduate programs?
- Tell me about MS Computer Science.
- What are the eligibility criteria for PhD admission?

---

## ⚡ Performance Notes

- **LLM inference on CPU is slow** (expected behavior)
- **First query takes longer** due to model loading
- **For production use:**
  - GPU deployment recommended
  - Hugging Face Inference API can be used
  - Smaller models can reduce latency

---

## ⚠️ Known Limitations

- CPU-only inference causes slow responses
- Ambiguous queries may return generalized answers
- Data freshness depends on scraper reruns
- English language support only

---

## 🔮 Future Enhancements

- [ ] GPU-based inference
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Multilingual support (Urdu / English)
- [ ] Voice-based interface
- [ ] Multi-university support
- [ ] Real-time scraping updates
- [ ] User feedback & rating system

---

## 🎓 Academic Relevance

This project demonstrates:

- Practical application of AI in education
- Integration of web scraping, NLP, and LLMs
- Clean, modular, and reusable architecture
- Industry-relevant design principles

**Suitable for:**
- Final Year Projects (FYP)
- Academic demonstrations
- Research prototypes

---

## 📄 License

This project is intended for **academic and educational use only**.

---

## 🙏 Acknowledgments

- Open-source NLP & AI community
- Hugging Face ecosystem
- Streamlit framework

---

**Made with ❤️ for advancing AI in Education**
