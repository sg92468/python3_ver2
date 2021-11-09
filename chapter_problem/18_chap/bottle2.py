from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='./chapter_problem/18_chap')

run(host='localhost', port=9999)