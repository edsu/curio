#!/usr/bin/env python

import curio
import pytest

def test_curio():
    c = curio.Cabinet("test-data")
    assert len(c.items) == 1821