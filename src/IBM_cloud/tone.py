import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('s8ttc4twbt-uX4kBtNzYOdVyyFfc1sTkKIdz8s15KJVK')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://gateway-lon.watsonplatform.net/tone-analyzer/api')

def get_tone(text):
    #text = 'Team, I know that times are tough! Product '\
    #    'sales have been disappointing for the past three '\
    #    'quarters. We have a competitive product, but we '\
    #    'need to do a better job of selling it!'

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    #print(json.dumps(tone_analysis, indent=2))
    return tone_analysis