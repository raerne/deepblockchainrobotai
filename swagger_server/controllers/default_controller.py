import connexion
import six

from swagger_server.models.move_request import MoveRequest  # noqa: E501
from swagger_server import util


def move_post(body):  # noqa: E501
    """move_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MoveRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
