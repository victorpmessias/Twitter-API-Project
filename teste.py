from src.services import _get_trends
from unittest import mock


def test_get_trends_with_sucess():
    # Arrange
    mock_api = mock.Mock()
    mock_api.get_place_trends.return_value = [
        {
            "trends": [
                {
                    "name": "#ITLLBEOKAY",
                    "url": "http://twitter.com/search?q=%23ITLLBEOKAY",
                }
            ]
        }
    ]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == [
        {
            "name": "#ITLLBEOKAY",
            "url": "http://twitter.com/search?q=%23ITLLBEOKAY",
        }
    ]
