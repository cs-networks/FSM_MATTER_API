import connexion
import six

from swagger_server.models.matter_properties import MatterProperties  # noqa: E501
from swagger_server.models.matter_response import MatterResponse  # noqa: E501
from swagger_server.models.action import Action  # noqa: E501
from swagger_server.models.link import Link  # noqa: E501
from swagger_server import util

from swagger_server.database import db
from swagger_server.database.models.matter_model import matter_model

from swagger_server.fsm.matter_fsm import machine

from flask import url_for


def add_matter(body=None):  # noqa: E501
    """Add a new State Machine to the pool

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    print("Post FSM")
    if connexion.request.is_json:
        body = MatterProperties.from_dict(connexion.request.get_json())  # noqa: E501
        new_body = body.to_dict()
        new_body.pop('id')
        new_obj = matter_model(**new_body)
        db.session.add(new_obj)
        db.session.commit()
        print(new_obj.id)
    return 'do some magic!'


def get_by_id(matter_id):  # noqa: E501
    """Info for a specific Matter object

     # noqa: E501

    :param id: The id of the Matter object to retrieve
    :type id: float

    :rtype: MatterResponse
    """
    print("Getting FSM %s"  % matter_id)
    model_obj = matter_model.get_by_id(id=matter_id)
    
    if model_obj is None:
        return "Matter object not found", 404

    fsm = model_obj.to_obj()
    machine.set_state(fsm.state)
    action_list = machine.get_actions_dict(id=fsm.id)
    self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')

    resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
    return resp