from agents import Agent, Runner

agent = Agent(name="Assistant",model="gpt-5-mini", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)