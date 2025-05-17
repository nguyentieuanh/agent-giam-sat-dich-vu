from langchain_google_genai import ChatGoogleGenerativeAI
from dconfig import config_key

google_api_key = config_key.GEMINI_KEY_API

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=google_api_key)
