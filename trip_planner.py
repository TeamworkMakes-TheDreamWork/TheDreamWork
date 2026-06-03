print("=== Road Trip Budget planner ===" )
print()
destination = input("please enter your destination  ")
print(f"we are going to {destination}")
distance = float(input("how many miles are we traveling "))
print(f"distance:{distance}miles")
mpg = int(input("please enter car's fuel efficiency in miles per gallon "))
gas_price = float(input("please enter your price per gallon of gas  "))
hotel_nights = int(input("please enter the number of nights in a hotel  "))
cost_per_night = float(input("please enter the cost of the hotel per night "))
food_budget = float(input("please enter the daily food budget  "))
total_gas_cost = distance/mpg * gas_price
gallons = distance/mpg
total_hotel_cost = cost_per_night * hotel_nights
days = (hotel_nights + 1)
total_food_cost = days * food_budget 
grand_total = total_hotel_cost + total_gas_cost + total_food_cost
print("--- Cost Breakdown ---" )
print(f"Gas:({gallons:.2f}gal @ ${gas_price:.2f}):  =   ${total_gas_cost:.2f}")
print(f"hotel( {hotel_nights}nights @ ${cost_per_night:.2f}):  =   {total_hotel_cost:.2f}")
print(f"food({days} @ ${food_budget:.2f})      =        {total_food_cost:.2f}   ")
print("-"*40 )
print(f"Estimated Total:                         {grand_total:.2f} ")