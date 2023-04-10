from django.shortcuts import render
from django.http import HttpResponse
import logging

def index(request):
    logger = logging.getLogger("Polls_Logger")
    logger.warning("Payload", request)
    return HttpResponse("Welcome to Polls website")

