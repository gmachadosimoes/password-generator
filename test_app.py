import os
import tempfile

import pytest

import app

homepage = 'index.html'

def test_client(client):
    assert homepage == 'index.html'

