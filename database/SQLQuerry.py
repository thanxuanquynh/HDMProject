add_users = ("INSERT INTO users "
               "(username, password, created_at, updated_at) "
               "VALUES (%(username)s, %(password)s, %(created_at)s, %(updated_at)s)")
add_topics = ("INSERT INTO topics "
              "(name, user_id, created_at, updated_at) "
              "VALUES (%(name)s, %(user_id)s, %(created_at)s, %(updated_at)s)")
