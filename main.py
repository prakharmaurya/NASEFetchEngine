import _thread
from engine import mainLoop
from flask import Flask, request

app = Flask(__name__, static_url_path='')


@app.route('/')
def root():
    return app.send_static_file('./static/')


def runServer():
    app.run()


# Define a function for the thread
def thread_runner(threadName, fn):
    print(threadName + " is running")
    fn()


try:
    _thread.start_new_thread(thread_runner, ("Server Thread", runServer, ))
    _thread.start_new_thread(thread_runner, ("Engine Thread", mainLoop, ))
except:
    print("Error: unable to start thread")
    _thread.start_new_thread(thread_runner, ("Server Thread", runServer, ))
    _thread.start_new_thread(thread_runner, ("Engine Thread", mainLoop, ))

while(1):
    pass
