# #Prompt User for Weather Input
# weather = input("What's the weather like today? (sunny/rainy/cold): ")

# #Provide Clothing Recommendations
# if weather == "sunny":
#     print("Wear a t-shirt and sunglasses.")
# elif weather == "rainy":
#     print("Don't forget your umbrella and a raincoat.")
# elif weather == "cold":
#     print("Make sure to wear a warm coat and a scarf.")
# else:
#     print("Sorry, I don't have recommendations for this weather.")


current_weather = True

while current_weather:
    #Prompt User for Weather Input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    #Provide Clothing Recommendations
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
        break
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
        break
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
        break
    else:
        print("Sorry, I don't have recommendations for this weather.")
