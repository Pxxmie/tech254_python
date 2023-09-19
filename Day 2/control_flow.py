# if Statement

film_rating = "u"
#:(condition)
if film_rating.lower() == "u":
    print("All age groups can watch this movie")
    # elif- use instead of lots of if statement  - less processing power and runs only if if condition is not met.
elif film_rating.lower() == "pg":
    print("Paretal guidance is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People aged 12 or over can watch this film unsupervised. Younger people must be supervised.")
elif film_rating.lower() == "15":
    print("People aged 25 or over can watch this movie.")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie.")
# else
else:
    print("This is not a valid rating, please use 'u', 'pg','12' or '12a, '15, '18'.")

# In Python there are no switch statements or case statements.

# Class Activity
