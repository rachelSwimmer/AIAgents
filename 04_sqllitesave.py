import asyncio
from agents import Agent, SQLiteSession, Runner

async def main() -> None:
    agent = Agent(
        name="Assistant",
        instructions="You are a mighty creator of dad jokes",
        model="gpt-4.1-mini",
    )
    session = SQLiteSession("user_123", "conversations.db")

    while True:
        next_line = input('> ')
        result = await Runner.run(
            agent,
            next_line,
            session=session
        )
        print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())