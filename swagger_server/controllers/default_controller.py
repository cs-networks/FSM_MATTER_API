import connexion
import six

from swagger_server.models.matter_response import MatterResponse  # noqa: E501
from swagger_server.models.action import Action  # noqa: E501
from swagger_server.models.link import Link  # noqa: E501
from swagger_server import util

from swagger_server.database.models.matter_model import matter_model

from swagger_server.fsm.matter_fsm import machine

from flask import url_for

def matter_get():  # noqa: E501
    """matter_get

    State of the Matter FSM # noqa: E501


    :rtype: MatterResponse
    """
    return_list = []
    state_list = []
    state_list.append(matter_model.get_all().to_obj())

    return_list = machine.get_actions_dict()
    
    self_link = Link( rel="self", href="http://localhost:8763/v1/matter" )
    
    print(state_list[0].state)
    machine.set_state(state_list[0].state)
    print(machine.get_current_state())
    
    resp = MatterResponse(_class='matter', properties=state_list[0], actions=return_list, links=self_link)
    return resp
