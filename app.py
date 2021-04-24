from api_gateway import *
from database.connection import *


if __name__ == '__main__':
    # cnx = connector.connect(
    #     host="127.0.0.1",
    #     port=3306,
    #     user=USER_NAME,
    #     password="")
    # cursor = cnx.cursor()
    # create_database(cursor)
    # create_table(cursor)
    init_database()
    app.run()
