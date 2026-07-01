class BaseAgent:

    def __init__(self, name):
        self.name = name

    def analyze(self):
        return f"{self.name} is analyzing Base ecosystem"


agent = BaseAgent("Base AI Agent")

print(agent.analyze())