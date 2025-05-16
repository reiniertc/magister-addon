from flask import Flask, jsonify
from datetime import datetime, timedelta
import asyncio
import json
import os
import sys

sys.path.append('/magister_lib')
from magister import Magister

app = Flask(__name__)

with open("/data/options.json") as f:
    config = json.load(f)

SCHOOL_URL = config["school_url"]
USERNAME = config["username"]
PASSWORD = config["password"]

async def haal_huiswerk_op():
    magister = await Magister.login(SCHOOL_URL, USERNAME, PASSWORD)
    vandaag = datetime.now()
    vijf_dagen = vandaag + timedelta(days=5)
    opdrachten = await magister.current_student.homework.get(vandaag, vijf_dagen)

    resultaat = []
    for opdracht in opdrachten:
        resultaat.append({
            "vak": opdracht.course.name,
            "beschrijving": opdracht.description,
            "datum": opdracht.deadline.strftime('%Y-%m-%d')
        })

    return resultaat

@app.route('/huiswerk')
def huiswerk_endpoint():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    huiswerk = loop.run_until_complete(haal_huiswerk_op())
    return jsonify({
        "aantal_opdrachten": len(huiswerk),
        "opdrachten": huiswerk
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
