### README.md
## streaming-05-smart-smoker project
## **Author: Jonathan Nkangabwa**
## **Date: February 7th, 2023**

## OVERVIEW 

## Simple Producer for Barbecue Smoker

This code takes information from a CSV file (smoker-temps.csv) and creates a producer with three queues. Each column in the CSV will be sent to its own queue.

## Prerequisites
Before running the code, make sure you have:

- Pika
- RabbitMQ (https://www.rabbitmq.com/download.html for setup)
- An active conda environment
- An open Anaconda prompt terminal

## Files Needed
- bbq_producer.py (check host and show_offer)
- smoker-temps.csv (4 columns: time, smoker temp, food A temp, food B temp)
- .gitignore file (choosen from previous repo project)

## Running the Program
Review and update bbq_producer.py if needed
Open smoker-temps.csv
Run bbq_producer.py

## Monitoring Barbecue Smoker Temperatures
We use temperature sensors to track the temperature of the smoker and food while barbecuing. This information is considered time-series data or data in motion.

## Reading Temperatures
Our thermometer records the temperature of the smoker, Food A, and Food B every 30 seconds (2 readings per minute).

## Significant Events
We want to know if:

The smoker temperature drops more than 15°F in 2.5 minutes (smoker alert!)
Food temperature changes less than 1°F in 10 minutes (food stall!)

Smart System
We'll use Python to:

- Simulate temperature readings from the smoker and foods
- Create a producer to send readings to RabbitMQ
- Create three consumers to monitor each temperature stream (module 6 with consumers)
- Check for significant events

## Optional Alerts
We can receive email or text alerts when significant events occur by adding outgoing email functionality.

## Screenshot of Program Running:
## Screenshot in Anaconda Prompt
![smokerv1](smoker_conda.png)

