from flask import Flask, request, jsonify, abort
from repositories.base_repository import BaseRepository

app = Flask(__name__)


@app.route('/country')
def get_country():
    country = request.args.get('country')

    if country is None:
        abort(400)

    db_repo = BaseRepository(logger=app.logger)
    result = db_repo.get_country_info(country)

    if result is None:
        abort(404)

    return jsonify(result)


@app.route('/region')
def get_region():
    region = request.args.get('region').upper()

    if region is None:
        abort(400)

    app.logger.info(region)
    db_repo = BaseRepository(logger=app.logger)
    result = db_repo.get_countries_by_region(region)

    if result is None:
        abort(404)

    return jsonify(result)


@app.route('/gdp')
def get_gdp():
    country = request.args.get('country').upper()

    if country is None:
        abort(400)

    app.logger.info(country)
    db_repo = BaseRepository(logger=app.logger)
    result = db_repo.get_country_gdp(country)

    if result is None:
        abort(404)

    return jsonify(result)


@app.route('/highest_avg_gdp')
def highest_avg_gdp():
    start = request.args.get('start')
    end = request.args.get('end')

    if start is None or end is None:
        abort(400)

    db_repo = BaseRepository(logger=app.logger)
    result = db_repo.get_gdp_avg(start, end, 'DESC')

    if result is None:
        abort(404)

    return jsonify(result)


@app.route('/lowest_avg_gdp')
def lowest_avg_gdp():
    start = request.args.get('start')
    end = request.args.get('end')

    if start is None or end is None:
        abort(400)

    db_repo = BaseRepository(logger=app.logger)
    result = db_repo.get_gdp_avg(start, end, 'ASC')

    if result is None:
        abort(404)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
