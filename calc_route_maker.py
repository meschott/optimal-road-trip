# Paste your optimal route after the equal sign (=) here
optimal_route = ('4919 Cave Run Drive, Houston, TX', 'Pedernales Falls State Park, Park Road 6026, Johnson City, TX', 'Big Bend National Park, TX', 'N Dean St & E Texas St, Marfa, TX 79843', 'Atalaya Mountain, Santa Fe, NM', 'Walnut Canyon National Monument, Walnut Canyon Road, Flagstaff, AZ', 'Grand Canyon National Park, AZ', 'Coachella Valley Fringe-Toed Lizard Preserve, Thousand Palms, CA', 'De las Flores, San Quintin, Mexico', 'The Queen Mary, Queens Highway, Long Beach, CA', 'Museum of Contemporary Art Santa Barbara, Santa Barbara, CA', 'Big Sur, Monterey County, CA', 'University of California, Santa Cruz, High Street, Santa Cruz, CA', 'Golden Gate Park, San Francisco, CA', 'Trancas Crossing Park, Trancas Street, Napa, CA', 'Lake Tahoe State Park, Nevada 28, Incline Village, NV', 'Yosemite National Park, CA', 'Mount Whitney, Inyo County, CA', 'Red Rock Canyon National Conservation Area, Nevada 159, Las Vegas, NV', 'Zion National Park, Washington County, UT', 'Powell Slough Waterfowl Management Area, Orem, UT', 'Bonneville Salt Flats, Tooele County, UT', 'Burnside Bridge, Portland, OR', 'Beacon Hill Park, Victoria, BC, Canada', 'Discovery Park, Discovery Park Boulevard, Seattle, WA', 'Grand Teton National Park, Teton County, WY', 'Boulder Mountain Park, Boulder, CO', 'Cherry Creek State Park, South Parker Road, Aurora, CO', 'Theodore Wirth Park, Theodore Wirth Parkway, Minneapolis, MN', 'Lake Superior Brewing Co, West Superior Street, Duluth, MN', 'Cherokee Marsh State Fishery Area, Madison, WI', '2131 West Cortez Street, Chicago, IL', 'Millennium Park Path, Grand Rapids, MI', '10 Witherell Street, Detroit, MI', 'Cherokee Park, Cochran Hill Road, Louisville, KY', 'Cheatham Wildlife Management Area, Ashland City, TN', 'Apache Cafe, 3rd Street Northwest, Atlanta, GA', 'Bonneau Ferry Wildlife Management Area, South Carolina 402, Cordesville, SC', 'University of North Carolina at Chapel Hill, Chapel Hill, NC', 'Monticello, Thomas Jefferson Parkway, Charlottesville, VA', 'Oriole Park At Camden Yards, West Camden Street, Baltimore, MD', 'Catskill Mountains, Shandaken, NY', 'Red Rocks Park, Central Avenue, South Burlington, VT', 'Congress Street, Portland, ME', '113 Mill Creek Road, South Chatham, MA')
optimal_route = list(optimal_route)
optimal_route += [optimal_route[0]]
subset = 0

while subset < len(optimal_route):

    waypoint_subset = optimal_route[subset:subset + 10]
    output = "calcRoute(\"%s\", \"%s\", [" % (waypoint_subset[0], waypoint_subset[-1])
    for waypoint in waypoint_subset[1:-1]:
        output += "\"%s\", " % (waypoint)

    if len(waypoint_subset[1:-1]) > 0:
        output = output[:-2]

    output += "]);"
    print(output)
    print("")
    subset += 9
