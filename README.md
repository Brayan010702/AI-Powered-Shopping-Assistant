# 🧠 LLM Agents Final Project

## 🛍️ AI-Powered Shopping Assistant

An **AI-driven shopping assistant** designed to enhance customer experience and optimize e-commerce operations using **Large Language Models (LLMs)**.  
This system enables natural language interaction for product discovery, cart management, and automated customer support, while reducing human workload and maintaining high-quality service.  

---

## 🚀 Overview  

The project simulates the development of an intelligent shopping assistant for a major e-commerce company.  
It aims to:  

- Improve **customer experience** through conversational product search and personalized recommendations.  
- Increase **operational efficiency** by automating common support interactions.  

The assistant can handle real-world scenarios such as:  

- Searching for “healthy breakfast options.”  
- Adding or removing items from the shopping cart.  
- Requesting refunds or reporting defective products.  
- Maintaining multi-turn conversation context and escalating complex issues to human support when needed.  

---

## 🧩 Data  

The assistant is powered by a **grocery store dataset** containing:  

- **49,000+ products** with names, departments, aisles, and prices.  
- **Historical order data** reflecting customer purchase behavior.  

The system uses:  

- **Structured search** (SQL-like filtering) for precise product queries.  
- **Semantic search** (via embeddings) to interpret natural language queries.  
- **Session memory** to maintain user context and cart state across conversations.  

---

## ⚙️ Tech Stack  

| Component | Description |
|------------|-------------|
| **Python** | Main programming language |
| **LangChain** | LLM integration and tool management |
| **LangGraph** | Conversation flow orchestration |
| **OpenAI GPT** | Natural language understanding and reasoning |
| **Chroma** | Vector database for semantic product search |
| **HuggingFace** | Text embeddings for semantic similarity |
| **Pandas** | Data manipulation and filtering |
| **Pydantic** | Data validation and schema definition |
| **Streamlit** | Web-based chat interface |
| **Pytest** | Unit and integration testing |

---

## 🧰 Installation  

### Prerequisites  

- Python 3.10+  
- OpenAI API key (or other model provider)  
- Git  

### Setup  

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-shopping-assistant.git
cd llm-shopping-assistant

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # (Mac/Linux)
venv\Scripts\activate       # (Windows)

# Install dependencies
pip install -r requirements.txt

# Configure your API key
export OPENAI_API_KEY="your-api-key-here"
```

## 🧮 Running the Application  

### 🧠 Command Line  

```python
from src.conversation_runner import run_single_turn

result = run_single_turn("Hi, I need some bananas", "test-thread-123")
print(result)
```

### 💬 Web Interface

```python
streamlit run app.py
```

Access the interactive web app to chat with the assistant, explore conversation flows, and test cart management in real time.

### 🧪 Testing

Run all tests to ensure functionality and consistency:

```python
pytest tests/
```

### 📊 Summary

This project demonstrates how to integrate LLMs, embeddings, and structured data processing to build a functional AI agent capable of:

- Natural and contextual conversation.
- Dynamic cart and session management.
- Real-time decision-making and response generation.

These components represent the foundation for next-generation AI-powered customer experiences.
