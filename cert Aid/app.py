from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def calculate_teams(urgency, area, location):
    if location.lower() == "city":
        if urgency.lower() == "super urgent" and area <= 1:
            return 2
        elif urgency.lower() == "urgent":
            if area <= 1:
                return 2
            elif area <= 3:
                return 4
    elif location.lower() == "countryside" and urgency.lower() == "super urgent" and area <= 1:
        return 9

    return 0

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        urgency = request.form["urgency"]
        area = float(request.form["area"])
        location = request.form["location"]

        man_trail_dog_teams = calculate_teams(urgency, area, location)
        return render_template("result.html", man_trail_dog_teams=man_trail_dog_teams)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
