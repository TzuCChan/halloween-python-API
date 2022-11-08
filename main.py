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

first = Movie(name="Halloween", year="1978", kill_counts="10")

first.save()

second = Movie(name="Halloween II", year="1981", kill_counts="20")

second.save()

third = Movie(name="Halloween III", year="1982", kill_counts="30")

third.save()

fourth = Movie(name="Halloween 4: The Return of Michael Myers",
               year="1988", kill_counts="40")

fourth.save()

fifth = Movie(name="Halloween 5: The Revenge of Michael Myers",
              year="1989", kill_counts="50")

fifth.save()

sixth = Movie(name="Halloween_The_Curse_Of_Michael_Myers",
              year="1995", kill_counts="60")

sixth.save()

seventh = Movie(name="halloween_H20_20_Years_Later",
                year="1998", kill_count="70")

seventh.save()

eighth = Movie(name="Halloween Resurrection", year="2002", kill_count="80")

eighth.save()

ninth = Movie(name="HALLOWEEN", year="2007", kill_count="90")

ninth.save()

tenth = Movie(name="HALLOWEEN II", year="2009", kill_count="100")

tenth.save()

eleventh = Movie(name="Halloween 2018", year="2018", kill_count="110")

eleventh.save()

twelfth = Movie(name="Halloween Kills", year="2021", kill_count="120")

twelfth.save()

thirteenth = Movie(name="Halloween Ends", year="2022", kill_count="130")

thirteenth.save()
