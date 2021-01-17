#function to find the lowest average score
def most_popular(friends):
    dictionary=dict.fromkeys(friends.keys(),0)
    #dictionary will have (name,total votes)
    #2D dictionary
    for name,ratingDict in friends.items():
        for student,vote in ratingDict.items():
            dictionary[student]+=vote
    #lowest score is found and printed
    lowavgscore=min(dictionary.values())
    return str([name for name in dictionary if dictionary[name]==lowavgscore])

alice_ratings =  {"alonzo" : 1, "bob" : 3, "turing" : 2}
bob_ratings =    {"alice" : 1, "alonzo": 2, "turing": 3}
alonzo_ratings = {"alice": 3, "bob": 2, "turing": 1}
turing_ratings = {"alice": 2, "alonzo": 1, "bob": 3}
friends = {"alice": alice_ratings, "bob": bob_ratings, "alonzo": alonzo_ratings, "turing": turing_ratings}

print(most_popular(friends))