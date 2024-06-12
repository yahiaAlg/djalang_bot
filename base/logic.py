import time
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

CHROMA_DB_DIRECTORY = "chroma_db/ask_bootstrap_docs"


def build_database():
    time.sleep(1)
    print("building completed!")


def answer_query(query):
    print(f"entering the chat with the query {query}")
    chat = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)  # type: ignore

    result = chat.invoke(query)

    # Assuming result.content is a complex object, convert it to a dictionary
    result_dict = {
        "content": result.content,
        # include other necessary attributes here
    }

    return result_dict
