from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_data = Post()


@app.route('/')
def get_all_posts():
    return render_template("index.html", data=blog_data.blog())


@app.route("/post/<int:index>")
def show_post(index):
    return render_template("post.html", data=blog_data.blog(), index=index)


if __name__ == "__main__":
    app.run(debug=True)
