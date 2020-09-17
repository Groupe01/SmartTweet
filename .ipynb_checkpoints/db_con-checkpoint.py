import os
import urllib.parse as up
import psycopg2

def connexion():
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







