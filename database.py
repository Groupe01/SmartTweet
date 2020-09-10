import os
import urllib.parse as up
import psycopg2

def connexion() :
    '''
    Connexion to elefantsql database
    '''
    print ('Data connexion...')

    os.environ['DATABASE_URL'] = "postgres://zrhugxuo:lbklxIE7ZbXRFZhQOFCl0n_FbxlOI_WW@kandula.db.elephantsql.com:5432/zrhugxuo"
    up.uses_netloc.append("postgres")
    url = up.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )

    cur = conn.cursor()
    return cur

    print ('OK - Connected to database.')


def insert(dataframe) :
    '''
    Insert datas in database from dataframe created after Azure treatment
    '''
    
    cur.execute('''INSERT INTO hashtag(id_hashtag, hashtag) VALUES (?,?);''',)