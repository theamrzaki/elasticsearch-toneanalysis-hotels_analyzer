#__python__
from flask import request, render_template, session,redirect
from . import hotel
from .. import mongo

#__src__
from src import tone_manager , csv_manager , elasticsearch_manager


#region tone_analyzer
@hotel.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('hotel/dashboard.html')
#endregion



#region tone_analyzer
@hotel.route('/tone_analyzer', methods=['GET', 'POST'])
def tone_analyzer():
    hotels = csv_manager.get_all_hotel_names()
    selected_hotel = ""
    tones = []
    ##tones = session["tones"] #testing
    if request.method == 'POST' and 'selected_hotel' in request.form:
        selected_hotel = request.form['selected_hotel']
        tones = tone_manager.get_tones_for_hotel(selected_hotel)
        try:
            print(tones)
        except:
            pass
        
        #session["tones"] = tones #testing
    return render_template('hotel/tone_analyzer.html',
                            selected_hotel=selected_hotel, hotels=hotels,tones=tones)
#endregion



#region hotel_indexer
@hotel.route('/hotel_indexer', methods=['GET', 'POST'])
def hotel_indexer():
    if "index" in session.keys() :
        hotels = csv_manager.get_all_hotel_names()
        selected_hotel = ""
        hotel_details = None
        tones = []
        #tones = session["tones"] #testing
        if request.method == 'POST' and 'selected_hotel' in request.form:
            selected_hotel = request.form['selected_hotel']
            tones = tone_manager.get_tones_for_hotel(selected_hotel)
            hotel_details = elasticsearch_manager.get_hotel(selected_hotel)
            ####session["tones"] = tones #testing
        return render_template('hotel/hotel_indexer.html',
                            index=True,selected_hotel=selected_hotel, hotels=hotels,tones=tones , hotel_details = hotel_details)
    else:
        return render_template('hotel/hotel_indexer.html',
                                index=False)


@hotel.route('/elasticindex_hotels', methods=['GET', 'POST'])
def elasticindex_hotels():
    try:
        result = elasticsearch_manager.load_es()
        if result:
            session["index"] = True
            print("elasticindex_hotels")
    except :
        pass
    return redirect("/hotel_indexer")

@hotel.route('/reset_index', methods=['GET', 'POST'])
def reset_index():
    try:
        result = elasticsearch_manager.delete_index()
        if result:
            print("reset_index")
            session.pop("index")
    except :
        pass
    
    return redirect("/hotel_indexer")
#endregion