import google.generativeai as genai
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetCourseInfo(Action):
    def name(self) -> Text:
        return "action_get_course_info"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        user_query = tracker.latest_message.get("text")

        # Configure the API with the key
        genai.configure(api_key="AIzaSyDFO4j-Id3ngyVpWaSL41kkWits1xtYoFI")  # Replace with your actual API key

        try:
            # Initialize the Gemini model
            model = genai.GenerativeModel("gemini-1.5-flash")

            # Generate the content based on user query
            response = model.generate_content(user_query)

            # Extract the response text from the generated content
            llm_response = response.text if response.text else "Sorry, no content was returned."

        except Exception as e:
            llm_response = f"Sorry, there was an error processing your request: {str(e)}"

        dispatcher.utter_message(text=llm_response)
        return []
