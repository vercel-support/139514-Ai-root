from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

# Set your OpenAI API key
openai.api_key = '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'

# Endpoint for generating a response
@app.route('/chat', methods=['POST'])
def chat():
    #return jsonify({'response': "OpenAI working Fine"})
    data = request.json  # JSON data containing the user's message
    # Get the user's message from the request data
    user_message = data['message']
    # Send the user's message to the OpenAI language model
    response = openai.Completion.create(
        engine='davinci',
        prompt=user_message,
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.7
    )
    # Get the model's response
    model_response = response.choices[0].text.strip()
    return jsonify({'response': model_response})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
