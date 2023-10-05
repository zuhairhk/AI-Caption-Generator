from flask import Flask, render_template, request
import mp4totxt
import ai_gen

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    generated_caption = ""
    sys_instruct = "You are a social media platform's caption generator. I will give you text, you must reply with a related and relevant caption to be used from the transcribed video text. Use of a few emojis is encouraged."

    if request.method == 'POST':
        input_text = request.form['input_text']
        generated_caption = ai_gen.generate_caption(input_text, sys_instruct)

    return render_template('index.html', generated_caption=generated_caption)

if __name__ == "__main__":
    app.run(port=5001)
