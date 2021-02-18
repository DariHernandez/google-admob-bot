#! python3

import os, random

def get_ramdom_address (): 
    """
    Function to manage random addres from file "address.txt"
    """

    # Get list of address
    current_dir = os.path.dirname (__file__)
    address_path = os.path.join (current_dir, "address.txt")
    address_file = open (address_path, "r")
    address_list = address_file.readlines()
    address_file.close ()

    random_address = random.choices (address_list)[0].strip()
    print (random_address)
    
    zip_code = random_address [-5:]
    state = random_address [-8:-6]
    city = random_address[random_address.find (",")+2:random_address.find(state)]
    street = random_address[:random_address.find (",")]

    return {
        "zip_code":zip_code,
        "state":state, 
        "city":city,
        "street":street
    }