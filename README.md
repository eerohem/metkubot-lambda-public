AWS Lambda to receive and handle Slack slash commands and redirect them to OpenAI API.

Requirements:
- Slack app with webhooks attached to channels
- OpenAI API key
- Lambda layer with openai
    - pip install --upgrade openai --target /path/to/directory
    - zip the folder
    - upload it AWS Lambda layers with matching Python version (3.7.1 or above required for openai)
    - Attach layer to Lambda function and deploy

Usage:
- All Lambda functions that use OpenAI API need to have Lambda layer attached to them
- sendSlashcommandAck.py should be duplicated for each OpenAI API Lambda with different API gateways
    - This is done to ensure each slash command has a different event URL on Slack side