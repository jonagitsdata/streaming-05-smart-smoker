import csv
import pika
import webbrowser
import sys 
import time


def ask_user_for_admin_webpage():
    user_input = input("Do you want to see the RabbitMQ admin webpage? (yes/no): ")
    if user_input.lower() == "yes":
        print("The RabbitMQ admin webpage can be accessed at http://localhost:15672")
    else:
        print("The RabbitMQ admin webpage will not be displayed.")

def main_work():
    # Get a connection to RabbitMQ and a channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    # Delete the existing queues and declare them anew
    channel.queue_delete("01-smoker")
    channel.queue_delete("02-food-A")
    channel.queue_delete("02-food-B")
    channel.queue_declare("01-smoker")
    channel.queue_declare("02-food-A")
    channel.queue_declare("02-food-B")
    
    # Open the csv file for reading and create a csv reader
    with open("smoker-temps.csv", "r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) # skip header row

        # Read the data from the csv file
        for data_row in reader:
            # Get the values from the current row
            timestamp = data_row[0]
            smoker_temp = float(data_row[1])
            food_A_temp = float(data_row[2])
            food_B_temp = float(data_row[3])
            
            # Create binary messages from the tuples
            smoker_message = (timestamp, smoker_temp)
            food_A_message = (timestamp, food_A_temp)
            food_B_message = (timestamp, food_B_temp)
            
            # Publish each of the 3 messages to their respective queues
            channel.basic_publish(exchange='',
                                  routing_key="01-smoker",
                                  body=str(smoker_message))
            channel.basic_publish(exchange='',
                                  routing_key="02-food-A",
                                  body=str(food_A_message))
            channel.basic_publish(exchange='',
                                  routing_key="02-food-B",
                                  body=str(food_B_message))

if __name__ == "__main__":
    ask_user_for_admin_webpage()
    main_work()
