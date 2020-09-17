import numpy
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from collect_tweets import collect_tweets
#
key = "7b3d4c450fd84d3485f41b09087d5038"
endpoint = "https://cs-groupe-un.cognitiveservices.azure.com/"
#
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    print("Azure authentification successful.")
    return text_analytics_client

client = authenticate_client()
#
#df=collect_tweets('EnseignementSup')
#print(df.shape)
#documents_1 = df[["Tweet.text"]]
#print (documents_1.head())
#
def sentiment_analysis(client):
    df=collect_tweets('#EnseignementSup')
    df["r_analyse"]= ""
    df["confidence"] = ""
    for i in range(len(df)) : 
         
           
        document = [df["Tweet.text"][i]]
        response = client.analyze_sentiment(documents = document)[0]
        df["r_analyse"][i] = response.sentiment
        #print(df["r_analyse"])
        
        list_r_analyse = [response.confidence_scores.positive,
                          response.confidence_scores.neutral,
                           response.confidence_scores.negative,]
        df["confidence"][i] = max(list_r_analyse)
    
#print(f"{i} tweets analysed.")
    print(df.head())
#
#return df
sentiment_analysis(client)



    
#     documents = ["I had the best day of my life. I wish you were there with me."]
#     response = client.analyze_sentiment(documents = documents)[0]
#     print("Document Sentiment: {}".format(response.sentiment))
#     print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
#         response.confidence_scores.positive,
#         response.confidence_scores.neutral,
#         response.confidence_scores.negative,
#     ))
#     for idx, sentence in enumerate(response.sentences):
#         print("Sentence: {}".format(sentence.text))
#         print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
#         print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
#             sentence.confidence_scores.positive,
#             sentence.confidence_scores.neutral,
#             sentence.confidence_scores.negative,
#         ))
          
# sentiment_analysis(client)