from flask import Flask, render_template, url_for, request, redirect
from motive import motive
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route('/')  # can input specific data to do stuff
def my_home(username=None, post_id=None):
    addr1 = request.args.get('addr1', None)
    addr2 = request.args.get('addr2', None)
    cat = request.args.get('cat', None)
    results = []
    if addr1 != None and addr2 != None and cat != None:
        results = motive(addr1, addr2, cat)
    # calling the file
    return render_template("Website.html", results=results)


@app.route('/<string:page_name>')  # type in browser
def html_page(page_name):
    return render_template(page_name)  # calling the file


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        file = database.write(f'\n{name},{email}')

# GETTING REQUEST DATA


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou!.html')
    else:
        return 'something went wrong'


# @app.route('/blog')  # http://127.0.0.1:5000/blog WILL RUN THIS STUF
# def blog():
#     return 'THESE ARE MY THOTS'


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'THIS IS MY DOG'


if __name__ == '__main__':
    app.run()
