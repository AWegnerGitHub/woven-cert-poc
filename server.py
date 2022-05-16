from sanic import Sanic
from sanic.response import text

from sanic_jinja2 import SanicJinja2
import os

app = Sanic(__name__)
jinja = SanicJinja2(app)

VALID_IDS = {
    "asdfghjkl54321": {
        "name": "Martin McFly",
        "certificate_name": "Highly Recommended",
        "issue_date": "May 2022",
        "expire_date": "May 2023",
        "expired": False,
    },
    "9876789AbCd": {
        "name": "Martin McFly",
        "certificate_name": "Recommended",
        "issue_date": "Jan 2020",
        "expire_date": "Jan 2021",
        "expired": True,
    },
    "TOTALLYREAL": {
        "name": "Martin McFly",
        "certificate_name": "Highly Recommended",
        "issue_date": "May 2020",
        "expire_date": None,
        "expired": False,
    },
}


@app.get("/")
async def root_path(request):
    return text("Ok!")


@app.get("/certificate/validate/<cert_id:str>")
async def hello_world(request, cert_id: str):
    try:
        certificate = VALID_IDS[cert_id]
    except KeyError:
        certificate = None

    return jinja.render("index.html", request, context=certificate)


app.run(host="0.0.0.0", port=os.environ["PORT"], debug=True, access_log=False)
