# News Scraping and Semantic Search Application

This project is a Streamlit application that allows users to scrape news articles from provided URLs, summarize them, and perform semantic searches on the stored articles. 

## Project Structure

```
news-scraping-app
├── src
│   ├── app.py                # Entry point of the Streamlit application
│   ├── scraping.py           # Functions for scraping news articles
│   ├── summarization.py       # Functions for summarizing articles
│   ├── vector_db.py          # Setup and querying of the vector database
│   └── utils.py              # Utility functions for managing URLs and other helpers
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd news-scraping-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Environment Setup

To run the project, you need to create a `.env` file in the root directory of the project. This file should contain the following credentials:

```
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_KEY=your_azure_openai_key
GPT_MODEL_NAME=your_gpt_model_name
GPT_API_VERSION=your_gpt_api_version
EMBEDDINGS_API_VERSION=your_embeddings_api_version
EMBEDDINGS_MODEL_NAME=your_embeddings_model_name
```

Replace `your_azure_openai_endpoint`, `your_azure_openai_key`, `your_gpt_model_name`, `your_gpt_api_version`, `your_embeddings_api_version`, and `your_embeddings_model_name` with your actual credentials.

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

## Features

- **Scraping**: Input a URL to scrape the headline and content of news articles.
- **Summarization**: Automatically generate summaries and identify main topics of the articles.
- **Semantic Search**: Search through the stored articles using a query to find relevant information.

## Demo
![Demo](https://github.com/anorboev3/news-scraping-app/blob/main/assets/demo.gif)
