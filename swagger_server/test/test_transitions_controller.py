# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestTransitionsController(BaseTestCase):
    """TransitionsController integration test stubs"""

    def test_do_condensate(self):
        """Test case for do_condensate

        Trigger transition condensate
        """
        response = self.client.open(
            '/v1/matter/{Id}/condensate'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_deionize(self):
        """Test case for do_deionize

        Trigger transition deionize
        """
        response = self.client.open(
            '/v1/matter/{Id}/deionize'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_deposit(self):
        """Test case for do_deposit

        Trigger transition deposit
        """
        response = self.client.open(
            '/v1/matter/{Id}/deposit'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_evaporate(self):
        """Test case for do_evaporate

        Trigger transition evaporate
        """
        response = self.client.open(
            '/v1/matter/{Id}/evaporate'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_freez(self):
        """Test case for do_freez

        Trigger transition freez
        """
        response = self.client.open(
            '/v1/matter/{Id}/freez'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_ionize(self):
        """Test case for do_ionize

        Trigger transition ionize
        """
        response = self.client.open(
            '/v1/matter/{Id}/ionize'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_melt(self):
        """Test case for do_melt

        Trigger transition melt
        """
        response = self.client.open(
            '/v1/matter/{Id}/melt'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_do_sublimate(self):
        """Test case for do_sublimate

        Trigger transition sublimate
        """
        response = self.client.open(
            '/v1/matter/{Id}/sublimate'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
