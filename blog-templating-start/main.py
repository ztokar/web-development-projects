from flask import Flask, render_template
import requests
from post import Post



posts=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

all_posts=[]
for post in posts:
    post_obj=Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=all_posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
