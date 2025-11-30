import asyncio
from agents import Agent, run_demo_loop

async def main() -> None:
    agent = Agent(
        name="Assistant",
        instructions="You are a mighty creator of dad jokes",
        model="gpt-4.1-mini",
    )

    await run_demo_loop(agent)

if __name__ == "__main__":
    asyncio.run(main())