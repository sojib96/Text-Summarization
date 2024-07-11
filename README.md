## Text Summarization 

### Introduction
**Text Summarization** is the process of condensing a text document to create a summary that retains the most important information. It is important because it helps in quickly understanding large volumes of text, saving time, and improving the efficiency of information retrieval.

### Project Overview
This project involves fine-tuning a Hugging Face model for text summarization. The backend is implemented with FastAPI, maintaining modular encoding and best practices, along with MLOps tools like Docker, GitHub, and CI/CD. The model used is **Google-Pegasus_Daily_CNN**, and the dataset is **SAMSUM**.

### Project Setup and Run Guidelines
1. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

2. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python app.py
    ```

4. **Open up the application**:
    - Navigate to `http://localhost:8080` in your browser.
    - If using for the first time, train the model using the `/train` route.
    - Once training is completed, use the `/predict` route for summarization.
