import psycopg2

connection = psycopg2.connect(host='127.0.0.1', 
                              port=2022, 
                              dbname='my_blog', 
                              user='postgres',
                              password='postgres')


def get_posts():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM posts')
    result = cursor.fetchall()

    return result


def get_authors():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM author')
    result = cursor.fetchall()

    return result
