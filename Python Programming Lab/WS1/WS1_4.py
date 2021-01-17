alonzo =   {"age" : 10, "height" : 42, "weight" : 175, "instrument" : "fiddle"}
turing =   {"age" : 41, "height" : 70, "weight" : 160, "instrument" : "theremin"}
bertha =   {"age" : 32, "height" : 97, "weight" : 587, "instrument" : "cello"}
tinkerB =  {"age" : 100, "height" : 4, "weight" : 0.5, "instrument" : "cello"}
banditos = {"Alonzo": alonzo, "Turing": turing, "Bertha": bertha, "TinkerB": tinkerB}

instrument=input("ENTER THE INSTRUMENT :")
dict={}
for d,name in banditos.items():
    if name["instrument"]==instrument :#if the instrument matches, we are inserting the dicitionary in dict
        dict.update({d:name})
    else:
        print("INSTRUMENT NOT FOUND IN THE GIVEN DICTIONARY!")
        break

print(dict)