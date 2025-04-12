"""app entry"""
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)



@app.get("/")
def index():
    """shows index"""

    return increase_page_views()

@app.get("/incr")
def increase_page_views():
    """increases the page views"""
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500

    return f"This page has been seen {page_views} times."



@app.get("/decr")
def decrease_page_views():
    """decreases the page views"""
    try:
        page_views = redis().decr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500

    return f"This page has been seen {page_views} times."


@cache
def redis():
    """returns the redis object"""
    return Redis()
