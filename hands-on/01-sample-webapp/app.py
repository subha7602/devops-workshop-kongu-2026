from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Spidey DevOps App</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: #202124;
      color: #fff;
      font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
      text-align: center;
    }
    h1 {
      font-size: 1.8rem;
      margin-bottom: 1rem;
    }
    img {
      width: 220px;
    }
    .quote {
      margin-top: 1rem;
      max-width: 24rem;
      font-style: italic;
      color: #ffd400;
    }
  </style>
</head>
<body>
  <h1>Hello, this is a web app!</h1>
  <img src="{{ spidey_gif }}" alt="Spider-Man">
  <p class="quote">&ldquo;With great power comes great responsibility.&rdquo;<br>&mdash; Uncle Ben</p>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HOME_HTML,
        spidey_gif=url_for("static", filename="spidey.gif"),
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
