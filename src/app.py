import streamlit as st
from scraping import scrape_article
from summarization import summarize_and_identify_topics
from vector_db import setup_vector_database, search_query
from utils import add_url

# Initialize session state for URL list and vector database
if 'url_list' not in st.session_state:
    st.session_state.url_list = []
if 'vector_db' not in st.session_state:
    st.session_state.vector_db = None

st.title("News Scraping and Semantic Search App")

# URL input section
url_input = st.text_input("Enter URL", placeholder="Add a news article URL")
if st.button("Add URL"):
    updated_urls, _ = add_url(url_input, st.session_state.url_list)
    st.session_state.url_list = updated_urls
    st.success("URL added!")
    # Clear the URL input after adding
    st.session_state.url_input = ""

# Display the list of URLs
st.subheader("URL List")
st.write(st.session_state.url_list)

# Process URLs button
if st.button("Process URLs"):
    with st.spinner("Processing URLs..."):
        articles = []
        for url in st.session_state.url_list:
            # Returns the headline and content as a tuple
            headline, content = scrape_article(url)
            # Returns a concise summary of the article
            summary = summarize_and_identify_topics(content)
            articles.append({"url": url, "headline": headline, "content": content, "summary": summary})

        # Initializes or clears the vector database as needed
        setup_vector_database(articles)

    st.success("URLs processed and stored in vector database.")

# Query input section
query_input = st.text_input("Enter Query", placeholder="Enter your search query")
if st.button("Search"):
    # Returns search results filtered by similarity score
    results = search_query(query_input)
    st.subheader("Search Results")
    st.write(results)
