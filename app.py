import requests
from flask import Flask, render_template, request

from settings import settings

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    template = render_template(template_name_or_list="index.html")
    if request.method == "POST":
        ip_address = request.form.get("ip_data", None)
        if ip_address:
            response = requests.get(
                settings.IP_ADDRESS_API.replace(
                    "IP_ADDRESS_API_KEY", settings.IP_ADDRESS_API_KEY
                ).replace("IP_ADDRESS", ip_address)
            )
            data = response.json()
            template = render_template(
                template_name_or_list="index.html",
                data=data,
                ip_address=ip_address,
                status=response.status_code,
            )

    return template
