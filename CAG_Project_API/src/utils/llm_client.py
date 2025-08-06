import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv(find_dotenv())

def get_llm_response(context: str, query: str) -> str:
    """
     Send a user query and context to Google Gemini and return the assistant's nse.

    Args:
        context (str): Background information delimited by triple backticks.
        query (str): The user's question to be answered based on the context.

    returns:
        str: The assistant's generate text response.

    Raises:
        ValueError: if thr GEMINI_API_KEY env variable is not set. 

    """
    # Ensure the GEMINI_API_KEY is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set in .env file.")

    # Configure the Gemini client
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    # Full prompt with embedded context
    prompt = (
        "You are a helpful assistant that can answer questions based on the provided context, which is delimited "
                "with triple backticks.\n\n"
                "You will be given a context and a user query. Your task is to generate a response that is "
                "relevant to the query based on the context provided. If the context does not contain enough "
                "information to answer the query, you should indicate that you do not have enough information "
                "to provide a complete answer.\n\n"
                "If the context is empty, you should respond with a message indicating that there is not "
                "enough information to answer the query.\n\n"
                "You should always respond in a friendly and helpful manner and you should not include "
                "personal opinions or information in your responses.\n\n"
                f"Context:\n```{context}```"
                f"User Query:\n{query}"
    )

    try:
        # Generate response (non-streaming, to simplify)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error from Gemini: {str(e)}"
