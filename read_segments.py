# Empty list to store segment dictionaries
trail_segments=[]
#open CSV File 
with open("data/trail_segments.csv", "r") as file:
	#read all lines from file
    lines= file.readlines()
    #skip header row
    for line in lines[:1]:
        #remove spaces and create new line
        line = line.strip()
        #split open and melt into pieces
        parts = line.split(",")
        #Create Dictionary from CSV File
        segment = {"segment_id": int(parts[0]), "trail": parts[1], "state": parts[2], "miles": float(parts[3]), "ellevation_gain": float(parts[4])}
        #add dictionary to list
        trail_segments.append(segment)
    #print first 3 dictionaries only 
    print("\nFIRST 3 TRAIL SEGMENTS:\n")
    
    for segment in trail_segments[:3]:
        print(segment)