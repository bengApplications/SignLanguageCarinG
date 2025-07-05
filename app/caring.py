import os

from view import View

def run():
    is_backend_on = True
    #is_backend_on = False #outcomment this line to run the backend test
    if is_backend_on:
        run_backendTest()
    else:
        view = View()
        view.run()

def run_backendTest():
    tag = 'first'
    from tag import train_tag
    train_tag(tag)
     


