import os
from datetime import datetime, timedelta
from mysql.connector import connection


class Data:

    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")

    def execute_query(query):
        try:
            con = connection.MySQLConnection(
                user=Data.DB_USER,
                password=Data.DB_PASSWORD,
                host="us-cdbr-east-04.cleardb.com",
                database="heroku_4ef95ca69d09856",
            )

            print("\nConexão iniciada\nQuery:")
            print(query)

            sql = con.cursor()
            sql.execute(query)
            result = sql.fetchall()
            print("Resultado Obtido...")
            con.commit()
            con.close()
            print("Conexão finalizada.")

            return result

        except:
            print("Connection error tag=execute_query")

    def add_new_participant(author_id, author):
        add_person_query = (
            "INSERT INTO Ranking "
            "(ID, Points, PersonName, IsActive) "
            'VALUES ("' + str(author_id) + '",0, "' + author + '", 0)'
        )

        Data.execute_query(add_person_query)

    def get_general_ranking():
        get_ranking_query = (
            "SELECT PersonName, Points FROM Ranking ORDER BY Points DESC"
        )

        return Data.execute_query(get_ranking_query)

    def get_general_overall_ranking():
        get_overall_ranking_query = (
            "SELECT r.PersonName, (r.Points + lr.Points) as Pts "
            + "    FROM Ranking AS r "
            + "LEFT JOIN LegacyRanking AS lr"
            + "    ON r.ID = lr.ID"
            + "ORDER BY Pts DESC;"
        )

        return Data.execute_query(get_overall_ranking_query)

    def get_points_by_id(id):
        get_player_ranking_query = (
            "SELECT Points " + "FROM Ranking WHERE ID = " + str(id)
        )

        return Data.execute_query(get_player_ranking_query)[0][0]

    def update_points(id, points):
        update_points_query = (
            "UPDATE Ranking SET Points = "
            + str(points)
            + ' WHERE ID = "'
            + str(id)
            + '"'
        )

        Data.execute_query(update_points_query)

    def add_new_image(author_id, url, filename):
        now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        add_image_query = (
            "INSERT INTO ImageRef "
            + "(PersonID, DateAdded, URL, IsActive,FileName) "
            + 'VALUES ("{}", "{}", "{}", {}, "{}")'.format(
                author_id, now_string, url, 1, filename
            )
        )

        Data.execute_query(add_image_query)

    def has_recent_image(author_id):
        twenty_minutes = timedelta(minutes=20)
        now = datetime.now()
        recent_time = now - twenty_minutes
        recent_time_string = recent_time.strftime("%Y-%m-%d %H:%M:%S")

        get_recent_images_query = (
            "SELECT PersonID FROM ImageRef "
            + 'WHERE PersonID = "{}" '.format(author_id)
            + 'AND DateAdded > "{}" '.format(recent_time_string)
        )
        result = Data.execute_query(get_recent_images_query)
        if result == []:
            return False
        return True
