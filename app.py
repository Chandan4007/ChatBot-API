from flask import Flask, request, render_template
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    openai.api_key = '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'
    quest = request.form['name']
    prompt = quest
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = completions.choices[0].text
    print(type(answer),">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Bot-------------------: " + answer)
    return render_template('index.html', r_answer=answer)

if __name__ == '__main__':
    app.run(debug=True)