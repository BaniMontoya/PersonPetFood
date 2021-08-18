# test_hello.py
import logging
from unittest import TestCase
import json
from app import app

LOGGER = logging.getLogger(__name__)


class AppTest(TestCase):

    def test_home(self):
        """
        [testing home path]
        """
        response = app.test_client().get('/')
        assert response.status_code == 200
