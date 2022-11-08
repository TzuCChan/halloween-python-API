from peewee import *

db = PostgresqlDatabase('film', user='leontzuchiangchan',
                        password='12345', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Movie(BaseModel):
    name = CharField()
    year = CharField()
    kill_counts = CharField()


db.drop_tables(Movie)
db.create_tables([Movie])

halloween = Movie(name="Halloween", year="1978", kill_counts="10")

halloween.save()

halloween_II = Movie(name="Halloween II", year="1981", kill_counts="20")

halloween_II.save()

halloween_III_Season_O_The_Witch = Movie(
    name="Halloween III", year="1982", kill_counts="30")

halloween_III_Season_O_The_Witch.save()

halloween_4_The_Return_Of_Michael_Myers = Movie(
    name="Halloween 4: The Return of Michael Myers", year="1988", kill_counts="40")

halloween_4_The_Return_Of_Michael_Myers.save()

halloween_5_The_Revenge_Of_Michael_Myers = Movie(
    name="Halloween 5: The Revenge of Michael Myers", year="1989", kill_counts="50")

halloween_5_The_Revenge_Of_Michael_Myers.save()

halloween_The_Curse_Of_Michael_Myers = Movie(
    name="Halloween_The_Curse_Of_Michael_Myers", year="1995", kill_counts="60")

halloween_The_Curse_Of_Michael_Myers.save()

halloween_H20_20_Years_Later = Movie(
    name="halloween_H20_20_Years_Later", year="1998", kill_count="70")

halloween_H20_20_Years_Later.save()

halloween_Resurrection = Movie(
    name="Halloween Resurrection", year="2002", kill_count="80")

halloween_Resurrection.save()

halloween_2007 = Movie(name="Halloween 2007", year="2007", kill_count="90")

halloween_2007.save()

halloween_II_2009 = Movie(name="Halloween II 2009",
                          year="2009", kill_count="100")

halloween_II_2009.save()

halloween_2018 = Movie(name="Halloween 2018", year="2018", kill_count="110")

halloween_2018.save()

halloween_Kills = Movie(name="Halloween Kills", year="2021", kill_count="120")

halloween_Kills.save()

halloween_Ends = Movie(name="Halloween Ends", year="2022", kill_count="130")

halloween_Ends.save()
