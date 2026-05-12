#=============================
#.        Appalachian Trail Tracker
#==============================
#         Author: Trevor Hain
#				 May 7th, 2026 for example only

#-  This program tracks:
#-  Nobo/ Sobo Direction
#-  Sections Hiked
#-  Miles Walked
#-  Calories Burned
#-  Upcoming Sections
#-  Daily Hike Log
#-  Trail Journal entries
#------------------------------------——————————————
#This will Demonstrate the Following:
#Variables, Functions, Loops, Nested Lists,
#Dictionaries, User Input, Conditionals and Indexing

#==============================================
#.                       Begin Code Here 
#==============================================

#Import today's date utilizing feature in Python

from datetime import date

# ---------------------------------------———————————-
#.           Appalachian Trail Section Data
#----------------------------------------———————————-
# # Appalachian Trail Section Data by State beginning in GA
# Each List to be in this format: 
#.       [start_point, end_point, miles]
#Important Index [0] = starting point, [1] = ending point, [2] miles
# ---------------------------------------—————————————
#.                      GEORGIA SECTIONS
#------------------------------------------————————————
#Begin with Georgia since 80-90 percent begin here

georgia = [
#Section 1 in Georgia - Beginning or end
    ["Springer Mountain", "Hawk Mountain Shelter", 8.1],
		#Section 2 - Georgia
    ["Hawk Mountain Shelter", "Gooch Mountain Shelter", 7.7],
    #Section 3, Georgia - this continues to end of Georgia
		["Gooch Mountain Shelter", "Neels Gap", 15.8],
]

# Going North Carolina is state 2 or 1 in list 

north_carolina = [
#First section in NC
    ["Neels Gap", "Dicks Creek Gap", 36.5],
		#Section 2 - Nc
    ["Dicks Creek Gap", "Standing Indian Shelter", 16.7],
		#Section 3 NC
    ["Standing Indian Shelter", "Winding Stair Gap", 15.9],
]

#Going North Tennessee is 3rd state or #2 in list

tennessee = [
    ["Winding Stair Gap", "Fontana Dam", 63.4],
    ["Fontana Dam", "Newfound Gap", 40.6],
    ["Newfound Gap", "Hot Springs", 33.7],
]

#Maine is 14th state going North or first going south

maine = [
#second section in Maine
    ["Monson", "Katahdin Stream Campground", 114.5],
		#Last Section for those going North 
		#First Section for those Going South! 
    ["Katahdin Stream Campground", "Mount Katahdin", 5.2],
]

#===================================================
#.                         MASTER TRAIL LIST
#===================================================
#Nested list - appalachian_trail contains state lists
# ******************How this Works***************
#appalachian_trail[0] - gets Georgia
#appalachian_trail[0][0] - gets first Georgia Section
#appalachian_trail[0][0][2] - gets first section mileage 


# create AT list of states 
appalachian_trail = [
    georgia,                                    #0 in index 
    north_carolina,                        # 1 in index
    tennessee,                               # 2 in index 
    maine                                       # 13 in index of 14 states ;)
]

#State names match the order in appalachian_trail list
state_names = [
    "Georgia",
    "North Carolina",
    "Tennessee",
    "Maine"
]

#==================================================
#.                STORAGE LISTS to store user info
#==================================================
#
#Daily log will store ALL daily hiking logs from user input

daily_log = [ ]

# Create List- Journal Entries will store all journal entries 
#if the user decides to utilize this. 

journal_entries = [ ]


# =================================================
#                              FUNCTIONS
# =================================================
#.   User must choose a direction - North or South
#.   This won't be asked again unless the user decides to
#.   change this in menu
# - NOBO - Northbound - Georgia to Maine 
# - How our States are currently laid out in list
# - SOBO - Southbound - Maine to Georgia
# - SOBO - We need to reverse states and sections - mileage will remain the same

def choose_direction():
    while True:
        direction = input("Are you hiking NOBO or SOBO? ").strip().upper()
        # - if user chooses NOBO
        if direction == "NOBO":
            return "north"
	  # - if user chooses SOBO
        elif direction == "SOBO":
            return "south"
	 # - invalid returns this
        else:
            print("Please enter NOBO or SOBO.")

#=================================================
#.               SORT and STORE Direction
#=================================================
#If user is hiking North - utilize states and sections in order
#If user is hiking South - reverse states and sections

