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
