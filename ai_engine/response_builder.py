import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def build_response(question, db_result):

    prompt = f"""
    A user asked the following question:

    {question}

    The database returned this result:

    {db_result}

    Explain the answer clearly for a car buyer.
    Show the best car and its details.

    Format like this:

    🚗 Best Car Based on Fuel Efficiency

    Model:
    Fuel Type:
    Mileage (MPG):
    Price:

    Then explain briefly why it is good.
    """

    response = model.generate_content(prompt)

    return response.text