from openai import OpenAI
from pydantic import BaseModel
import json

# Initialize OpenAI client that points to the local LM Studio server
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

# Define the conversation with the AI
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Create 1-3 fictional characters"}
]

# Define the expected response structure
response_format=CalendarEvent,

# Get response from AI
response = client.beta.chat.completions.parse(
    model="glm-4-9b-chat-1m",
    messages=messages,
    response_format=CalendarEvent,
)

# Parse and display the results
results = json.loads(response.choices[0].message.content)
print(json.dumps(results, indent=2))
