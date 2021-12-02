import tweepy
from src.secrets import Consumer_Key, Access_Token, Access_Token_Secret, Consumer_Secret
from typing import List, Dict, Any
from src.constants import BRAZIL_WDE_ID
from src.connection import trends_collection


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """
    Get trend topics,

    Args:
        woe_id (int): identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """

    trends = api.get_place_trends(woe_id)

    return trends[0]["trends"]


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    auth = tweepy.OAuthHandler(consumer_key=Consumer_Key, consumer_secret=Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WDE_ID)
    trends_collection.insert_many(trends)
