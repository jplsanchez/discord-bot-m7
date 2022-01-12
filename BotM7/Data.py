import os
from datetime import datetime, timedelta
from mysql.connector import connection


class Data:

    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")

    def __execute_query(query):
        try:
            con = connection.MySQLConnection(
                user=Data.DB_USER,
                password=Data.DB_PASSWORD,
                host="us-cdbr-east-04.cleardb.com",
                database="heroku_4ef95ca69d09856",
            )

            print("\nINFO: Conexão iniciada\nQuery:")
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
            print("ERROR: Erro de conexão tag=__execute_query")

    def add_new_participant(self, author_id, author):
        add_person_query = (
            "INSERT INTO Ranking "
            + "(ID, Points, PersonName, IsActive) "
            + f'VALUES ("{str(author_id)}", 0, "{author}", 0)'
        )

        Data.__execute_query(add_person_query)

    def get_general_ranking(self):
        get_ranking_query = (
            "SELECT PersonName, Points FROM Ranking ORDER BY Points DESC"
        )

        return Data.__execute_query(get_ranking_query)

    def get_general_overall_ranking(self):
        get_overall_ranking_query = (
            "SELECT r.PersonName, (r.Points + lr.Points) as Pts "
            + "FROM Ranking AS r "
            + "LEFT JOIN LegacyRanking AS lr "
            + "ON r.ID = lr.ID "
            + "ORDER BY Pts DESC; "
        )

        return Data.__execute_query(get_overall_ranking_query)

    def get_points_by_id(self, id):
        get_player_ranking_query = f"SELECT Points FROM Ranking WHERE ID = {str(id)}"

        return Data.__execute_query(get_player_ranking_query)[0][0]

    def update_points(self, id, points):
        update_points_query = (
            f'UPDATE Ranking SET Points = {str(points)} WHERE ID = "{str(id)}"'
        )

        Data.__execute_query(update_points_query)

    def add_new_image(self, author_id, url, filename):
        now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        add_image_query = (
            "INSERT INTO ImageRef (PersonID, DateAdded, URL, IsActive,FileName) "
            + f'VALUES ("{author_id}", "{now_string}", "{url}", {1}, "{filename}")'
        )

        Data.__execute_query(add_image_query)

    def has_recent_image(self, author_id):
        twenty_minutes = timedelta(minutes=20)
        now = datetime.now()
        recent_time = now - twenty_minutes
        recent_time_string = recent_time.strftime("%Y-%m-%d %H:%M:%S")

        get_recent_images_query = (
            "SELECT PersonID FROM ImageRef "
            + f'WHERE PersonID = "{author_id}" AND DateAdded > "{recent_time_string}" '
        )
        result = Data.__execute_query(get_recent_images_query)
        if result == []:
            return False
        return True

    def set_points(self, id: str, points: float):
        set_points_query = (
            f'UPDATE ranking SET points = {str(points)} where ID = "{id}"'
        )
        return Data.__execute_query(set_points_query)
