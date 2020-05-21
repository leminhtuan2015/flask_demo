from flask import Blueprint, render_template
from flask import request
import json

from .temperature import Temperature

temperrature_bp = Blueprint('temperrature_bp', __name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')

@temperrature_bp.route('/', methods=['GET'])
def index():
    day = request.args.get('day', default = "2020-05-21", type = str)

    temperatures = Temperature.getByDay(day)
    jsonStr = json.dumps([temperature.toJSON() for temperature in temperatures])

    return render_template('temperrature/index.html', temperatures = temperatures, jsonStr = jsonStr)

@temperrature_bp.route('/api/get/', methods=['GET'])
def api_get():
    day = request.args.get('day', default = "2020-05-21", type = str)

    temperatures = Temperature.getByDay(day)
    jsonStr = json.dumps([temperature.toJSON() for temperature in temperatures])

    return jsonStr

@temperrature_bp.route('/api/create/', methods=['POST'])
def api_create():
    temperature = request.get_json()

    print("temperature: ")
    print(temperature)
    
    status = Temperature.create(temperature)
    return {"success": status}