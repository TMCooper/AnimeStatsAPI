from flask import Flask, jsonify, request
from src.backend import *

class Yui:
    app = Flask(__name__)
    
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "test" : "test"
        })
    
    @app.route("/api/stats", methods=["GET"]) # https://animestats.fuyuki.me/api/stats?n=Nom_ANIME&s=Num_SAISON&e=NOMBRE_EPISODE
    def statsCollect():
        nom_anime = request.args.get("n", "").strip()
        saison_num = request.args.get("s", "").strip()
        num_episode = request.args.get("e", "").strip()

        if not nom_anime or saison_num or num_episode:
            return jsonify({"satus": "args manquans", "saved": False})

        Cardinal.statCollect(nom_anime, saison_num, num_episode)

        return jsonify({"status": "ok", "saved": True})
    
    @app.route("/api/getStats", methods=["GET"])
    def getStats():
        p = request.args.get("p", "").strip()
        rows = Cardinal.getStats(p)
        return jsonify(rows)
