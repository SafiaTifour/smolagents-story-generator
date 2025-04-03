from smolagents import CodeAgent, Tool, DuckDuckGoSearchTool, LiteLLMModel
from config import GEMINI_MODEL_ID, IMAGE_GEN_TOOL_SPACE

# Initialize AI Agents
story_planner = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=LiteLLMModel(model_id=GEMINI_MODEL_ID)
)

story_writer = CodeAgent(
    model=LiteLLMModel(model_id=GEMINI_MODEL_ID),
    tools=[]
)

story_illustrator = CodeAgent(
    model=LiteLLMModel(model_id=GEMINI_MODEL_ID),
    tools=[]
)

# Image Generation Tool
image_generation_tool = Tool.from_space(
    IMAGE_GEN_TOOL_SPACE,
    name="image_generator",
    description="Generate an image from a prompt"
)

image_generator = CodeAgent(
    model=LiteLLMModel(model_id=GEMINI_MODEL_ID),
    tools=[image_generation_tool]
)
