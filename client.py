import os
from strands.models import BedrockModel
from mcp.client.streamable_http import streamable_http_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient

# Bedrock API key (bearer token) - boto3 picks this up automatically
os.environ["AWS_BEARER_TOKEN_BEDROCK"] = ""
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

bedrock_model = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    region_name="us-east-1",)


def create_streamable_http_transport():
    return streamable_http_client("http://34.228.80.70/mcp")

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

# Agent must be used INSIDE the context manager
with streamable_http_mcp_client:
    tools = streamable_http_mcp_client.list_tools_sync()
    print(f"Tools available: {tools}")
    agent = Agent(model=bedrock_model, tools=tools)    
    response = agent("add 10 and 20")
    print(response)
