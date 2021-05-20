from flask import Flask
from datetime import datetime
import os

PORT = 8080
name = os.environ['NAME']
if name == None or len(name) == 0:
  name = "Santander"
MESSAGE = "Hello, " + name + "!"
# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)
print(" Message: '" + MESSAGE + "'")

app = Flask(__name__)


@app.route("/")
def root():
  print("Handling web request. Returning message.")
  result = MESSAGE.encode("utf-8")
  return result


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
