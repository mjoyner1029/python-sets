# Define the sets of flight destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Find destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

# Find destinations unique to our airline
unique_destinations_ours = our_routes.difference(competitor_routes)

# Find destinations unique to the competitor's airline
unique_destinations_competitor = competitor_routes.difference(our_routes)

# Find destinations that neither airline shares
neither_shares = our_routes.symmetric_difference(competitor_routes)

# Display the results
print("Destinations both airlines fly to:", common_destinations)
print("Destinations unique to our airline:", unique_destinations_ours)
print("Destinations unique to competitor's airline:", unique_destinations_competitor)
print("Destinations that neither airline shares:", neither_shares)
