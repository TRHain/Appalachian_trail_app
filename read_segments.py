# This opens the CSV file in read mode
with open("data/trail_segments.csv", "r") as file:
	#Will loop through each line in file CSV
    for line in file:
        #print each line - raw info, to console for print
        print(line.strip())