import os
from trunk import run as run

from camera import Camera
import graphicalInterface

def main():
    try:
        run()
        graphicalInterface.run()
    finally:
        graphicalInterface.cleanup()
        print("fertig ohne probleme")

if __name__ == "__main__":
    main()


    