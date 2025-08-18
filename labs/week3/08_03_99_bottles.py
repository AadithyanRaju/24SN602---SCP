# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it

jars_of_payasam = 100
while jars_of_payasam > 0:
    print(f"There are {jars_of_payasam} jar of payasam on the counter ... now I ate one!")
    jars_of_payasam -= 1
print(f"There are 0 jars of payasam on the counter - none left to eat!")
print("Now I will go vomit....")
