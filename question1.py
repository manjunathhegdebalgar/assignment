""" PROGRAM TO READ A FILE LINE BY LINE AND STORE THEM IN A LIST """

file = open("defaultDataFile.txt", "r")
line_list = list()
for line in file:
    content = line.split("\n")  # removing new line character from the line
    line_list.append(content[0])
print(line_list)
