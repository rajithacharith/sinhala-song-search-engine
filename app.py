from flask import Flask, render_template, request
from  singlish2sinhala import Translate
import json
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

synonyms =  open("./synonyms.txt", "r",encoding='utf-8').read().split("\n")
synonyms_list = [i.split(",") for i in synonyms]
for sublist in synonyms_list:
    sublist = [i.strip() for i in sublist]

def get_similar_words(query_words):
    similar_words = query_words.copy()
    for sublist in synonyms_list:
        is_synonym = [i for i in query_words if i in sublist]
        if len(is_synonym) > 0:
            for i in sublist:
                similar_words.append(i)
    return similar_words

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        query = request.form['query']
        syn_artist = ['ගායකයා', 'ගයනවා', 'ගායනා', 'ගායනා', 'ගැයු', 'ගයන','ගැයූ']
        syn_eng_artist = ['sing', 'artist', 'singer', 'sung']
        syn_lyrics = ['ගත්කරු', 'රචකයා', 'ලියන්නා', 'ලියන', 'රචිත', 'ලියපු', 'ලියව්‌ව', 'රචනා', 'රචක', 'ලියන්']
        syn_eng_lyrics = ['lyricist', 'write', 'wrote', 'songwriter', 'written']
        syn_popularity = ['හොඳම', 'ජනප්‍රිය', 'ප්‍රචලිත', 'ප්‍රසිද්ධ', 'හොදම', 'ජනප්‍රියම']
        syn_eng_popularity = ['best','top']
        genre_keywords_si = ['Old Pops','Classics','Movie Songs','New Pop','Request','Duets','Golden Pop','Inspirational','Golden Oldies','Current Songs']
        fields = ['title', 'song_lyrics','searchable_lyric']
        query = query.split();
        for i in query:
            if(syn_artist.__contains__(i.lower())):
                fields.append('Artist_si^5')
                print("Boosting artist sinhala")
            if (syn_eng_artist.__contains__(i.lower())):
                fields.append('Artist^5')
                print("Boosting artist english")
            if (syn_lyrics.__contains__(i.lower())):
                fields.append('Lyrics_si^5')
                print("Boosting writer sinhala")
            if (syn_eng_lyrics.__contains__(i.lower())):
                fields.append('Lyrics^5')
                print("Boosting writer english")
            if (syn_popularity.__contains__(i.lower()) or syn_eng_popularity.__contains__(i.lower())):
                results = sorted_search()
                hits = results['hits']['hits']
                break
        else:
            results = search(query,fields)
            hits = results['hits']['hits']
            # print(results)

        # aggregations = results['aggregations']
        results_count = len(hits)
        if(results_count == 0):
            fields = ['title', 'song_lyrics^2','searchable_lyric^2']

            hits = search(query,fields)['hits']['hits']
            results_count = len(hits)

        aggs = results['aggregations']
        # print(results[0])
        return render_template('index.html', hits=hits, results_count=results_count,que=' '.join(query).strip(),agg = aggs)
    if request.method == 'GET':
        return render_template('index.html', init='True')


def search(query,fields):
    print('case 3')
    res = es.search(index='song_new', body={
        "query": {
            "multi_match": {
                "query": ' '.join(get_similar_words(query)),
                "fields": fields,
                # "fields": ['views'],
                "fuzziness": "AUTO"
                # "operator": operator,
                # "type": "best_fields"
            }
        },
        'size':20,
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "Genre.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "Music.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "Artist.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "Lyrics.keyword",
                    "size": 10
                }
            }
        }
    })
    print(res['aggregations'])
    return (res)

def sorted_search():
    print("Best case")
    res = es.search(index='song_new', body={
        "query": {
            "match_all": {}
        },
        'size':20,
        'sort':{'views' : 'desc'},
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "Genre.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "Music.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "Artist.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "Lyrics.keyword",
                    "size": 10
                }
            }
        }
    })
    return (res)


if __name__ == '__main__':
    app.run()
