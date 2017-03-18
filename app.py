from github import Github
from flask import Flask
import sys
import base64

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker App!!"


@app.route("/v1/<filename>")
def getConfig(filename):
    if(filename == 'dev-config.yml' or filename == 'test-config.yml' or
       filename == 'dev-config.json' or filename == 'test-config.json'):
        try:
            g = Github()
            arg=sys.argv[1]
            url=arg.split("/")
            user=url[3]
            repo=url[4]
            file=g.get_user(user).get_repo(repo).get_file_contents(filename).content
            return base64.b64decode(file)
        except:
            return "Invalid GitHub Repository."
            
    else:
        return "File is invalid. Please try again."
                

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
