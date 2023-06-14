Chatbot helpdesk.

Installation and workings.



Created a project called "helpdesk chatbot".

ADD file to the project
test.py
index2.html(templates file)



test.py file include:

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










index2.html file includes:

<!DOCTYPE html>
<html>
<head>
    <title>Chatbot</title>
    <style>
        .container {
            width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        select, textarea {
            width: 100%;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
            resize: vertical;
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form action="http://127.0.0.1:5000/process" method="POST">
        <h1>Welcome to the Chatbot Helpdesk</h1>
        <label for="dropdown1">Select Health Conditions</label>
        <select id="dropdown1" name="dropdown1">
            <option value="Poor">Poor</option>
            <option value="Healthy">Healthy</option>
            <option value="Neutral">Neutral</option>
        </select>

        <label for="dropdown1">Select Severity Level</label>
        <select id="dropdown2" name="dropdown2">
            <option value="Mild">Mild</option>
            <option value="Moderate">Moderate</option>
            <option value="Sever">Sever</option>
        </select>

        <label for="message">Send Message</label>
        <textarea id="message" name="message" rows="5"></textarea>


        <input type="submit" value="Submit">
    </form>
</body>
</html>



In terminal install 
"pip install python"
"pip install flask"
"flask --app test.py run"


Right Click on index2.html and select "reveal in File Explorer" and open index2 (chrome or edge)file.

On UI page select the conditons and severity levels.

write your query and submit.
