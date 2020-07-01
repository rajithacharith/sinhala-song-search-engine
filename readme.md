# Sinhala Songs Search Engine

A Search Engine for Sinhala songs using Elasticsearch. A Web interface have been built to use the functions of the system.

## Getting Started:
To start the search engine follow the instructions given below.
* Run elasticsearch instance (port : 9200)
* Run the command `flask run`
* Go to http://localhost:5000 to experience



## Functions

* Search a song by title - කුරුටු ගෑ ගී
* Search by an artist name - නන්දා මාලනී ගැයූ ගීත
* Range queries - හොඳම සින්දු 10
* Synnonyms - මව් ගුණ ගීත
* Misspelled queries - කරුනරත දිවුල්ගනේ ගැයූ ගීත

## Data
Song Lyrics for the project was scraped from https://sinhalasongbook.com/ website. This website contains the song lyrics in sinhala with following metadata.


* Artist (English)
* Lyric writer (English)
* Music (English) 
* Genre (English)
* Beat
* View count
* Guitar Key
* Title (Both in Sinhala and English)

In order to support both sinhala and english in searching, these data were processed and added following metadata.
* Artist (Sinhala)
* Lyric Writer (Sinhala)
* Music (Sinhala)

And also, users are more likely to search songs from the lyrics as a singlish term, all the lyrics were transliterated into english. Therefore in processed documents there were 12 searchable data altogether.


## Indexing and Querying Techniques Used
Standard analyzer was used in querying as same as indexing. If input is in sinhala, sinhala features are boosted and if input is in English, English fields are boosted in order to get relevant results for the given input. And also the input was analyzed using predefined rules and if they match required rules, relevant fields were boosted in the query. 
In order to support misspelled words fuzziness is used when querying. This will calculate the Levenshtein edit distance with the terms and the query and include the similar documents in the results.

For assisting text mining, sinhala synonym list was inserted to the search engine. If the query contains at least one given phrase in the synonym list, then all the synonyms are inserted into the query. Using this, the system was able to identify to the queries like ‘මව් ගුණ ගීත’ and respond with songs which contains phrases such as ‘අම්මා’,’මව්නි’ etc. And also, this search engine contains a rule based algorithm to identify the content of the query.

The search engine supports faceted searches. Aggregations were used to create facets. Four filters (Genre filter, Artist Filter, Lyric filter and Music filter) were used to get the data separate for each type. This will include a separate part in the query result which contains the document counts for each bucket in each filter.
