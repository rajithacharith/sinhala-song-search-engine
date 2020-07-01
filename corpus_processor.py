import os
import json
from singlish2sinhala import Translate,transliterate
file_list = os.listdir('./raw_corpus')

for file in file_list:
    with open('./raw_corpus/'+file) as f:
        data = json.load(f)
        try:
            data['Artist_si'] = Translate(data['Artist'].lower())
            data['Lyrics_si'] = Translate(data['Lyrics'].lower())
            data['Music'] = Translate(data['Music'].lower())
            data['searchable_lyric'] = transliterate(data['song_lyrics'].lower())
        except KeyError:
            print(data)
        except AttributeError:
            print(data)

        with open('./processed_corpus/'+file, 'w',encoding='utf-8') as outfile:
            json.dump(data, outfile,indent=4,ensure_ascii=False)
