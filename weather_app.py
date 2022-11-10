import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Base.metadata.tables # Check tables, not much useful
# Base.classes.keys() # Get the table names

Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Hawaii Weather App <br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"<br/>"
        f"List of Stations: /api/v1.0/stations<br/>"
        f"<br/>"
        f"Temperature for one year: /api/v1.0/tobs<br/>"
        f"<br/>"
        f"Temperature stat from the start date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"<br/>"
        f"Temperature stat from start to end dates(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )
#################################################
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    params = [Measurement.date,Measurement.prcp]
    query_result = session.query(*params).all()
    session.close()

    precipitation = []
    for date, prcp in query_result:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)

#################################################
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    params1 = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    query_result1 = session.query(*params1).all()
    session.close()

    stations = []
    for station,name,lat,lon,el in query_result1:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)

#################################################
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    lateststr = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    query_date = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    params2 = [Measurement.date,Measurement.tobs]
    query_result2 = session.query(*params2).filter(Measurement.date >= query_date).all()
    session.close()

    tobs_all = []
    for date, tobs in query_result2:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobs_all.append(tobs_dict)

    return jsonify(tobs_all)

#################################################
@app.route('/api/v1.0/<start>')
def get_t_start(start):
    session = Session(engine)
    query_result3 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()

    tobs_all1 = []
    for min,avg,max in query_result3:
        tobs_dict1 = {}
        tobs_dict1["Min"] = min
        tobs_dict1["Average"] = avg
        tobs_dict1["Max"] = max
        tobs_all1.append(tobs_dict1)

    return jsonify(tobs_all1)

#################################################
@app.route('/api/v1.0/<start>/<stop>')
def get_t_start_stop(start,stop):
    session = Session(engine)
    query_result4 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= stop).all()
    session.close()

    tobs_all2 = []
    for min,avg,max in query_result4:
        tobs_dict2 = {}
        tobs_dict2["Min"] = min
        tobs_dict2["Average"] = avg
        tobs_dict2["Max"] = max
        tobs_all2.append(tobs_dict2)

    return jsonify(tobs_all2)

#################################################
# run app
#################################################
if __name__ == '__main__':
    app.run(debug=True)