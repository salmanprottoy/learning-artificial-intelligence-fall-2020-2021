import requests
import random
import nltk
from nltk.corpus import stopwords, wordnet
import re

english_stops = set(stopwords.words('english'))
# below words were  intentionally removed , based on few analytical stuff
english_stops.add('.')
english_stops.add('also')
english_stops.add('get')


def feature_extractor(document):
    features = {}
    ls = []
    for document_words in document:
        for i, word in enumerate(document_words):
            if ((word.lower() not in english_stops
                 and word.isalpha())
                    or word.lower() == 'not'):
                syn = wordnet.synsets(word.lower())
                v = 'no'
                n = 'no'
                r = 'no'
                a = 'no'
                identity = 'unknown'
                if len(syn) == 0:
                    identity = 'unknown'
                    continue
                else:
                    identity = 'known'
                word = word.lower()
                features['contains(%s) with identity %s' % (word.lower(), identity)] = True
    return features


def pre_train_processor(sent):
    rd = re.sub(r'(^@| @)[^ ]+', r"", sent)
    rd = re.sub(r'(^http| http)[^ ]+', r"", rd)
    rd = re.sub(r'(\.)*\1', r".", rd)
    rep = re.findall(r'(\w).*\1.*\1', rd)

    for ch in rep:
        rd = re.sub(r'' + ch + ch + ch + r'+', r'' + ch + ch, rd)
    sentences = nltk.sent_tokenize(rd)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    return sentences


def train_classifier():
    l = ['1006589563512903396', '1008324413029484000', '1040575996755346578', '1045137713186360887',
         '7022552177697192106', '674420826054740334', '698451933787252187', '414302334487557591', '8944057146243258823',
         '6946341970593481260', '1431312376514000040', '7864797704321962005', '7070434591968454556']
    app_id = ''
    app_key = ''
    final_resp = []
    featuresets = []
    url = "http://developer.goibibo.com/api/voyager/get_hotels_by_cityid/?app_id=<enter your app id without <> >&app_key=<enter your app key with <> >&city_id=6771549831164675055"
    res = requests.get(url)
    result = res.json()

    print(len(result['data'].keys()))
    count = 0
    for key in result['data'].keys():
        count += 1
        print(count)
        vid = result['data'][key]['hotel_geo_node']['_id']
        # vid = data.get('vid','7022552177697192106')

        limit = "50"
        url = "http://ugc.goibibo.com/api/HotelReviews/forWeb?app_id=" + app_id + "&app_key=" + app_key + "&vid=" + vid + "&limit=" + limit + "&offset=0"
        res = requests.get(url)
        reslt = res.json()
        try:
            for review in reslt:
                if review.get('reviewContent') and len(review['reviewContent'].strip()) > 10:
                    final_resp.append({'rating': review['totalRating'], 'text': review['reviewContent']})
        except Exception as e:
            print(str(e))

    for x in final_resp:
        data = feature_extractor(pre_train_processor(x['text']))
        if x['rating'] > 3:
            tag = 'good'
        elif x['rating'] == 3:
            tag = 'moderate'
        else:
            tag = 'bad'
        featuresets.append((data, tag))
    print("lenght of data set: " + str(len(featuresets)))
    feat_len = int(0.8 * len(featuresets))
    train_set, test_set = featuresets[:feat_len], featuresets[feat_len:]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
    return classifier


def check_pos_hotels(classifier, data):
    sentences = pre_train_processor(data)

    feat = feature_extractor(sentences)

    res = {'features': feat, 'tag': classifier.classify(feat)}
    return res

