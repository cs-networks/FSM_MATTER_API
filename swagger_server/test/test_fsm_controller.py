# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.matter_properties import MatterProperties  # noqa: E501
from swagger_server.models.matter_response import MatterResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFSMController(BaseTestCase):
    """FSMController integration test stubs"""

    def test_add_matter(self):
        """Test case for add_matter

        Add a new State Machine to the pool
        """
        body = MatterProperties()
        response = self.client.open(
            '/v1/matter',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_by_id(self):
        """Test case for get_by_id

        Info for a specific Matter object
        """
        response = self.client.open(
            '/v1/matter/{Id}'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
