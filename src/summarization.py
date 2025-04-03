from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve env data from environment variables
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
subscription_key = os.getenv("AZURE_OPENAI_KEY")
gpt_model_name = os.getenv("GPT_MODEL_NAME")
gpt_api_version = os.getenv("GPT_API_VERSION")

# Configure Azure OpenAI client
client = AzureOpenAI(
    api_version=gpt_api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Function to summarize the content of an article and identify its topics
# Uses a summarization model to generate a concise summary
# Returns the summary as a string
def summarize_and_identify_topics(article_text):
    response = client.chat.completions.create(
        model=gpt_model_name,
        messages=[
            {"role": "system", "content": "Summarize the article and identify its main topics."},
            {"role": "user", "content": article_text}
        ],
        temperature=0.3
    )
    summary = response.choices[0].message.content
    return summary