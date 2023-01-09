def retail_store():
 
  products = {
    "tshirt": 10,
    "jeans": 20,
    "hat": 15,
    "water bottle": 5,
    "laptop": 500,
    "stickers": 9,
    "pencils":16
  }
#prints greeting to user 
  print("Hello, how can I help you today? \nYou can ask me about store hours, location, available products, or prices. \nType 'exit' to end.")
 #creates a loop  
  while True:
   #waits for the user input
    message = input()
   #check if the imput is location 
    if message.lower() == "location":
     #prints the store location 
      print("Our store is located at Manor.")
   #check if the imput is store hours 
    elif message.lower() == "store hours":
     #prints the store hours
      print("Our store is open from 8am to 10pm every day.")
   #check if the imput is available products
    elif message.lower() == "available products":
     #prints a list of the available products 
      print("We have the following products available in our store:")
      for product in products:
        print(product)
   #check if the the imput is prices
    elif message.lower() == "prices":
    #prints a message for asking the specific price of a product
      print("If you have a specific product in mind, you can ask me about its price and I'll let you know. You can use the following phrase(what is the price of) ")
    #checks if the imput starts with "what is the price of"
    elif message.lower().startswith("what is the price of "):
     #extracts the product name from the message
      product = message[len("what is the price of "):]
    #checks if the product is in the dictionary
      if product in products:
      #prints the price of the product 
        print(f"The price of {product} is {products[product]}.")
      #prints a message if the product is not in the dictionary
      else:
        print(f"I'm sorry, we do not have {product} in the store at the moment.")
   #ends the program if the imput is exit
    elif message.lower() == "exit":
     #prints a message if the imput is exit 
      print("Have a nice day")
      break
   #prints a message if the chatbot do no understand an imput
    else:
      print("I'm sorry, I didn't understand your question. Could you repeated it?")
#executes the function
retail_store()
