from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel

gemini = Agent(
    name="Assistant",
    instructions="You are a mighty creator of dad jokes",
    model=LitellmModel(model="gemini/gemini-2.5-flash", api_key="AIzaSyCvhxmpvBGoR0L4k5flSmR_ONS1jAgAiQM")
)

result = Runner.run_sync(gemini, "Write a random dad joke")
print(result.final_output)