def get_ordered_trail(direction):

    #IF NOBO - follow normal order
    if direction == "north":

        return appalachian_trail, state_names

    # - SOBO - so please reverse order of states and sections		
    else:

        reversed_trail = [ ]
				
        #Reverse ALL STATES 
        for state in reversed(appalachian_trail):
            reversed_state = [ ]

		 #----------———— IMPORTANT -------------------———

            #Now reverse SECTIONS inside of EACH STATE
            for section in reversed(state):

		    # - Swaps Start and End Points to make things easier
                start = section[1]
                end = section[0]
                miles = section[2]
			#append 
                reversed_state.append([start, end, miles])

            reversed_trail.append(reversed_state)

        return reversed_trail, list(reversed(state_names))
# ==============================================
#                  SHOW FULL TRAIL
#		WILL DISPLAY EVERY SECTION IN ORDER
# ==============================================

def show_full_trail(direction):
    trail, names = get_ordered_trail(direction)

    print("\n--- Trail Sections ---")

    # here enumerate will give us index + item
    for i, state in enumerate(trail):
        print(f"\n{names[i]}:")

        for section in state:
            print(f"{section[0]} → {section[1]} | {section[2]} miles")
	
#==============================================
#                     FIND SECTIONS
#============================================== 
# This will find all sections between the start point and end point 
# and will return to the user: sections hiked and total miles. 

def find_hike_sections(direction, start_point, end_point):
    trail, names = get_ordered_trail(direction)

    tracking = False
    sections_hiked = []
    total_miles = 0

    # Loop Through ALL STATES
    for state_index, state in enumerate(trail):
        # LoopThrough all SECTIONS
        for section in state:
            section_start = section[0]
            section_end = section[1]
            section_miles = section[2]
            # start tracking once start point is found 
            if section_start.lower() == start_point.lower():
                tracking = True
            # add Section While Tracking
            if tracking:
                sections_hiked.append([
                    names[state_index],
                    section_start,
                    section_end,
                    section_miles
                ])
                total_miles += section_miles
# Stop once the endpoint is found
            if tracking and section_end.lower() == end_point.lower():
                return sections_hiked, total_miles

    return None, 0

#============================================== 
#.              LETS CALCULATE CALORIES!
#============================================== 
# This is a simple estimate utilizing formula found on web
# weight in lbs x miles x .75

def calculate_calories(weight_lbs, miles):
    return weight_lbs * miles * 0.75

#============================================== 
#.             SHOW UPCOMING SECTIONS
#============================================== 
# This will display the sections ahead of user for tomorrow, following today’s hike

def show_sections_ahead(direction, end_point, limit=3):
    trail, names = get_ordered_trail(direction)
    found = False
    ahead = []

    for state_index, state in enumerate(trail):
        for section in state:

           # When current section is found start collecting the next sections
            if found and len(ahead) < limit:

                ahead.append([
                    names[state_index],
                    section[0],
                    section[1],
                    section[2]
                ])
            # Current endpoint is found
            if section[1].lower() == end_point.lower():
                found = True

    return ahead

#============================================== 
#.           LOG DAILY HIKE
#============================================== 
# This will create a simple report for today

def log_daily_hike(direction, weight_lbs):
    print("\n--- Log Today's Hike ---")
    hike_date = input("Enter date or press Enter for today: ").strip()

# USE TODAYS DATE AUTOMATICALLY 
    if hike_date == "":

        hike_date = str(date.today())

    start_point = input("Where did you start today? ").strip()
    end_point = input("Where did you end today? ").strip()
# We must find all matching sections
    sections, miles_hiked = find_hike_sections(direction, start_point, end_point)

# If Route NOT Found
    if sections is None:
        print("\nCould not find that route.")
        print("Check spelling or make sure both places exist in your trail data.")
        return

# Calculate Calories 
    calories_burned = calculate_calories(weight_lbs, miles_hiked)
    calories_for_20 = calculate_calories(weight_lbs, 20)
    calories_for_same = calculate_calories(weight_lbs, miles_hiked)

# Store Today’s hiking data in the dictionary
    entry = {
        "date": hike_date,
        "direction": direction,
        "start": start_point,
        "end": end_point,
        "miles": miles_hiked,
        "calories_burned": calories_burned,
        "sections": sections
    }

