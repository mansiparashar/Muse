import os
import requests
import json
import text2emotion as te

def get_score(input):
    returned_score = te.get_emotion(input)
    anger_score = returned_score['Angry']
    fear_score = returned_score['Fear']
    happy_score = returned_score['Happy']
    sadness_score = returned_score['Sad']
    surprise_score = returned_score['Surprise']
    positivescore = (happy_score + surprise_score)
    negativescore = (fear_score+sadness_score+anger_score)
    finalScore = max(positivescore,negativescore)
    if finalScore == positivescore:
        score = finalScore*100
    else:
        score = finalScore*50
    return score


