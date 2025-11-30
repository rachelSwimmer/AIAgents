import asyncio
from agents import Agent, SQLiteSession, Runner, FunctionTool, function_tool

@function_tool
async def save_joke(joke: str) -> str:
    """Save the given dad joke because it was so funny

    Args:
        joke: The joke text
    """
    print("*** Funny joke detected, saving! ***")
    # In real life, we'd fetch the weather from a weather API
    with open('jokes.txt', 'a', encoding='utf8') as f:
        f.write(joke)
        f.write("\n\n")

    return "joke saved"

async def main() -> None:
    agent = Agent(
        name="Assistant",
        instructions="You are a mighty creator of dad jokes. save the really funny ones with your tool",
        tools=[save_joke],
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