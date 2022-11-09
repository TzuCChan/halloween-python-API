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
    director = CharField()
    kill_counts = CharField()


db.drop_tables(Movie)
db.create_tables([Movie])

first = Movie(name="Halloween", year="1978",
              director="John Carpenter", kill_counts="5")

first.save()

second = Movie(name="Halloween II", year="1981",
               director="Rick Rosenthal", kill_counts="10")

second.save()

third = Movie(name="Halloween III", year="1982",
              director="Tommy Lee Wallace", kill_counts="28")

third.save()

fourth = Movie(name="Halloween 4: The Return of Michael Myers",
               year="1988", director="Dwight H. Little", kill_counts="10")

fourth.save()

fifth = Movie(name="Halloween 5: The Revenge of Michael Myers",
              year="1989", director="Dominique Othenin-Girard", kill_counts="15")

fifth.save()

sixth = Movie(name="Halloween_The_Curse_Of_Michael_Myers",
              year="1995", director="Joe Chappelle", kill_counts="16")

sixth.save()

seventh = Movie(name="halloween_H20_20_Years_Later",
                year="1998", director="Steve Miner", kill_count="7")

seventh.save()

eighth = Movie(name="Halloween Resurrection", year="2002",
               director="Rick Rosenthal", kill_count="11")

eighth.save()

ninth = Movie(name="HALLOWEEN", year="2007",
              director="Rob Zombie", kill_count="22")

ninth.save()

tenth = Movie(name="HALLOWEEN II", year="2009",
              director="Rob Zombie", kill_count="19")

tenth.save()

eleventh = Movie(name="Halloween 2018", year="2018",
                 director="David Gordon Green", kill_count="17")

eleventh.save()

twelfth = Movie(name="Halloween Kills", year="2021",
                director="David Gordon Green", kill_count="31")

twelfth.save()

thirteenth = Movie(name="Halloween Ends", year="2022",
                   director="David Gordon Green", kill_count="15")

thirteenth.save()
