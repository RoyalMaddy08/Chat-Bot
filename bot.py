import openai
import os


openai.api_key = 'your_api_key'

def get_chatbot_response(user_input, conversation_history):

    conversation_history.append(f"You: {user_input}")

    response = openai.Completion.create(
        model='text-davinci-002',
        prompt="\n".join(conversation_history),

        temperature = 0
    )

    reply = response['choices'][0]['text']
    conversation_history.append(f"ChatGPT: {reply}")
    return reply, conversation_history


conversation_history = []

while True:
    user_input = input("You: ")


    if user_input.lower() == 'exit':
        break


    chatbot_reply, conversation_history = get_chatbot_response(user_input, conversation_history)


    print(f"ChatGPT: {chatbot_reply}")
