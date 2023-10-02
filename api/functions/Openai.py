import openai
openai.api_key = "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"

def openaiResponse(prompt):
        
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": str(prompt)
            }
        ],
        ##max_tokens=100  # Usar max_tokens en lugar de maxTokens
    )

    return response