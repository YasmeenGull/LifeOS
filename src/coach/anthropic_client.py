import os

from dotenv import load_dotenv
from anthropic import Anthropic


load_dotenv()


class AnthropicCoachClient:
    """Handles Anthropic API communication."""

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is not set."
            )

        self.client = Anthropic(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        """Generate an LLM response."""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            temperature=0.4,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.content[0].text