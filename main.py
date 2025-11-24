from src.api import *
from src.backend import* 

class Api:
    def launch():
        Cardinal.init_db()
        Yui.app.run(port=5024)

if __name__ == "__main__":
    Api.launch()