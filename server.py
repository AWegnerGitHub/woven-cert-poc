from sanic import Sanic
from sanic.response import text
import os

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


app.run(host="0.0.0.0", port=os.environ["PORT"], debug=True, access_log=False)
