"""app entry"""
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)

@app.get("/")
def index():
    """shows index"""
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500
    
    return f"This page has been seen {page_views} times."




@cache
def redis():
    """returns the redis object"""
    return Redis()
