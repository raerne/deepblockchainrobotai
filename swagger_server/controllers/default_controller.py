from collections import defaultdict
from models.terrain_grid import FieldType
import connexion
import six
import json

from swagger_server.models.move_request import MoveRequest  # noqa: E501
from swagger_server import util
import requests

def move_post(body):  # noqa: E501
    """move_post

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MoveRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print(body.arena.terrain.map["(0,0)"])
    decoded = body.arena.terrain.decode_terrain(body.arena.bounds.rows, body.arena.bounds.cols)


    # select an enemy
    enemies = [r for r in body.arena.robots if r.player != body.arena.active_player]
    target_enemy = enemies[0]
    player = body.arena.robots[body.arena.active_player]

    rowdiff = target_enemy.position.row - player.position.row
    coldiff = target_enemy.position.col - player.position.col
    directions = []

    # move vertically
    row = player.position.row
    col = player.position.col
    stride = 1 if rowdiff > 0 else -1
    letter = "S" if rowdiff > 0 else "N"
    ramDirection = letter
    while(rowdiff != 0):
        rowdiff = rowdiff - stride # decreases/increases to zero
        nextrow = row + stride
        if(decoded[col][nextrow].field_type != FieldType.ROCK):
            row = nextrow
            directions.append(letter)

    stride = 1 if coldiff > 0 else -1
    letter = "E" if coldiff > 0 else "W"
    while(coldiff != 0):
        ramDirection = letter # update direction to where we move
        coldiff = coldiff - stride # decreases/increases to zero
        nextcol = col + stride
        if(decoded[nextcol][row].field_type != FieldType.ROCK):
            row = nextrow
            directions.append(letter)

    # prepare response
    shootEnergy = 0
    shootDirection = 0
    ram = True # just always ram

    # instead of calculating energy that is left simply take available - 1 to have one left to ram
    loadShield = player.energy - 1 - len(directions)


    response = {
        "requestId": body.request_uuid,
        "player": body.arena.active_player,
        "directions": directions,
        "loadShield": loadShield,
        "shootEnergy": shootEnergy,
        "shootDirection": shootDirection,
    }

    if ram:
        response["ramDirection"] = ramDirection
    print(json.dumps(response))

    url = 'http://localhost:8080/bout/{uuid}/moveResponse'.format(uuid=body.bout_uuid)
    print(url)
    res = requests.post(url, json=json.dumps(response))
    print('response from server:', res.text)
    # dictFromServer = res.json()

    return 200;

    # return json.dumps(response)
