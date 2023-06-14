from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/') #<----------- FLASK URL localhost
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST']) #<----------- FLASK URL process
def process_form():

    #Fetching the data from the HTML
    dropdown1 = request.form.get('dropdown1')
    dropdown2 = request.form.get('dropdown2')
    message_value = request.form.get('message')

    # print(dropdown1) #----------Uncomment this to check value inside -----------------Delete later
    
    #Putting data in one variable
    data = f"{message_value}\nCondition: {dropdown1}\nSeverity: {dropdown2}\n"

    print(data) #----------Uncomment this to check value inside -----------------Delete later


    #OpenAI
    Qn = "What should i do?"
    prompt = f"Q: {data+Qn}\nA:"

    response = requests.post(
            'https://api.openai.com/v1/engines/text-davinci-002/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + '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'
            },
            json={
                'prompt': prompt,
                'temperature': 0.7,
                'max_tokens': 100,
                'n': 1,
                'stop': None
            }
        )

        # Extract the response text from the OpenAI API response
    response_data = response.json()
    choices = response_data.get('choices')
    if choices and len(choices) > 0:
        response_text = choices[0].get('text', '').strip()
    else:
        response_text = "Sorry, I could not generate a response for your query."

    return jsonify({"response": response_text})

    # return f"Submitted Form: Name={name}, Email={email}"

if __name__ == '__main__':
    app.run(debug=True)


