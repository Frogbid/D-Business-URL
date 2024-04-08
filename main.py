import urllib.parse

url = "https://www.bbb.org"

country = "us"

# All state names
state_codes = [
    "al", "ak", "az", "ar", "ca",
    "co", "ct", "de", "fl", "ga",
    "hi", "id", "il", "in", "ia",
    "ks", "ky", "la", "me", "md",
    "ma", "mi", "mn", "ms", "mo",
    "mt", "ne", "nv", "nh", "nj",
    "nm", "ny", "nc", "nd", "oh",
    "ok", "or", "pa", "ri", "sc",
    "sd", "tn", "tx", "ut", "vt",
    "va", "wa", "wv", "wi", "wy"
]

# City names organized into a two-dimensional array
city_names_2d = [
    ["birmingham", "montgomery", "huntsville", "mobile", "tuscaloosa"],  # Alabama
    ["anchorage", "fairbanks", "juneau", "sitka", "ketchikan"],  # Alaska
    ["phoenix", "tucson", "mesa", "chandler", "glendale"],  # Arizona
    ["little-rock", "fort-smith", "fayetteville", "springdale", "jonesboro"],  # Arkansas
    ["los-angeles", "san-diego", "san-jose", "san-francisco", "fresno"],  # California
    ["denver", "colorado-springs", "aurora", "fort-collins", "lakewood"],  # Colorado
    ["bridgeport", "new-haven", "stamford", "hartford", "waterbury"],  # Connecticut
    ["wilmington", "dover", "newark", "middletown", "smyrna"],  # Delaware
    ["jacksonville", "miami", "tampa", "orlando", "st-petersburg"],  # Florida
    ["atlanta", "augusta", "columbus", "macon", "savannah"],  # Georgia
    ["honolulu", "pearl-city", "hilo", "kailua", "waipahu"],  # Hawaii
    ["boise", "meridian", "nampa", "idaho-falls", "pocatello"],  # Idaho
    ["chicago", "aurora", "rockford", "joliet", "naperville"],  # Illinois
    ["indianapolis", "fort-wayne", "evansville", "south-bend", "carmel"],  # Indiana
    ["des-moines", "cedar-rapids", "davenport", "sioux-city", "iowa-city"],  # Iowa
    ["wichita", "overland-park", "kansas-city", "olathe", "topeka"],  # Kansas
    ["louisville", "lexington", "bowling-green", "owensboro", "covington"],  # Kentucky
    ["new-orleans", "baton-rouge", "shreveport", "lafayette", "lake-charles"],  # Louisiana
    ["portland", "lewiston", "bangor", "south-portland", "auburn"],  # Maine
    ["baltimore", "columbia", "germantown", "silver-spring", "waldorf"],  # Maryland
    ["boston", "worcester", "springfield", "lowell", "cambridge"],  # Massachusetts
    ["detroit", "grand-rapids", "warren", "sterling-heights", "lansing"],  # Michigan
    ["minneapolis", "st-paul", "rochester", "duluth", "bloomington"],  # Minnesota
    ["jackson", "gulfport", "southaven", "hattiesburg", "biloxi"],  # Mississippi
    ["kansas-city", "st-louis", "springfield", "independence", "columbia"],  # Missouri
    ["billings", "missoula", "great-falls", "bozeman", "butte"],  # Montana
    ["omaha", "lincoln", "bellevue", "grand-island", "kearney"],  # Nebraska
    ["las-vegas", "henderson", "reno", "north-las-vegas", "sparks"],  # Nevada
    ["manchester", "nashua", "concord", "derry", "dover"],  # New Hampshire
    ["newark", "jersey-city", "paterson", "elizabeth", "edison"],  # New Jersey
    ["albuquerque", "las-cruces", "rio-rancho", "santa-fe", "roswell"],  # New Mexico
    ["new-york-city", "buffalo", "rochester", "yonkers", "syracuse"],  # New York
    ["charlotte", "raleigh", "greensboro", "durham", "winston-salem"],  # North Carolina
    ["fargo", "bismarck", "grand-forks", "minot", "west-fargo"],  # North Dakota
    ["columbus", "cleveland", "cincinnati", "toledo", "akron"],  # Ohio
    ["oklahoma-city", "tulsa", "norman", "broken-arrow", "lawton"],  # Oklahoma
    ["portland", "salem", "eugene", "gresham", "hillsboro"],  # Oregon
    ["philadelphia", "pittsburgh", "allentown", "erie", "reading"],  # Pennsylvania
    ["providence", "warwick", "cranston", "pawtucket", "east-providence"],  # Rhode Island
    ["columbia", "charleston", "north-charleston", "mount-pleasant", "rock-hill"],  # South Carolina
    ["sioux-falls", "rapid-city", "aberdeen", "brookings", "watertown"],  # South Dakota
    ["nashville", "memphis", "knoxville", "chattanooga", "clarksville"],  # Tennessee
    ["houston", "san-antonio", "dallas", "austin", "fort-worth"],  # Texas
    ["salt-lake-city", "west-valley-city", "provo", "west-jordan", "orem"],  # Utah
    ["burlington", "south-burlington", "rutland", "barre", "montpelier"],  # Vermont
    ["virginia-beach", "norfolk", "chesapeake", "richmond", "newport-news"],  # Virginia
    ["seattle", "spokane", "tacoma", "vancouver", "bellevue"],  # Washington
    ["charleston", "huntington", "morgantown", "parkersburg", "wheeling"],  # West Virginia
    ["milwaukee", "madison", "green-bay", "kenosha", "racine"],  # Wisconsin
    ["cheyenne", "casper", "laramie", "gillette", "rock-springs"]  # Wyoming
]

category = [
    "driving-school",
    "driving-lessons",
    "training-program",
    "online-education",
    "traffic-school"
]

# Open a file in write mode
with open(country+"_urls.txt", "w") as file:
    # Iterate over each state code
    for state_code in state_codes:
        # Iterate over each state's list of cities
        for state_cities in city_names_2d:
            # Iterate over each city in the current state's list of cities
            for city in state_cities:
                # Construct the base URL for the current city
                city_base_url = f"{url}/{country}/{state_code}/{city}/category/"

                # Iterate over each category
                for cat in category:
                    # Construct the complete URL for the current city and category
                    city_cat_url = f"{city_base_url}{cat}"

                    # Write the URL to the file
                    file.write(city_cat_url + "\n")

                    # Print the URL (optional)
                    print(city_cat_url)

# Notify the user that the data has been saved
print("URLs have been saved to urls.txt file.")
