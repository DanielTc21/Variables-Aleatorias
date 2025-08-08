from src.custom_model import CustomChatOpenAI
from config.config import Config

class LLMManager:
    """Manager for handling interactions with ChubbGPT."""
    def __init__(self, tools=[], model = 'api_openai_gpt_4o_g'):
        """Initialize the LLMManager with tools.

        Args:
            tools (list): A list of tools to bind to the custom model.
        """
        self.model = CustomChatOpenAI(model_name=Config.MODEL_NAME, 
                                     openai_api_key=Config.OPENAI_API_KEY, 
                                     temperature=Config.TEMPERATURE)

    def invoke_model(self, messages):
        """Invoke the model with the input message.

        Args:
            messages: message to send to the model.

        Returns:
            Response from the model.
        """
        response = self.model.invoke(messages)
        return response
    
 