"""This file gives our app the ability to respond to text queries for specific styles of beer."""
import json
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import requests


APP = Flask(__name__)


def count_beers(query_results):
    "Returns the number of beers that match the user's request."
    data = json.loads(query_results)
    return len(data)


@APP.route("/", methods=['GET', 'POST'])
def handle_sms():
    """This function provides the response for twilio test message requests."""
    style = request.form['Body']
    query_results = requests.get("http://beerapi/current?style={}".format(style))
    #Handles any situation where an attempt to get a response failed.
    if query_results.status_code != 200:
        response = MessagingResponse()
        response.message("Sorry, I cannot handle your request. Please try again later!")
        return str(response)

    count = count_beers(query_results.text)

    response = MessagingResponse()
    if count == 0:
        response.message("Sorry, no results for stout")
    elif count == 1:
        response.message("There is 1 beer with the style {}".format(style))
    else:
        response.message("There are {} beers with the style {}.".format(count, style))
    return str(response)


if __name__ == "__main__":
    APP.run(debug=True)
