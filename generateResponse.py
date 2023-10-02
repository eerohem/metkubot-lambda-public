__author__      = "Eero Hemminki"
__copyright__   = "Copyright 2023"
__credits__     = ["Eero Hemminki, Metropolia UAS Student Union METKA"]
__license__     = "GPL"
__version__     = "1.0.1"
__maintainer__  = "Eero Hemminki"
__email__       = "eero.hemminki@metkaweb.fi"

import json
import urllib.parse
import os
import base64
import openai
import requests

# Fetch the URL from environment variables
url = os.getenv('yourSlackChannelWebhookVariable')

def lambda_handler(event, context):
    # Log the received event for debugging
    print(f"Received event: {json.dumps(event, indent=2)}")
    
    # Slack slash commands send a set of URL parameters encoded in base64
    # The following is to parse the parameters for future use. 
    commandBody_b64 = event['body']
    commandBody = base64.b64decode(commandBody_b64).decode('utf-8')
    
    # Parse the URL-encoded body
    key_values = urllib.parse.parse_qs(commandBody)
    
    # Safely get the first element of each list, if exists
    user_id = key_values.get('user_id', ['Not Found'])[0]
    user_name = key_values.get('user_name', ['Not Found'])[0]
    text = key_values.get('text', ['Not Found'])[0]
    channel_id = key_values.get('channel_id', ['Not Found'])[0]
    
    print(f"user_id: {user_id}")
    print(f"user_name: {user_name}")
    print(f"text: {text}")
    print(f"channel_id: {channel_id}")
    
    # Full list of models available, see https://platform.openai.com/docs/models/overview
    model_to_use = "gpt-3.5-turbo"
    input_prompt = text

    # Fetch the API key from environment variables
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    try:
        response = openai.ChatCompletion.create(
            model=model_to_use,
            messages=[{"role": "user", "content": input_prompt}]
        )
    except Exception as e:
        print(f"OpenAI API call failed: {e}")
        return
    
    text_response = "<@" + user_id + "> " + text + "\n\n" + response.choices[0].message.content
    payload = {'text': text_response}
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Slack post failed: {e}")
