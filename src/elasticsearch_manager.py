from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

def load_es():
    try:
        with open('src/Data/7282_1.csv', encoding="utf8") as f:
            reader = csv.DictReader(f)
            helpers.bulk(es, reader, index='my-index2', doc_type='my-type2')
            return True
    except:
            return False
    
def delete_index(index_name = 'my-index2'):
    try:
        es.indices.delete(index_name)
        return True
    except:
        return False
    
def get_hotel(hotel_name = "Days Inn Barstow"):
    hotel_list = []
    res2 = es.search(index="my-index2", body={"query": {"match": {"name": hotel_name}}})
    max_score = res2["hits"]["max_score"]
    for h in res2["hits"]["hits"]:
        if h["_score"] == max_score:
            hotel_list.append(h["_source"])
    return hotel_list