# We now append the daily log with new dictionary entry 
    daily_log.append(entry)

#============================================== 
#.            THIS IS THE DAILY REPORT
#============================================== 
# Prints full daily report for the user in correct formatting
# date, n or s, start, end, miles hiked today and estimated calories burned,
# and sections hiked

    print("\n==============================")
    print("DAILY HIKING REPORT")
    print("==============================")
    print(f"Date: {hike_date}")
    print(f"Direction: {direction.upper()}")
    print(f"Started: {start_point}")
    print(f"Ended: {end_point}")
    print(f"Miles hiked today: {miles_hiked:.2f}")
    print(f"Estimated calories burned: {calories_burned:.0f}")

    print("\nSections hiked:")
    for section in sections:
        print(f"- {section[0]}: {section[1]} → {section[2]} | {section[3]} miles")

    print("\nTomorrow calorie estimate:")
    print(f"- To hike 20 miles: {calories_for_20:.0f} calories")
    print(f"- To hike same distance as today: {calories_for_same:.0f} calories")
# shows next sections
    ahead = show_sections_ahead(direction, end_point)

    print("\nSections ahead:")
    if len(ahead) == 0:
        print("No sections ahead found.")
    else:
        for section in ahead:
            print(f"- {section[0]}: {section[1]} → {section[2]} | {section[3]} miles")
#============================================== 
#.            VIEW DAILY LOG
#============================================== 

def view_daily_log():
    print("\n--- Daily Log ---")

    if len(daily_log) == 0:
        print("No hikes logged yet.")
        return

    for entry in daily_log:
        print("\n------------------------------")
        print(f"Date: {entry['date']}")
        print(f"Direction: {entry['direction'].upper()}")
        print(f"Route: {entry['start']} → {entry['end']}")
        print(f"Miles: {entry['miles']:.2f}")
        print(f"Calories burned: {entry['calories_burned']:.0f}")

#============================================== 
#.            ADD NEW JOURNAL ENTRY 
#============================================== 
def add_journal_entry():
    print("\n--- Trail Journal Entry ---")

    entry_date = input("Enter date or press Enter for today: ").strip()

    if entry_date == "":
        entry_date = str(date.today())

    entry_text = input("Write your journal entry: ")
# Stores Journal entry as dictionary 
    journal = {
        "date": entry_date,
        "entry": entry_text
    }
# Add to journal list
    journal_entries.append(journal)

    print("\nJournal entry saved.")

#============================================== 
#.            READ JOURNAL
#============================================== 
def read_journal():
    print("\n--- Trail Journal ---")

    if len(journal_entries) == 0:
        print("No journal entries yet.")
        return

    for journal in journal_entries:
        print("\n======================")
        print(f"Date: {journal['date']}")
        print("----------------------")
        print(journal["entry"])

#============================================== 
#.            CHANGE DIRECTION HIKER
#============================================== 

def change_direction():
    print("\nChange trail direction")
    return choose_direction()


# ==============================================
# MAIN PROGRAM
# ==============================================

def main():
    print("================================")
    print("APPALACHIAN TRAIL TRACKER")
    print("================================")
# store North or South Direction
    direction = choose_direction()

# Get user weight for calorie math
    while True:
        try:
            weight_lbs = float(input("Enter your body weight in pounds: "))
            break
        except ValueError:
            print("Please enter a valid number.")
# This is the Main Menu Loop
    while True:
        print("\n========== MENU ==========")
        print("1. See full trail sections")
        print("2. See miles walked today / log hike")
        print("3. View daily log")
        print("4. Change NOBO/SOBO direction")
        print("5. Add journal entry")
        print("6. Read journal")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

#============================================== 
#.            MENU OPTIONS 
#============================================== 
        if choice == "1":
            show_full_trail(direction)

        elif choice == "2":
            log_daily_hike(direction, weight_lbs)

        elif choice == "3":
            view_daily_log()

        elif choice == "4":
            direction = change_direction()
            print(f"Direction changed to {direction.upper()}.")

        elif choice == "5":
            add_journal_entry()

        elif choice == "6":
            read_journal()

        elif choice == "7":
            print("Happy trails. Stay dry, eat snacks, and trust the white blaze.")
            break

        else:
            print("Invalid option. Try again.")

# PROGRAM START 
main()