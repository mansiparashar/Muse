import os
import requests
import json
import text2emotion as te

def get_score(input):
    returned_score = te.get_emotion(input)
    anger_weight = -17
    sadness_weight = -25
    happy_weight = 25
    surprise_weight = 17
    fear_weight = -17
    anger_score = returned_score['Angry']*anger_weight
    fear_score = returned_score['Fear']*fear_weight
    happy_score = returned_score['Happy']*happy_weight
    sadness_score = returned_score['Sad']*sadness_weight
    surprise_score = returned_score['Surprise']*surprise_weight
    score = (happy_score + surprise_score+fear_score+sadness_score+anger_score)
    return score




