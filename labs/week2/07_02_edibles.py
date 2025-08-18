# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
print(s[7:12])
print(s[5:9]+ s[11])
print(s[s.find('butter'):s.find('butter')+6])
print(s[s.find('flourish')]+s[s.find('ish'):s.find('ish')+3])
