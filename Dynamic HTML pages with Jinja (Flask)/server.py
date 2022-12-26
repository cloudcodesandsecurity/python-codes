from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


# https://genderize.io/
# https://api.agify.io?name=michael

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"
    gender_response = requests.get(gender_url)
    age_response =requests.get(age_url)
    gender_data = gender_response.json()
    age_data = age_response.json()
    gender = gender_data["gender"]
    age = age_data["age"]
    return render_template("index.html", person_name=name, gender=gender, age=age)


# npoint.io used to create json API
@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/d23dc3578c21e79ee3a5"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)