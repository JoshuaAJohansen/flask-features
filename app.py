from flask import Flask, request, render_template, url_for
from flask import jsonify
from flask import redirect
from flask import Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    # full query string
    request.query_string
    # query parameter
    request.args.get('foo')
    return 'Hello World!'


# return json for get method
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    # get ip of requester
    print(request.remote_addr)
    return jsonify({'ip': request.remote_addr}), 200 # { "ip": "127.0.0.1" }


# redirect
@app.route("/redirect")
def hello():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

# optional parameters - https://stackoverflow.com/a/14032302
@app.route('/<user_id>', defaults={'username': None})
@app.route('/<user_id>/<username>')
def show(user_id, username):
    pass


# parameterized urls with data type
@app.route('/user/id/<int:user_id>')
def profile(user_id):
    print(user_id)
    return 'hello'


# accept post only
@app.route('/postmethod', methods=['POST'])
def post_method():

    # access headers
    request.headers['your-header-name'] # https://stackoverflow.com/a/29387151
    # access cookies
    request.cookies['']
    # get raw data despite the headers, https://stackoverflow.com/a/23898949
    request.get_data()
    # access query params
    search = request.args.get("search")
    page = request.args.get("page")
    print(request.is_json)
    # fail silently
    content = request.get_json(silent=True)
    print(content)
    return 'JSON posted'


# return xml response
@app.route('/ajax_ddl')
def ajax_ddl():
    xml = '<note>foo</note>'
    # https: // stackoverflow.com / a / 11774026
    # https: // stackoverflow.com / questions / 11773348 / python - flask - how - to - set - content - type
    return Response(xml, mimetype='text/xml')

# return json response
@app.route('/create/<int:id>')
def primes(id):
    return Response("{'id':'" + id + "'}", status=201, mimetype='application/json')


# error handling
@app.errorhandler(404)
def not_found(e):
    return '', 404


if __name__ == '__main__':
    app.run()
