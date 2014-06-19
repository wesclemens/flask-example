from .. import app, cache

from time import gmtime, strftime

@app.route("/", methods=['GET'])
@app.route("/hi", methods=['GET'])
@cache.cached(timeout=20)
def home_get():
    return "Hello, World! -- GET -- %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime())


@app.route("/", methods=['POST'])
@app.route("/hi", methods=['POST'])
def home_post():
    return "Hello, World! -- POST -- %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime())
