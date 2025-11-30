import asyncio
from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel
import os

async def main():
    agent = Agent(
        name="Assistant",
        model=LitellmModel(model="github/gpt-4.1", api_key=os.environ["GITHUB_TOKEN"]),
        instructions="You only respond in haikus.",
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())