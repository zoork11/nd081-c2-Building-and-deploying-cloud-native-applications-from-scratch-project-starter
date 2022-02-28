import json
import logging
import azure.functions as func


def main(event: func.EventHubEvent):

    logging.info(f'Function triggered to process a message: {event.get_body().decode()}')



