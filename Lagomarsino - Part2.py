#Create a command-line interface that enables a user to perform analysis and visualise data by 
#entering queries through the terminal.


import pandas as pd 
listings = pd.read_csv('airbnb_listings_v1.csv')

# Function1: To get the 5 cheapest listings per neighbourhood, with the detail of it's url, name, and price.

def cheapest_listings_by_neighborhood(neighborhood):
    neighborhood_data = listings[listings['neighbourhood_cleansed'] == neighborhood]
    cheapest_listings = neighborhood_data.sort_values(by='price').head(5)

    return cheapest_listings

neighborhood_name = input("Please enter the neighborhood name: ")
cheapest_listings = cheapest_listings_by_neighborhood(neighborhood_name)
print("Cheapest 5 listings in", neighborhood_name, ":")
print(cheapest_listings[['listing_url', 'name', 'price']])

# Function2: To get the detail of the amenities a listing has.
def get_listing_amenities():
    try:
        user_listing_id = int(input("Please enter the listing ID: "))
        listing_amenities = listings.loc[listings['id'] == user_listing_id, 'amenities'].values[0]
        return listing_amenities
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid listing ID.")

amenities_result = get_listing_amenities()

# Function3: To see if a host has other listings, and it's details.
def host_listings(host_id):
    listings_info = listings[listings['host_id'] == host_id]
    return listings_info

try:
    user_host_id = int(input("Enter the host ID: "))
    listings_info = host_listings(user_host_id)

    if not listings_info.empty:
        print(f"-The host with ID {user_host_id} has {listings_info['id'].nunique()} listings.")
        print("-Details of host listings:")
        print(listings_info[['id', 'listing_url']])
    else:
        print(f"No listings found for the host with ID {user_host_id}.")
except ValueError:
    print("Invalid input. Please enter a valid host ID.")







