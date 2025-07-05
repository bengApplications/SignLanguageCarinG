import os

from view import View

def run():
    is_backendTest_on = True
    is_backendTest_on = False #outcomment this line to run the backend test
    if is_backendTest_on:
        run_backendTest()
    else:
        view = View()
        view.run()

def run_backendTest():
    tag = 'peace'
    from tag import train_tag
    train_tag(tag)
     


