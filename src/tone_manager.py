
#__src__
from src import csv_manager
from src.IBM_cloud import tone
##import csv_manager
##from IBM_cloud import tone

def _average(lst): 
    return sum(lst) / len(lst) 

    
def get_tones_for_hotel(hotel_name = "Days Inn Barstow"):
    df = csv_manager.get_hotel(hotel_name)
    reviews = df["reviews.text"]
    tones_dict = {}
    for r in reviews:
        result = tone.get_tone(r)
        for r_tone in result["document_tone"]["tones"]:
            tone_id = r_tone["tone_id"] 
            if tone_id not in tones_dict.keys():
                tones_dict[tone_id] = []
            tones_dict[tone_id].append(r_tone["score"])

    tones_result = {}
    for key,values in tones_dict.items():
        tones_result[key] = _average(values)

    return tones_result

#######get_tones_for_hotel(hotel_name = "Acorn Motor Inn")


