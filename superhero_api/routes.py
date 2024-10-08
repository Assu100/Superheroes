from flask import jsonify, request
from .models import db, Hero, Power, HeroPower

def setup_routes(app):
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes])

    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if hero:
            return jsonify(hero.to_dict()), 200
        return jsonify({"error": "Hero not found"}), 404

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers])

    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if power:
            return jsonify(power.to_dict()), 200
        return jsonify({"error": "Power not found"}), 404

    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        
        data = request.json
        if 'description' in data:
            power.description = data['description']
        
        try:
            db.session.commit()
            return jsonify(power.to_dict()), 200
        except Exception as e:
            return jsonify({"errors": ["validation errors"]}), 400

    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.json
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        try:
            db.session.add(hero_power)
            db.session.commit()
            return jsonify(hero_power.to_dict()), 201
        except Exception as e:
            return jsonify({"errors": ["validation errors"]}), 400
        
    @app.route('/', methods=['GET'])
    def home():
        return "Welcome to the Superheroes API!"


