from flask import Flask, jsonify, request, render_template
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

        if not nom_anime or not saison_num or not num_episode:
            return jsonify({"status": "arguments invalides", "saved": False})

        Cardinal.statCollect(nom_anime, saison_num, num_episode)

        return jsonify({"status": "ok", "saved": True})
    
    @app.route("/api/getStats", methods=["GET"])
    def getStats():
        p = request.headers.get("X-Admin-Token", "").strip()
        if p == "":
            p = request.args.get("p", "").strip()
            
        elif p != ADMIN_PASSWORD:
            return jsonify({"status": "Unauthorized", "saved": False})
        
        rows = Cardinal.getStats(p)
        return jsonify(rows)

    @app.route("/api/renderStats", methods=["GET"])
    def renderStats():
        return jsonify({"status": "Offline", "info": "The site is actually on update for new ui"})
        # return render_template("index.html", token=ADMIN_PASSWORD)