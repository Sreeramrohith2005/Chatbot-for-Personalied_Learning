# Chatbot-for-Personalied_Learning

This project integrates the **Google Gemini API** with a Rasa chatbot to fetch and provide course-related information based on user queries. The action, `ActionGetCourseInfo`, processes the user's input, interacts with the Gemini API, and returns the generated content to the user.

## Requirements

- Python 3.7+
- Rasa SDK
- `google-generativeai` Python package
- A valid API key for Google Gemini API

## Installation

1. **Install Python dependencies**:

   Create a virtual environment and activate it (if not already done):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install required Python packages**:

   You need to install the following packages:

   ```bash
   pip install rasa-sdk google-generativeai
   ```

3. **Set up the Gemini API**:

   - Ensure you have a valid Gemini API key. You can obtain the API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Replace the `api_key` in the `ActionGetCourseInfo` class with your valid API key.

4. **Configure API key in your environment** (optional, if you're using environment variables):

   ```bash
   export GOOGLE_API_KEY="your-api-key-here"  # On Windows: set GOOGLE_API_KEY="your-api-key-here"
   ```

## Usage

1. **Add the action to your Rasa project**:

   - Add the `ActionGetCourseInfo` class to your `actions.py` file.
   - Make sure the `google-generativeai` package is correctly imported.
   
2. **Configure the action in your `domain.yml`**:

   Add the following to your `domain.yml` under `actions`:

   ```yaml
   actions:
     - action_get_course_info
   ```

3. **Update your stories or rules**:

   Create a story or rule that triggers the `action_get_course_info` action based on user input. Example:

   ```yaml
   stories:
     - story: user asks for courses
       steps:
         - intent: ask_courses
         - action: action_get_course_info
   ```

4. **Test the action**:

   - Start your Rasa action server:

     ```bash
     rasa run actions
     ```

   - Interact with your Rasa bot, and test the action by asking course-related questions.

## Code Explanation

- **ActionGetCourseInfo**: This custom action sends the user's query to the Google Gemini API using the `google.generativeai` Python package.
- **API key**: The API key for Google Gemini API is provided directly in the code or fetched from the environment variables.
- **Model**: The action uses the `gemini-1.5-flash` model to generate content based on the user’s query.
- **Response**: The response from the API is parsed, and the content is returned as a message to the user.

## Troubleshooting

- **API Key Issues**: Ensure that the API key is valid and has appropriate access to the Gemini API.
- **Error Handling**: If the API returns an error or unexpected response, check the full response by logging `response` to diagnose the issue.
- **Missing content**: If the `response.text` is empty or null, verify that the Gemini API is returning valid data based on the query. You can also inspect the response object for any error messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
