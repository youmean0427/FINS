import requests
import json

key_table = [
  {
    "keyword_id": 1701,
    "keyword": "hero"
  },
  {
    "keyword_id": 9663,
    "keyword": "sequel"
  },
  {
    "keyword_id": 9715,
    "keyword": "superhero"
  },
  {
    "keyword_id": 9717,
    "keyword": "based on comic"
  },
  {
    "keyword_id": 179431,
    "keyword": "duringcreditsstinger"
  },
  {
    "keyword_id": 180059,
    "keyword": "death of king"
  },
  {
    "keyword_id": 180547,
    "keyword": "marvel cinematic universe (mcu)"
  },
  {
    "keyword_id": 195394,
    "keyword": "hidden civilization"
  },
  {
    "keyword_id": 952,
    "keyword": "lightning"
  },
  {
    "keyword_id": 2095,
    "keyword": "anti hero"
  },
  {
    "keyword_id": 9715,
    "keyword": "superhero"
  },
  {
    "keyword_id": 9717,
    "keyword": "based on comic"
  },
  {
    "keyword_id": 15001,
    "keyword": "demon"
  },
  {
    "keyword_id": 155030,
    "keyword": "superhero team"
  },
  {
    "keyword_id": 179431,
    "keyword": "duringcreditsstinger"
  },
  {
    "keyword_id": 229266,
    "keyword": "dc extended universe"
  },
  {
    "keyword_id": 1295,
    "keyword": "europe"
  },
  {
    "keyword_id": 3023,
    "keyword": "eastern europe"
  },
  {
    "keyword_id": 244797,
    "keyword": "donbass war"
  },
  {
    "keyword_id": 252606,
    "keyword": "russian invasion of ukraine"
  },
  {
    "keyword_id": 257783,
    "keyword": "2010s"
  },
  {
    "keyword_id": 272265,
    "keyword": "ukraine"
  },
  {
    "keyword_id": 273967,
    "keyword": "war"
  },
  {
    "keyword_id": 294795,
    "keyword": "war in ukraine"
  },
  {
    "keyword_id": 301386,
    "keyword": "russo-ukrainian war"
  },
  {
    "keyword_id": 3199,
    "keyword": "clown"
  },
  {
    "keyword_id": 3335,
    "keyword": "halloween"
  },
  {
    "keyword_id": 6506,
    "keyword": "resurrection"
  },
  {
    "keyword_id": 9663,
    "keyword": "sequel"
  },
  {
    "keyword_id": 10292,
    "keyword": "gore"
  },
  {
    "keyword_id": 12339,
    "keyword": "slasher"
  },
  {
    "keyword_id": 15127,
    "keyword": "killer"
  },
  {
    "keyword_id": 176691,
    "keyword": "killer clown"
  },
  {
    "keyword_id": 179431,
    "keyword": "duringcreditsstinger"
  },
  {
    "keyword_id": 191327,
    "keyword": "evil clown"
  },
  {
    "keyword_id": 232795,
    "keyword": "halloween night"
  },
  {
    "keyword_id": 296359,
    "keyword": "graphic violence"
  },
  {
    "keyword_id": 306196,
    "keyword": "megaslasher"
  },
  {
    "keyword_id": 703,
    "keyword": "detective"
  },
  {
    "keyword_id": 8250,
    "keyword": "victorian england"
  },
  {
    "keyword_id": 9663,
    "keyword": "sequel"
  },
  {
    "keyword_id": 160342,
    "keyword": "female detective"
  },
  {
    "keyword_id": 273879,
    "keyword": "sherlock holmes"
  },
  {
    "keyword_id": 236,
    "keyword": "suicide"
  },
  {
    "keyword_id": 703,
    "keyword": "detective"
  },
  {
    "keyword_id": 2340,
    "keyword": "paranoia"
  },
  {
    "keyword_id": 2726,
    "keyword": "therapist"
  },
  {
    "keyword_id": 2754,
    "keyword": "trauma"
  },
  {
    "keyword_id": 10541,
    "keyword": "curse"
  },
  {
    "keyword_id": 11612,
    "keyword": "hospital"
  },
  {
    "keyword_id": 13005,
    "keyword": "doctor"
  },
  {
    "keyword_id": 41329,
    "keyword": "mental illness"
  },
  {
    "keyword_id": 156075,
    "keyword": "evil"
  },
  {
    "keyword_id": 157701,
    "keyword": "psychotic"
  },
  {
    "keyword_id": 241827,
    "keyword": "demonic"
  },
  {
    "keyword_id": 268132,
    "keyword": "based on short film"
  },
  {
    "keyword_id": 278807,
    "keyword": "ptsd"
  },
  {
    "keyword_id": 818,
    "keyword": "based on novel or book"
  },
  {
    "keyword_id": 2504,
    "keyword": "world war i"
  },
  {
    "keyword_id": 11117,
    "keyword": "tank"
  },
  {
    "keyword_id": 14643,
    "keyword": "battle"
  },
  {
    "keyword_id": 15060,
    "keyword": "period drama"
  },
  {
    "keyword_id": 191004,
    "keyword": "german soldier"
  },
  {
    "keyword_id": 210184,
    "keyword": "1910s"
  },
  {
    "keyword_id": 230333,
    "keyword": "aircraft"
  },
  {
    "keyword_id": 810,
    "keyword": "budapest, hungary"
  },
  {
    "keyword_id": 1462,
    "keyword": "samurai"
  },
  {
    "keyword_id": 6259,
    "keyword": "psychopath"
  },
  {
    "keyword_id": 6625,
    "keyword": "family secrets"
  },
  {
    "keyword_id": 9675,
    "keyword": "prequel"
  },
  {
    "keyword_id": 9826,
    "keyword": "murder"
  },
  {
    "keyword_id": 11062,
    "keyword": "impersonator"
  },
  {
    "keyword_id": 18409,
    "keyword": "mental patient"
  },
  {
    "keyword_id": 161814,
    "keyword": "psycho killer"
  },
  {
    "keyword_id": 173298,
    "keyword": "escaped mental patient"
  },
  {
    "keyword_id": 197430,
    "keyword": "missing daughter"
  },
  {
    "keyword_id": 210544,
    "keyword": "estonia"
  },
  {
    "keyword_id": 227855,
    "keyword": "female psychopath"
  },
  {
    "keyword_id": 209439,
    "keyword": "sport climbing"
  },
  {
    "keyword_id": 1415,
    "keyword": "small town"
  },
  {
    "keyword_id": 2286,
    "keyword": "border"
  },
  {
    "keyword_id": 156091,
    "keyword": "missing person"
  },
  {
    "keyword_id": 2710,
    "keyword": "fairy"
  },
  {
    "keyword_id": 4344,
    "keyword": "musical"
  },
  {
    "keyword_id": 6300,
    "keyword": "puppet"
  },
  {
    "keyword_id": 209220,
    "keyword": "live action and animation"
  },
  {
    "keyword_id": 245230,
    "keyword": "live action remake"
  },
  {
    "keyword_id": 267848,
    "keyword": "talking animals"
  },
  {
    "keyword_id": 302735,
    "keyword": "pinocchio"
  },
  {
    "keyword_id": 2157,
    "keyword": "hacker"
  },
  {
    "keyword_id": 241221,
    "keyword": "wild life"
  },
  {
    "keyword_id": 380,
    "keyword": "sibling relationship"
  },
  {
    "keyword_id": 616,
    "keyword": "witch"
  },
  {
    "keyword_id": 3335,
    "keyword": "halloween"
  },
  {
    "keyword_id": 5923,
    "keyword": "sister"
  },
  {
    "keyword_id": 6270,
    "keyword": "high school"
  },
  {
    "keyword_id": 6506,
    "keyword": "resurrection"
  },
  {
    "keyword_id": 9663,
    "keyword": "sequel"
  },
  {
    "keyword_id": 12377,
    "keyword": "zombie"
  },
  {
    "keyword_id": 33795,
    "keyword": "salem, massachusetts"
  },
  {
    "keyword_id": 179430,
    "keyword": "aftercreditsstinger"
  },
  {
    "keyword_id": 179431,
    "keyword": "duringcreditsstinger"
  }
]


final_result = []
with open('movie_data_test.json', 'r') as f:
    kw_data = json.load(f)
    with open('keyword_movie_edit.json', 'w', encoding='utf-8') as f:
        for k in range(len(kw_data)):
            print(k)
            movie_id = kw_data[k]['movie_key']
            requestData = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=8d2390a7f14da4093a0836c65dfb59a2")
            mData = requestData.json()
            keywords = mData["keywords"]

            # with open('../1117JSON/keyword_table.json', 'r', encoding='utf-8') as f:
            #     gen_table = json.load(f)
                # kk['id']이 일치하는 keyword의 인덱스 번호를 담아야함..
            for k1 in range(len(keywords)):
                for k2 in range(len(key_table)):
                    if keywords[k1]['id'] == key_table[k2]['keyword_id']:
                        keyword_id = k2
                        keywords_dic = {
                            'movie_id' : k,
                            'keyword_id' : keyword_id,
                        }
                        final_result.append(keywords_dic)    
        json.dump(final_result, f, indent=2, ensure_ascii=False)
