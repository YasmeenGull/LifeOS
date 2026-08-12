import os

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()


class AnthropicCoachClient:
    """Handles Anthropic API communication for LifeOS."""

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is not set."
            )

        self.model = os.getenv(
            "ANTHROPIC_MODEL",
            "claude-sonnet-4-5"
        )

        self.client = Anthropic(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        """Generate an LLM response using Anthropic."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=0.4,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text