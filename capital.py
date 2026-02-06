from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("IBM_URL_END_POINT")
apikey = os.getenv("IBM_API_KEY")
username = os.getenv("WATSONX_USERNAME")
project_id = os.getenv("IBM_PROJECT_ID")

# testing
# model_id='ibm/granite-3-3-8b-instruct',
model_id = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"

credentials = Credentials(
    url=url,
    api_key=apikey,
)
print(credentials)
params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 100,
}
model = ModelInference(
    model_id=model_id, params=params, credentials=credentials, project_id=project_id
)
# granite_text = """
# Only reply with the answer. What is the capital of Canada?
# """

## adding special tokens to the prompt for better performance
# llama_text = """
# <|begin_of_text|><|start_header_id|>system<|end_header_id|>
# You are an expert assistant who provides concise and accurate answers.<|eot_id|>

# <|start_header_id|>user<|end_header_id|>
# What is the capital of Canada?<|eot_id|>

# <|start_header_id|>assistant<|end_header_id|>
# """
granite_specific_text = """
<|system|>
You are an expert assistant who provides concise and accurate answers.
<|user|>
What is the capital of France?
<|assistant|>
"""
print(model.generate(granite_specific_text)["results"][0]["generated_text"])
