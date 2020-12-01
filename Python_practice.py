#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes) + "% of the total votes.")
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
#message_to_candidate = (
#    f"You received {my_votes:,} votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson":390222}

#for county, voters in counties_dict.items():
#   print(f"{county} county has {voters:,} registered voters.")

voting_data = [{'county':'Arapahoe', 'registered_voters':422829}, {'county':'Denver', 'registered_voters':463353}, {'county':'Jefferson', 'registered_voters':432438}]
for dic in voting_data:
    print(f"{dic['county']} county has {dic['registered_voters']:,} registered voters.")

dir(voting_data)