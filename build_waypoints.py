all_waypoints = [   "4919 Cave Run Drive, Houston, TX",
                    "Pedernales Falls State Park, Park Road 6026, Johnson City, TX",
                    "Big Bend National Park, TX",
                    "N Dean St & E Texas St, Marfa, TX 79843",
                    "Atalaya Mountain, Santa Fe, NM",
                    "Cherry Creek State Park, South Parker Road, Aurora, CO",
                    "Boulder Mountain Park, Boulder, CO",
                    "Powell Slough Waterfowl Management Area, Orem, UT",
                    "Bonneville Salt Flats, Tooele County, UT",
                    "Zion National Park, Washington County, UT",
                    "Grand Canyon National Park, AZ",
                    "Walnut Canyon National Monument, Walnut Canyon Road, Flagstaff, AZ",
                    "Red Rock Canyon National Conservation Area, Nevada 159, Las Vegas, NV",
                    "Mount Whitney, Inyo County, CA",
                    "Coachella Valley Fringe-Toed Lizard Preserve, Thousand Palms, CA",
                    "The Queen Mary, Queens Highway, Long Beach, CA",
                    "De las Flores, San Quintin, Mexico",
                    "Museum of Contemporary Art Santa Barbara, Santa Barbara, CA",
                    "Big Sur, Monterey County, CA",
                    "University of California, Santa Cruz, High Street, Santa Cruz, CA",
                    "Golden Gate Park, San Francisco, CA",
                    "Trancas Crossing Park, Trancas Street, Napa, CA",
                    "Yosemite National Park, CA",
                    "Indian Island, Eureka, CA",
                    "Lake Tahoe State Park, Nevada 28, Incline Village, NV",
                    "Burnside Bridge, Portland, OR",
                    "Discovery Park, Discovery Park Boulevard, Seattle, WA",
                    "Beacon Hill Park, Victoria, BC, Canada",
                    "Grand Teton National Park, Teton County, WY",
                    "Lake Superior Brewing Co, West Superior Street, Duluth, MN",
                    "Theodore Wirth Park, Theodore Wirth Parkway, Minneapolis, MN",
                    "Cherokee Marsh State Fishery Area, Madison, WI",
                    "2131 West Cortez Street, Chicago, IL",
                    "Millennium Park Path, Grand Rapids, MI",
                    "10 Witherell Street, Detroit, MI",
                    "Cherokee Park, Cochran Hill Road, Louisville, KY",
                    "Cheatham Wildlife Management Area, Ashland City, TN",
                    "Apache Cafe, 3rd Street Northwest, Atlanta, GA",
                    "Bonneau Ferry Wildlife Management Area, South Carolina 402, Cordesville, SC",
                    "University of North Carolina at Chapel Hill, Chapel Hill, NC",
                    "Monticello, Thomas Jefferson Parkway, Charlottesville, VA",
                    "Oriole Park At Camden Yards, West Camden Street, Baltimore, MD",
                    "Catskill Mountains, Shandaken, NY",
                    "Red Rocks Park, Central Avenue, South Burlington, VT",
                    "Congress Street, Portland, ME",
                    "Parc national du Mont-Saint-Bruno, St-Bruno-de-Montarville, QC, Canada",
                    "113 Mill Creek Road, South Chatham, MA"]

import googlemaps

gmaps = googlemaps.Client(key="AIzaSyAZ9p2YxcBSwvzferltOm6HvPpfUW9saH8")



from itertools import combinations

waypoint_distances = {}
waypoint_durations = {}

for (waypoint1, waypoint2) in combinations(all_waypoints, 2):
    try:
        route = gmaps.distance_matrix(origins=[waypoint1],
                                      destinations=[waypoint2],
                                      mode="driving", # Change this to "walking" for walking directions,
                                                      # "bicycling" for biking directions, etc.
                                      language="English",
                                      units="imperial")

        #print waypoint1, waypoint2
        # "distance" is in meters
        distance = route["rows"][0]["elements"][0]["distance"]["value"]

        # "duration" is in seconds
        duration = route["rows"][0]["elements"][0]["duration"]["value"]

        waypoint_distances[frozenset([waypoint1, waypoint2])] = distance
        waypoint_durations[frozenset([waypoint1, waypoint2])] = duration


    except Exception as e:
        print("Error with finding the route between %s and %s." % (waypoint1, waypoint2))

with open("my-waypoints-dist-dur.tsv", "wb") as out_file:
    out_file.write("\t".join(["waypoint1",
                              "waypoint2",
                              "distance_m",
                              "duration_s"]))

    for (waypoint1, waypoint2) in waypoint_distances.keys():
        out_file.write("\n" +
                       "\t".join([waypoint1,
                                  waypoint2,
                                  str(waypoint_distances[frozenset([waypoint1, waypoint2])]),
                                  str(waypoint_durations[frozenset([waypoint1, waypoint2])])]))
