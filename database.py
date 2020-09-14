import os
import urllib.parse as up
import psycopg2

def connexion() :
    '''
    Connexion to elefantsql database
    '''
    print ('Database connexion...')

    os.environ['DATABASE_URL'] = "postgres://zrhugxuo:lbklxIE7ZbXRFZhQOFCl0n_FbxlOI_WW@kandula.db.elephantsql.com:5432/zrhugxuo"
    url = up.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )

    cur = conn.cursor()
    print ('OK - Connected to Database.')

    return conn, cur




def insert(dataframe, hashtag) :
    '''
    Insert datas in database from dataframe created after Azure treatment
    '''
    conn, cur = connexion()

    print ('\nFormating datas...')
    df_import = dataframe
    df_import.replace(['positive', 'neutral', 'negative', 'mixed'],[1, 2, 3, 4],inplace=True)
    df_import['id_tweet'] = df_import.index
    print ('OK.\n')

    print ('Insert hashtag in database...')
    cur.execute(f"INSERT INTO hashtag(hashtag) VALUES('{hashtag}') ON CONFLICT DO NOTHING;")
    print ('OK.\n')

    print ('Insert tweets in database...')
    cur.execute(f"SELECT id_hashtag FROM hashtag WHERE hashtag.hashtag = '{hashtag}'")
    df_import['hashtag'] = cur.fetchall()[0][0]

    liste_df = df_import.values.tolist()
    cur.executemany("INSERT INTO tweet(date,lang,text,fk_feelind_id,confidence,id_tweet,fk_hashtag_id) VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;", liste_df)
    print ('OK. \n')

    conn.commit()
    conn.close()

    return len(liste_df)