from flask import Flask, redirect
from flask_limiter import Limiter
from flask_talisman import Talisman

app = Flask(__name__)

i = 0


def get_ipaddr():
    if "X-Forwarded-For" in request.headers:
        return request.headers.get("X-Forwarded-For").split(",")[0].strip()
    return request.remote_addr

Talisman(app, content_security_policy=None, force_https=True)

limiter = Limiter(
    app=app,
    key_func=get_ipaddr,
    default_limits=["100 per hour"]
)

@limiter.limit("50 per hour")
@app.route('/')
def home():
  global i
  try:
    html_link = ["https://index-autumn.onrender.com", "https://autumn-ambrosia.pages.dev"]

    return redirect(html_links[i % len(html_links)])
  except:
    return "<h2>Failed to redirect. Please try again</h2>"

@limiter.limit("40 per hour")
@app.route('/wake')
def wake():
    return "w"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
