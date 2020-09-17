from back.db_con import connexion
import pandas as pd


# connect to database
conn,cursor = connexion()


# getting feeling
def get_feeling (hashtag):

    cursor.callproc('get_feeling',[hashtag,])

    result = cursor.fetchall()
    
    df = pd.DataFrame(result,columns=['Hashtag','Positive','Negative','Neutral','Mixed'])
    df= df.astype({'Positive':int,'Negative':int,'Neutral':int,'Mixed':int})
    return(df)


# getting feeling by day   
def feeling_by_day(hashtag):
    '''
    Call the sql function to view datas day by day
    '''
    
    
    cursor.callproc('feeling_by_day',[hashtag,])
    result = cursor.fetchall()

    
    df = pd.DataFrame(result,columns=['hashtag','date','feeling','nb_tweets'])

    return (df)








