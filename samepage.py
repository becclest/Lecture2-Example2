from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return "Here's the main page. <a href='http://localhost:5000/seeform'>Click here to see the form</a>."


@app.route('/seeform', methods=["GET", "POST"])
def see_form():
    formstring = """<br><br>
    <form action="" method='POST'>
    <input type="text" name="phrase"> Enter a phrase: <br>
    <input type="submit" value="Submit">
    </form>
"""  # HINT: In there ^ is where you need to add a little bit to the code...
    if request.method == "POST":
        return formstring + "<br><br>{}".format(request.form.get('phrase', ''))
        # Add more code here so that when someone enters a phrase, you see their data (somehow) AND the form!
    else:
        return formstring


if __name__ == "__main__":
    app.run(debug=True)
