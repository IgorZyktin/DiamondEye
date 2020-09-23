# -*- coding: utf-8 -*-

"""Fixtures.
"""
import numpy as np
import pytest


@pytest.fixture
def ref_blacky_sig():
    return np.array([0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, -1, 1, -1, 1, 1, 0,
                     0, 0, -1, 1, -1, 1, 2, 0, 0, 0, -1, 2, -1, 2, 2, 0, 0,
                     0, -2, 1, -2, -1, -1, 0, 0, 0, -1, 1, -2, -2, -2, 0, 0, 0,
                     -1, 1, -2, -2, 1, 0, 0, 0, -1, -2, -2, 1, -1, 0, 0, 0, 2,
                     0, 2, 2, 0, 0, -1, 1, 0, 1, 0, 1, 2, -1, -1, 1, -1, 1,
                     -1, 1, 2, -1, -1, 1, -1, 2, 1, 2, 2, -2, -2, 2, -2, 2, -2,
                     2, 2, -2, 1, 2, -2, 1, -1, 1, -2, 1, 2, 2, -1, -1, -1, -2,
                     -2, 2, 2, 2, 1, 2, -2, -2, 2, -1, -1, -2, -2, -1, -2, -2,
                     -1,
                     1, -2, 0, 1, 0, -1, -1, 0, 0, -1, 1, 0, 1, 0, 2, 2, -2,
                     -1, -1, -1, 1, 1, 2, 2, -2, -2, 2, -1, 2, 2, 2, 2, -2, -2,
                     1, -2, 1, -2, 2, -2, -2, -1, 1, -1, -2, 2, -2, -1, 2, 2,
                     2,
                     2, 1, 1, 2, -1, 2, 2, 2, -1, 2, 2, -1, 2, -2, 2, 1, -2,
                     1, -2, 1, -1, 1, 1, 0, -1, 0, -1, -1, 0, 0, -2, -1, 0, 2,
                     0, 1, 2, -2, -2, -2, -2, 2, -2, -2, -2, -2, -2, 2, -2, 2,
                     -2,
                     -2, 2, -2, -2, -2, -2, -2, -2, -1, -2, 2, 2, -1, 2, 1, 2,
                     2,
                     1, 1, -2, -2, -1, -2, 1, -1, -2, 1, 1, 2, 2, 2, 2, 1, 2,
                     -2, -1, 1, -2, -1, -2, -1, -1, 1, 1, 0, 1, 0, -1, -1, 0,
                     0,
                     -1, 2, 0, 1, 0, -1, 1, -2, 2, 2, -1, 1, -1, -1, 1, 2, 2,
                     2, -1, 2, -2, -1, 2, -2, 1, -2, -2, -2, -2, -2, -1, 2, -2,
                     -1,
                     2, -1, -2, 1, -2, -1, 1, -2, 1, -2, 1, -2, -1, 2, -1, 2,
                     2,
                     2, -2, 1, 2, -2, 1, 1, -2, -1, -2, -1, -2, 1, 1, 0, 1, 0,
                     -1, -2, 0, 0, 1, 1, 0, 1, 0, -1, -1, -1, 1, 2, -1, 1, -1,
                     -1, -1, -1, 1, 2, -1, 2, -2, -1, -1, -2, 2, 2, -2, 2, -2,
                     -2,
                     1, 1, -1, -1, -2, -2, -2, -2, -2, 2, 2, 2, 2, 2, -2, 1,
                     -2,
                     1, -1, 2, -2, 1, -2, -2, -2, -2, 1, 1, -1, -2, -2, -2, -2,
                     2,
                     2, 0, 2, 0, -2, -2, 0, 0, 1, 1, 0, 1, 0, -1, -1, 1, 1,
                     2, -1, 1, -1, -1, -1, 1, 1, 2, -1, 1, -1, -1, -1, 1, 2, 2,
                     -1, 2, -2, -1, 2, -1, 2, 2, -2, 2, -2, -2, -2, 2, -1, 2,
                     -2,
                     -2, -2, -2, -2, 2, 2, 2, 2, 2, -2, -2, -2, 2, 2, 2, -2,
                     -2,
                     -2, -2, -2, 2, 2, 0, 2, 0, -2, -2, 0, 0, 1, 1, 0, 1, 0,
                     -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 2, -1, 1, -1,
                     -1,
                     -1, 1, 1, 2, -1, 2, -1, -1, 1, -2, 2, 2, -2, -2, -2, -2,
                     -2,
                     2, 2, 2, 2, -1, -1, -1, -2, 2, 2, 2, 1, -1, -1, -1, -1, 2,
                     2, 2, 1, -1, -1, -1, -1, 2, 2, 0, 1, 0, -1, -1, 0, 0, 1,
                     1, 0, 1, 0, 0, 0, 1, 1, 1, -1, -1, 0, 0, 0, 1, 1, 1,
                     1, 1, 0, 0, 0, 1, 1, 2, -1, 1, 0, 0, 0, -1, 2, 1, -1,
                     1, 0, 0, 0, 2, 1, 1, -1, -1, 0, 0, 0, 2, 1, 1, 1, 1,
                     0, 0, 0, 1, 1, 1, -1, -1, 0, 0, 0, 1, 1, 0, 1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_blurry_sig():
    return np.array([0, 0, 0, 0, -1, 0, -2, 1, 0, 0, 0, 1, -1, -2, 1, 2, 0,
                     0, 0, 1, 2, 1, 2, 1, 0, 0, 0, -2, -1, 1, -1, -1, 0, 0,
                     0, 1, 1, 1, 1, 2, 0, 0, 0, -1, -1, 1, 2, 2, 0, 0, 0,
                     1, -1, 2, 2, -1, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, -1,
                     0, 1, 1, 0, 0, 2, 2, 0, 2, 0, -1, -1, -1, -1, -1, -2, 2,
                     -2, -2, 1, -2, -2, -1, -2, -1, -2, -2, -2, -1, 1, -1, 1,
                     1, -1,
                     -1, 2, 1, -1, -1, -1, 2, -1, 1, 2, -2, -2, -2, -2, -1, -2,
                     -1,
                     -2, -2, -2, -2, 1, -2, 1, -1, -2, 1, -1, -1, 2, -1, 2, 1,
                     1,
                     -1, -1, 0, 1, 0, 1, 1, 0, 0, 1, 2, 0, 1, 0, -1, 2, 1,
                     2, 2, -1, 2, -1, 2, 2, -1, 2, 1, -2, -1, 2, 1, 1, 2, 1,
                     1, 1, 2, 1, 1, -2, -2, -1, 2, -2, 1, -2, -2, -2, -2, 1,
                     -1,
                     -1, -1, -2, -2, -2, 2, 1, -2, 1, -2, -2, -1, -1, 2, -1,
                     -1, 2,
                     -1, 1, 1, 1, -1, -1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 2,
                     0, 2, 2, -2, -2, -2, -2, -1, 2, 2, -1, -2, -1, -1, 1, -1,
                     2,
                     1, 2, -1, -1, 2, 1, -2, 1, 2, -1, 2, 2, 2, 2, 1, 2, 2,
                     2, 2, 2, 2, -1, 1, 1, 2, 2, 2, 1, -1, -1, 1, 1, 2, -1,
                     1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 0, 1, 0, -1, 1, 0,
                     0,
                     -2, -2, 0, 2, 0, 2, 2, -2, -2, -2, -2, -2, -1, 1, -2, 1,
                     -1,
                     -1, 2, 2, 2, 2, 2, -2, -2, -2, -2, -2, -1, -1, -2, 1, -2,
                     -1,
                     2, 1, 2, 1, 1, -2, -2, -1, -1, 2, 1, -1, 1, -2, -2, -2,
                     -2,
                     -2, -2, -2, -2, 1, 1, 1, 2, 1, 2, 1, 1, 1, -1, 0, -1, 0,
                     -1, -1, 0, 0, -2, 1, 0, 1, 0, 2, 2, -2, -1, -2, -1, -2, 1,
                     1, -2, 2, -2, 1, 2, 1, 2, 1, -2, -2, 1, -2, -1, -2, -1,
                     -2,
                     -1, 2, -1, -1, 2, -1, -2, 1, 2, -1, 1, 2, 1, 1, 1, 2, 1,
                     -1, 2, -2, -1, -2, 2, -1, -2, 2, -1, 1, 2, -1, 2, 1, 1,
                     -1,
                     1, 0, 1, 0, 1, 1, 0, 0, -2, -1, 0, 1, 0, 2, -2, -2, -1,
                     -2, -1, -2, 1, -2, -2, 2, -1, 1, 2, -2, 2, 2, -1, 2, 2, 2,
                     2, 2, 2, 2, 2, 1, -1, -1, -2, 2, 1, 2, -2, -2, -2, -2, -2,
                     -2, 1, -2, -2, -1, 1, -2, 2, -1, -2, 1, -2, 2, -1, -1, 1,
                     1,
                     1, -1, 1, -1, -1, 0, -1, 0, -1, 1, 0, 0, -2, -1, 0, -2, 0,
                     -2, -1, 2, 2, -2, 2, 1, 1, 2, 1, 2, -2, -2, -1, -2, 2, -1,
                     -1, 1, -2, -1, 2, 2, 2, 2, 2, -2, -2, -1, -2, -2, -1, 2,
                     2,
                     2, 2, 2, 2, 2, 2, 2, 2, 2, -1, -1, -2, -2, 2, 2, -2, 2,
                     1, 1, 2, 1, 2, 1, 1, -1, -1, 0, -1, 0, -1, -1, 0, 0, 2,
                     -1, 0, 2, 0, 0, 0, 1, -2, -2, -2, -2, 0, 0, 0, -1, 1, -2,
                     2, -1, 0, 0, 0, 1, -2, 1, 1, 2, 0, 0, 0, -2, -2, -2, -2,
                     -1, 0, 0, 0, -2, -2, -2, 1, -2, 0, 0, 0, -2, -2, -2, 2,
                     -2,
                     0, 0, 0, 2, -1, 1, 2, -1, 0, 0, 0, -1, 1, 0, 1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_comfy_sig():
    return np.array([0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, -1, -1, 1, -1, 2, 0,
                     0, 0, 1, -1, 1, 2, 1, 0, 0, 0, 1, -1, 2, 1, 1, 0, 0,
                     0, 1, 1, 1, 1, 1, 0, 0, 0, -1, 1, -1, 1, 1, 0, 0, 0,
                     -1, 1, -1, -1, 1, 0, 0, 0, -1, 2, -1, 1, 2, 0, 0, 0, -2,
                     0, -1, 1, 0, 0, -1, -1, 0, -1, 0, 1, 2, -1, 1, -1, 1, 2,
                     1, 2, -1, -2, -2, -2, -2, -2, -1, -2, -2, -1, -1, -1, 2,
                     -1, -1,
                     -1, -1, -1, -1, 1, 1, 1, -1, -1, -2, -1, -1, 1, -1, 1, -1,
                     -2,
                     -1, -1, 1, 1, -1, 1, -2, -1, -2, -1, -1, 1, -1, 1, -2, -2,
                     2,
                     -2, -1, 0, -1, 0, -2, 1, 0, 0, -1, -1, 0, 2, 0, -2, -1,
                     -2,
                     -2, 1, -2, -2, -2, -2, -2, 1, 2, 1, 2, -1, -1, -2, -2, 2,
                     1,
                     1, 1, -1, -2, -2, -1, 1, 1, 1, 1, -1, -2, 1, -1, 2, 2, 2,
                     1, 2, 2, 1, 2, 1, 1, 2, -2, -2, -1, 2, 1, 2, 2, 2, 2,
                     2, 2, 2, 2, -2, -1, 0, -2, 0, -2, 1, 0, 0, 2, 2, 0, 2,
                     0, 1, 2, 1, 2, 1, -2, -2, -1, 1, 1, 2, 2, 2, 2, -1, 2,
                     2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, -1, -2, -2, -1, 1, 2,
                     1, 1, -1, 1, 1, 2, 2, 2, 2, -2, -2, -2, -2, -2, -2, -2,
                     -2,
                     -1, -2, 2, 2, 2, -1, -1, 1, -2, -1, 0, -2, 0, -2, -2, 0,
                     0,
                     -1, 1, 0, 2, 0, 2, 2, -2, -1, -2, -2, -1, 1, 2, 1, -1, -2,
                     -2, 1, -1, 2, 2, 2, -2, -2, -1, 1, 1, 2, 2, 2, -2, -2, -2,
                     -1, -1, 1, 1, -1, -1, -2, 2, 1, 1, 2, 1, -1, -2, 2, 1, -1,
                     -1, 1, -1, -1, 2, 1, 2, 1, 2, -1, 1, -2, -1, 2, 0, -2, 0,
                     -2, -2, 0, 0, -2, -1, 0, 2, 0, -1, 2, -2, -2, -2, -2, -2,
                     -2,
                     1, -2, -1, -2, -2, 2, 1, 2, -1, -2, -2, -2, -1, -1, -1,
                     -1, -2,
                     -2, -2, -1, -2, 1, -1, -2, -2, -2, 1, -1, -1, 1, -2, -1,
                     -2, -1,
                     1, 1, 1, 2, 1, -1, 1, 1, 1, -1, 2, -1, -2, 1, -1, -1, 2,
                     2, 0, 2, 0, 2, 2, 0, 0, 1, 2, 0, 2, 0, 1, 2, -2, -1,
                     -2, -2, -2, -2, -1, -2, 2, 1, 1, 2, -2, 2, -2, -2, 2, 2,
                     2,
                     2, 1, 1, -1, -1, 2, 2, 1, -1, -1, -1, -1, 1, 2, 2, 1, 1,
                     2, -1, 1, 2, 1, -1, -1, -2, -1, -1, -1, -2, -1, 1, -2, 1,
                     -1,
                     1, -2, 2, 1, -2, 0, 1, 0, -2, 2, 0, 0, -1, 2, 0, 2, 0,
                     -2, 1, -2, 1, -2, -2, -2, -2, -2, -1, 2, 2, -1, 2, -1, 2,
                     2,
                     2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, -1, 1, 2, 1, -1,
                     -1, -1, 1, -1, 1, 1, -1, 1, -2, 1, -1, -1, -2, -2, -1, -2,
                     2,
                     2, 2, 2, 2, 2, 1, 2, -2, -2, 0, -2, 0, -2, 1, 0, 0, 2,
                     2, 0, 2, 0, 0, 0, -1, 2, -2, -2, 2, 0, 0, 0, 1, -2, -2,
                     -2, -2, 0, 0, 0, -2, -2, -2, 2, -2, 0, 0, 0, -1, -1, -1,
                     2,
                     -2, 0, 0, 0, 1, 1, 2, 2, 2, 0, 0, 0, -1, 1, -2, -2, -2,
                     0, 0, 0, 2, -1, 2, 2, 2, 0, 0, 0, -2, -1, 0, -2, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_spoony_sig():
    return np.array([0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, -2, 1, 2, -1, 2, 0,
                     0, 0, -1, 1, -2, 1, -1, 0, 0, 0, -1, -1, 1, -1, -1, 0, 0,
                     0, 1, -1, 1, -1, 1, 0, 0, 0, 1, -1, 1, 2, -1, 0, 0, 0,
                     1, -2, 2, -1, -2, 0, 0, 0, 2, 2, 2, -1, 2, 0, 0, 0, -2,
                     0, -2, 1, 0, 0, -2, -2, 0, -2, 0, -2, -1, -2, 1, 2, 2, 2,
                     -1, 2, 1, -2, -1, -1, -2, -1, -1, -2, -2, 1, 1, -1, 1, -1,
                     -2,
                     -2, -2, 1, 1, -1, 1, 1, -2, -2, -2, -1, -2, -2, -1, -2,
                     -2, -2,
                     -2, 1, 1, -2, 2, -2, -2, -1, -1, 2, 1, 2, 2, 2, 1, 2, 2,
                     -2, -1, 0, -2, 0, -2, -2, 0, 0, 2, 1, 0, 2, 0, 1, 1, 1,
                     -2, 1, -2, -2, -2, -2, -2, -1, 2, 2, 2, -2, -1, -1, 1, 2,
                     2,
                     2, 2, 1, 2, 2, 1, 2, 2, 2, -1, -1, 2, 1, 1, 2, 2, 2,
                     1, 2, 1, 1, 2, 2, 1, -1, -2, 1, -1, 2, 2, 1, -2, 2, -1,
                     -1, 2, 1, 2, -2, 2, 0, 1, 0, 1, 2, 0, 0, -1, 2, 0, 1,
                     0, 1, 1, -1, 2, 1, -1, 1, 1, 1, 2, 2, 1, -2, -1, 1, -1,
                     2, -1, -1, -2, -2, -1, -2, 1, -1, -1, -1, -1, -1, 2, 1, 2,
                     1,
                     2, -1, -1, 1, -1, 2, 1, 2, 2, -2, -2, -2, -2, -1, -2, -1,
                     -2,
                     -2, -1, -1, 1, 2, 1, -1, -1, -2, -2, 0, -2, 0, -2, -2, 0,
                     0,
                     -1, -1, 0, -1, 0, 1, 1, -1, -1, 1, 1, 2, 1, 1, 2, -2, -2,
                     -1, -2, -2, -1, 2, 2, 1, 1, -2, 2, -1, 2, 2, 2, 1, -1, -1,
                     1, 1, 2, 2, 2, -2, -2, 2, -1, 2, 2, 2, 2, -2, 1, -1, -2,
                     -2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, -1, 0,
                     2, 2, 0, 0, -1, -1, 0, 1, 0, -2, 1, -1, -1, 1, -1, 2, -2,
                     1, 1, -2, -2, -2, -2, 1, -2, -2, 1, -2, -2, -2, -1, -1,
                     -2, 1,
                     1, -2, -2, -2, 1, -1, 1, 1, 1, -2, -2, -2, 1, -1, 1, 1, 1,
                     -2, -1, -2, 1, -1, 1, 2, -1, -1, -2, -2, 1, 1, 2, -1, -1,
                     -2,
                     -2, 0, -1, 0, -1, -1, 0, 0, 2, 2, 0, 2, 0, 2, 2, -1, -1,
                     2, -2, 1, -1, -1, -1, -1, 2, 2, -1, 2, -1, -1, 1, -1, -1,
                     -1,
                     -2, -1, -2, -2, -1, -1, -1, -1, 1, -1, -2, -1, -2, -1, -1,
                     -1, 1,
                     1, -1, -2, -2, -1, -2, -2, -1, -2, -2, -2, -2, 1, 1, 1, 2,
                     -1,
                     -1, -1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, -2, 1, 0, 1, 0,
                     2, 2, -2, 1, 1, -1, 1, 2, 2, 2, 1, 1, 2, -1, 1, 2, 2,
                     2, -1, 2, 2, -1, 1, 1, 1, -2, 1, 1, 1, -1, -2, -1, -2, -2,
                     2, 2, 2, 2, 2, 2, -2, -2, 2, 2, 1, -2, -1, -2, -2, -2, 2,
                     1, -1, 1, 1, -2, -2, -2, -1, -1, 0, -1, 0, -2, -2, 0, 0,
                     -2,
                     -2, 0, 1, 0, 0, 0, -2, -2, -2, -1, -1, 0, 0, 0, -2, -2,
                     -1,
                     1, -1, 0, 0, 0, -2, -1, 1, 1, -2, 0, 0, 0, 2, 2, -2, 2,
                     -2, 0, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 2, 2, -1, 1,
                     0, 0, 0, 2, 2, 2, -1, 1, 0, 0, 0, 2, 2, 0, -1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_wildy_sig():
    return np.array([0, 0, 0, 0, 2, 0, -1, -1, 0, 0, 0, -2, -1, -2, -2, -1, 0,
                     0, 0, 1, -2, -2, -1, -1, 0, 0, 0, 2, -2, 2, 2, -2, 0, 0,
                     0, 2, 2, 2, 1, 2, 0, 0, 0, -2, 2, -2, -1, 2, 0, 0, 0,
                     -2, 2, -2, 2, -1, 0, 0, 0, -2, -1, 1, -2, -1, 0, 0, 0, 1,
                     0, -2, -1, 0, 0, 1, 2, 0, -1, 0, -1, 2, 1, 2, 2, 1, 2,
                     -1, 2, 2, 1, 1, -2, -2, -1, 1, -1, -1, 1, -2, -2, 1, -2,
                     -1,
                     -1, -2, 2, -1, 2, 2, 2, 2, 2, -1, -2, 1, 2, -2, 2, 2, -2,
                     2, -2, -2, -1, -2, -2, -2, -2, -1, 1, 2, 2, 2, 1, 1, 2, 2,
                     1, 1, 0, -1, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, -1, 2, -2,
                     -2, -1, -2, -2, -2, -2, 1, -2, 1, 1, 2, 1, -1, 2, -2, 1,
                     1,
                     -2, -1, -1, 2, -2, -2, 2, -2, -2, 1, -2, -2, -2, -2, 1, 2,
                     2,
                     2, 2, 2, 2, 2, -2, 2, -1, -2, 1, -2, -2, 1, 1, -2, -1, -1,
                     1, -2, 1, 1, -2, -1, 0, -1, 0, -1, 1, 0, 0, 1, 2, 0, 2,
                     0, 2, 2, -2, 2, 1, -2, 2, -1, 1, -1, -1, -2, -2, -2, -2,
                     -2,
                     -2, -2, 2, 2, 2, 2, -1, 1, 1, 1, 2, 2, -2, 1, 1, 1, 1,
                     -2, 2, -2, 2, -1, 1, 1, -2, 1, -2, 2, 2, -1, 2, -2, -1, 2,
                     -1, -1, 1, -2, 1, -2, -1, -1, -1, -1, 0, -1, 0, -1, -1, 0,
                     0,
                     -2, 1, 0, 2, 0, 2, 2, -2, -1, 2, -2, -2, 1, -1, 1, 1, 2,
                     -1, 2, -1, 2, 2, -1, 2, -1, -1, 1, 1, 2, -1, -1, -1, -1,
                     -1,
                     -1, -2, -1, -1, -2, 2, 2, 2, 2, 2, 2, 2, 2, -1, 1, 2, -2,
                     2, -2, -1, 2, -2, 1, 1, -2, 1, -2, 1, -2, 1, 1, 0, -1, 0,
                     1, -2, 0, 0, -2, -1, 0, -1, 0, -1, -1, -2, 1, -2, 1, 1, 1,
                     1, -1, -1, -2, -2, -1, -2, 1, -1, -2, 1, 1, 1, 2, -1, 2,
                     -1,
                     -1, 1, 1, -2, 1, -1, -1, -1, -2, 2, -2, 2, 1, 1, 1, -1, 1,
                     -2, 1, 2, -1, 2, -1, -1, 2, -2, -1, -1, -2, -2, -2, -2, 1,
                     2,
                     2, 0, 2, 0, 1, 2, 0, 0, 1, -1, 0, 1, 0, 1, 1, 1, -1,
                     -1, -1, -2, 1, 1, -2, 1, 1, -2, 2, -2, 2, -1, -2, 2, 1, 1,
                     2, 1, 2, -1, -1, 1, 1, -1, -1, -2, -1, -1, 1, 2, 1, 1, 2,
                     1, 1, 2, 2, -1, 1, 2, -1, 2, 1, 2, 2, -2, 2, -1, -2, 2,
                     -2, 2, 1, -1, -2, 0, -2, 0, -1, -1, 0, 0, -1, -1, 0, 1, 0,
                     -1, -2, -1, -1, -2, -1, -2, -1, -2, -1, 2, 1, -2, 2, -2,
                     -1, 2,
                     -1, 2, 1, 1, 2, -1, 2, 2, 1, 1, 1, -1, 1, 1, 2, 1, 1,
                     -1, -2, -1, -1, 1, -1, -1, -1, -2, -2, 2, -1, 2, -2, -2,
                     -1, -2,
                     -2, 1, -2, -1, -2, -2, -2, -1, 1, 0, 1, 0, -2, -2, 0, 0,
                     1,
                     1, 0, -2, 0, 0, 0, 2, 2, 1, 2, 2, 0, 0, 0, 1, -2, -2,
                     -2, -2, 0, 0, 0, 1, -2, -2, 2, -1, 0, 0, 0, -1, -1, 1, 1,
                     -1, 0, 0, 0, -1, 1, 2, 1, 1, 0, 0, 0, 1, 2, 2, -1, 1,
                     0, 0, 0, 1, 2, 2, -1, 1, 0, 0, 0, 2, 2, 0, -1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_wildy_blurry_sig():
    return np.array([0, 0, 0, 0, 2, 0, -1, -1, 0, 0, 0, -2, -1, -2, -2, -1, 0,
                     0, 0, 1, -2, -2, -1, -1, 0, 0, 0, 2, -2, 2, 2, -2, 0, 0,
                     0, 2, 2, 2, 1, 2, 0, 0, 0, -2, 2, -2, -1, 2, 0, 0, 0,
                     -2, 2, -2, 2, -1, 0, 0, 0, -2, -1, 1, -2, -1, 0, 0, 0, 1,
                     0, -2, -1, 0, 0, 1, 2, 0, -1, 0, -2, 2, 1, 2, 2, 1, 2,
                     -1, 2, 2, 1, 1, -2, -2, -1, 1, -1, -1, 1, -2, -2, 1, -2,
                     -1,
                     -1, -2, 2, -1, 2, 2, 2, 2, 2, -1, -2, 1, 2, -2, 2, 2, -2,
                     2, -2, -2, -1, -2, -2, -2, -2, -1, 1, 2, 2, 2, 1, 1, 2, 2,
                     1, 1, 0, -1, 0, 1, 1, 0, 0, 2, 1, 0, 2, 0, -1, 2, -2,
                     -2, -1, -2, -2, -2, -2, 1, -2, 1, 1, 2, 1, -1, 2, -2, 1,
                     1,
                     -2, -1, -1, 2, -2, -2, 2, -2, -2, 1, -2, -2, -2, -2, 1, 2,
                     2,
                     2, 2, 2, 2, 2, -2, 2, -1, -2, 1, -2, -2, 1, 1, -2, -1, -1,
                     1, -2, 1, 1, -2, -1, 0, -1, 0, -1, 1, 0, 0, 1, 2, 0, 2,
                     0, 2, 2, -2, 2, 1, -2, 2, -1, 1, -1, -1, -2, -2, -2, -2,
                     -2,
                     -2, -2, 2, 2, 2, 2, -1, 1, 1, 1, 2, 2, -2, 1, 1, 1, 1,
                     -2, 2, -2, 2, -1, 1, 1, -2, 1, -2, 2, 2, -1, 2, -2, -1, 2,
                     -1, -1, 1, -2, 1, -2, -1, -1, -1, -1, 0, -1, 0, -1, -1, 0,
                     0,
                     -2, 1, 0, 2, 0, 2, 2, -2, -1, 2, -2, -2, 1, -1, 1, 1, 2,
                     -1, 2, -1, 2, 2, -1, 2, -1, -1, 1, 1, 2, -1, -1, -1, -1,
                     -1,
                     -1, -2, -1, -1, -2, 2, 2, 2, 2, 2, 2, 2, 2, -1, 1, 2, -2,
                     2, -2, -1, 2, -2, 1, 1, -2, 1, -2, 1, -2, 1, 1, 0, -1, 0,
                     1, -2, 0, 0, -2, -1, 0, -1, 0, -1, -1, -2, 1, -2, 1, 1, 1,
                     1, -1, -1, -2, -2, -1, -2, 1, -1, -2, 1, 1, 1, 2, -1, 2,
                     -1,
                     -1, 1, 1, -2, 1, -1, -1, -1, -2, 2, -2, 2, 1, 1, 1, -1, 1,
                     -2, 1, 2, -1, 2, -1, -1, 2, -2, -1, -1, -2, -2, -2, -2, 1,
                     2,
                     2, 0, 2, 0, 1, 2, 0, 0, 1, -1, 0, 1, 0, 1, 1, 1, -1,
                     -1, -1, -2, 1, 1, -2, 1, 1, -2, 2, -2, 2, -1, -2, 2, 1, 1,
                     2, 1, 2, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 2, 1, 1, 1,
                     1, 1, 2, 2, -1, 1, 2, -1, 2, 1, 2, 2, -2, 2, -1, -2, 2,
                     -2, 2, 1, -1, -2, 0, -2, 0, -1, -1, 0, 0, -1, -1, 0, -1,
                     0,
                     -1, -2, -1, -1, -2, 1, -2, -1, -2, -1, 2, 1, -2, 2, -2,
                     -1, 2,
                     -1, 2, 1, 1, 2, -1, 2, 2, 1, 1, 1, -1, 1, 1, 2, 1, 1,
                     -1, -2, -1, -1, 1, -1, -1, -1, -2, -2, 2, -1, 2, -2, -2,
                     -1, -2,
                     -2, 1, -2, -1, -2, -2, -2, -1, 1, 0, 1, 0, -2, -2, 0, 0,
                     1,
                     1, 0, -2, 0, 0, 0, 2, 2, 1, 2, 2, 0, 0, 0, 1, -2, -2,
                     -2, -2, 0, 0, 0, 1, -2, -2, 2, -1, 0, 0, 0, -1, -1, 1, 1,
                     -1, 0, 0, 0, -1, 1, 2, 1, 1, 0, 0, 0, 1, 2, 2, -1, 1,
                     0, 0, 0, 1, 2, 2, -1, 1, 0, 0, 0, 2, 2, 0, -1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_wildy_crop_sig():
    return np.array([0, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0, -2, -1, -2, -2, -2, 0,
                     0, 0, 1, -2, -2, -2, -2, 0, 0, 0, 2, -2, -1, -1, -1, 0, 0,
                     0, 2, -1, 2, 2, 2, 0, 0, 0, 1, 2, 2, 2, 2, 0, 0, 0,
                     -2, -2, -2, -2, 1, 0, 0, 0, 2, 2, -1, 2, 2, 0, 0, 0, -2,
                     0, -1, -1, 0, 0, -1, 2, 0, 1, 0, -2, 2, -2, 2, 2, -1, -1,
                     -2, 2, 2, 2, 2, 1, 1, -1, 2, 2, -2, 2, 1, -2, 1, 1, 2,
                     -2, 1, 1, -2, -2, -1, -2, -2, 1, -1, -2, -2, 2, 2, -1, 2,
                     2,
                     -2, -2, 2, 1, 1, 2, 2, -2, 2, -1, -2, 1, -2, 1, -2, 1, 1,
                     -2, 1, 0, -1, 0, -1, 1, 0, 0, 2, 2, 0, 2, 0, 2, 2, -2,
                     -2, -2, -2, 1, -1, -2, 1, -2, -2, -2, -1, -2, -2, 1, -2,
                     2, 2,
                     2, 2, 2, 2, 2, 1, -1, -1, -2, -2, -2, -1, -2, -2, 1, -2,
                     -2,
                     2, -2, -1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 2, -2, -1, 1, -2,
                     1, -1, -2, -1, -1, -1, 0, -1, 0, -2, -1, 0, 0, -2, 1, 0,
                     -2,
                     0, -2, -2, -2, 2, 2, 2, 2, -1, -1, -1, -1, -1, -2, -2, -2,
                     -2,
                     -2, -2, 2, -2, 1, 2, -2, -1, -1, -1, -1, 2, 1, 2, 1, 2, 1,
                     1, 2, 1, -2, -1, 2, -1, -1, -2, -2, -2, 1, -2, -2, -2, -2,
                     -2,
                     -2, 2, 2, 2, 2, -1, 1, 1, 1, 1, 0, -2, 0, -2, -2, 0, 0,
                     2, 1, 0, -1, 0, 2, 2, 2, 1, 2, 1, -1, 2, 2, 2, 1, 2,
                     1, 1, 1, 2, 2, 1, 2, 1, -2, -1, -1, 1, -1, -1, 1, -1, 1,
                     1, -1, 1, 1, 1, -1, 1, 2, 1, -2, 1, 1, -1, 2, 2, 1, 2,
                     2, 2, 1, 1, 2, -1, 2, -2, 1, -1, -1, 1, -1, 2, 0, -1, 0,
                     -2, 1, 0, 0, -2, -2, 0, 2, 0, -1, -1, -2, -2, -2, -2, -2,
                     -2,
                     -2, -2, -2, -2, -1, 2, -2, 1, -1, -2, -1, 1, -1, 2, -1, 2,
                     -1,
                     -1, 1, -1, -1, 1, -1, -1, -1, -2, -1, -1, -2, 1, -2, -1,
                     -1, 1,
                     1, -1, 1, 2, -1, 1, 2, -1, -1, 1, 2, 1, 2, 2, 1, 2, -1,
                     -1, 0, -2, 0, -2, -1, 0, 0, 1, 2, 0, 1, 0, -1, -1, 1, 2,
                     -1, -1, -1, -1, -1, -1, 2, 1, -2, 1, -2, -1, -1, -2, 2, 1,
                     1,
                     2, 1, 2, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 2, 1, -1, 1,
                     2, 1, -1, -1, -1, -2, -2, -2, -2, -2, -2, 1, 1, -1, 2, 2,
                     1,
                     -1, 2, 2, -2, 1, 0, -1, 0, 2, 2, 0, 0, 1, 1, 0, 1, 0,
                     1, -1, 1, 1, 1, -1, -1, 1, -2, 1, 1, 1, -2, 1, -2, -1, 1,
                     -2, 2, 1, 1, 2, 1, 2, 1, 2, -1, 1, -1, -1, -1, -1, 1, -1,
                     1, 1, 2, 1, -1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, -1, -1,
                     -2, -2, -2, -1, -2, -2, -2, -2, -2, 0, 1, 0, -2, -2, 0, 0,
                     -1,
                     -1, 0, -2, 0, 0, 0, 1, 2, 1, 2, 2, 0, 0, 0, -1, -1, -2,
                     -2, -2, 0, 0, 0, 2, -1, 1, 2, 1, 0, 0, 0, -2, -1, -2, -1,
                     -1, 0, 0, 0, 1, -1, -1, 1, -1, 0, 0, 0, -1, -1, 2, 1, -1,
                     0, 0, 0, 1, 2, 2, 1, 2, 0, 0, 0, 2, 2, 0, -2, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_wildy_inverted_sig():
    return np.array([0, 0, 0, 0, -2, 0, 1, 1, 0, 0, 0, 2, 1, 2, 2, 1, 0,
                     0, 0, -1, 2, 2, 1, 1, 0, 0, 0, -2, 2, -2, -2, 2, 0, 0,
                     0, -2, -2, -2, -1, -2, 0, 0, 0, 2, -2, 2, 1, -2, 0, 0, 0,
                     2, -2, 2, -2, 1, 0, 0, 0, 2, 1, -1, 2, 1, 0, 0, 0, -1,
                     0, 2, 1, 0, 0, -1, -2, 0, 1, 0, 1, -2, -1, -2, -2, -1, -2,
                     1, -2, -2, -1, -1, 2, 2, 1, -1, 1, 1, -1, 2, 2, -1, 2, 1,
                     1, 2, -2, 1, -2, -2, -2, -2, -2, 1, 2, -1, -2, 2, -2, -2,
                     2,
                     -2, 2, 2, 1, 2, 2, 2, 2, 1, -1, -2, -2, -2, -1, -1, -2,
                     -2,
                     -1, -1, 0, 1, 0, -1, -1, 0, 0, -1, -1, 0, -2, 0, 1, -2, 2,
                     2, 1, 2, 2, 2, 2, -1, 2, -1, -1, -2, -1, 1, -2, 2, -1, -1,
                     2, 1, 1, -2, 2, 2, -2, 2, 2, -1, 2, 2, 2, 2, -1, -2, -2,
                     -2, -2, -2, -2, -2, 2, -2, 1, 2, -1, 2, 2, -1, -1, 2, 1,
                     1,
                     -1, 2, -1, -1, 2, 1, 0, 1, 0, 1, -1, 0, 0, -1, -2, 0, -2,
                     0, -2, -2, 2, -2, -1, 2, -2, 1, -1, 1, 1, 2, 2, 2, 2, 2,
                     2, 2, -2, -2, -2, -2, 1, -1, -1, -1, -2, -2, 2, -1, -1,
                     -1, -1,
                     2, -2, 2, -2, 1, -1, -1, 2, -1, 2, -2, -2, 1, -2, 2, 1,
                     -2,
                     1, 1, -1, 2, -1, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0,
                     2, -1, 0, -2, 0, -2, -2, 2, 1, -2, 2, 2, -1, 1, -1, -1,
                     -2,
                     1, -2, 1, -2, -2, 1, -2, 1, 1, -1, -1, -2, 1, 1, 1, 1, 1,
                     1, 2, 1, 1, 2, -2, -2, -2, -2, -2, -2, -2, -2, 1, -1, -2,
                     2,
                     -2, 2, 1, -2, 2, -1, -1, 2, -1, 2, -1, 2, -1, -1, 0, 1, 0,
                     -1, 2, 0, 0, 2, 1, 0, 1, 0, 1, 1, 2, -1, 2, -1, -1, -1,
                     -1, 1, 1, 2, 2, 1, 2, -1, 1, 2, -1, -1, -1, -2, 1, -2, 1,
                     1, -1, -1, 2, -1, 1, 1, 1, 2, -2, 2, -2, -1, -1, -1, 1,
                     -1,
                     2, -1, -2, 1, -2, 1, 1, -2, 2, 1, 1, 2, 2, 2, 2, -1, -2,
                     -2, 0, -2, 0, -1, -2, 0, 0, -1, 1, 0, -1, 0, -1, -1, -1,
                     1,
                     1, 1, 2, -1, -1, 2, -1, -1, 2, -2, 2, -2, 1, 2, -2, -1,
                     -1,
                     -2, -1, -2, 1, 1, -1, -1, 1, 1, 2, 1, 1, -1, -2, -1, -1,
                     -2,
                     -1, -1, -2, -2, 1, -1, -2, 1, -2, -1, -2, -2, 2, -2, 1, 2,
                     -2,
                     2, -2, -1, 1, 2, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, -1, 0,
                     1, 2, 1, 1, 2, 1, 2, 1, 2, 1, -2, -1, 2, -2, 2, 1, -2,
                     1, -2, -1, -1, -2, 1, -2, -2, -1, -1, -1, 1, -1, -1, -2,
                     -1, -1,
                     1, 2, 1, 1, -1, 1, 1, 1, 2, 2, -2, 1, -2, 2, 2, 1, 2,
                     2, -1, 2, 1, 2, 2, 2, 1, -1, 0, -1, 0, 2, 2, 0, 0, -1,
                     -1, 0, 2, 0, 0, 0, -2, -2, -1, -2, -2, 0, 0, 0, -1, 2, 2,
                     2, 2, 0, 0, 0, -1, 2, 2, -2, 1, 0, 0, 0, 1, 1, -1, -1,
                     1, 0, 0, 0, 1, -1, -2, -1, -1, 0, 0, 0, -1, -2, -2, 1, -1,
                     0, 0, 0, -1, -2, -2, 1, -1, 0, 0, 0, -2, -2, 0, 1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_wildy_rotate_1_sig():
    return np.array([0, 0, 0, 0, 1, 0, -2, -1, 0, 0, 0, -1, -1, -2, -2, -2, 0,
                     0, 0, 1, -2, -1, -1, -1, 0, 0, 0, 2, -2, 2, 2, -1, 0, 0,
                     0, 2, 2, 2, 2, 1, 0, 0, 0, -2, 2, -2, -2, 1, 0, 0, 0,
                     -2, 1, -2, -1, 1, 0, 0, 0, -1, -2, -2, -1, -1, 0, 0, 0, 2,
                     0, 1, 1, 0, 0, 2, 2, 0, 2, 0, -1, 2, 1, 2, 1, -2, -1,
                     -2, -1, -2, 2, 1, -2, 1, 1, -1, -2, -1, 1, -2, -2, -1, -2,
                     -2,
                     -1, -2, 1, -2, 2, 2, -1, 2, 2, -1, -1, 2, 2, 1, 2, 2, 1,
                     1, -1, 1, 2, -2, 1, -2, -2, 1, -1, 1, -1, -1, -1, -2, -1,
                     -1,
                     1, -1, 0, 1, 0, 1, 1, 0, 0, 1, 2, 0, 2, 0, 2, 1, -2,
                     1, 1, -2, -2, -1, -2, 2, 2, 2, 2, 2, 2, -1, 2, -1, 1, 1,
                     -2, -2, -1, 2, -2, -2, 2, -2, -2, 1, -2, -1, -2, -1, 1,
                     -1, 2,
                     2, 1, 2, 2, 1, -1, 2, 2, -1, 2, 2, 1, 2, -1, 1, -1, -2,
                     1, -2, -1, 1, 1, -1, 0, -1, 0, -1, 1, 0, 0, -2, 1, 0, -2,
                     0, 1, -1, -1, 2, 1, 2, 2, 2, 1, -1, -2, -2, -2, -2, -2,
                     -2,
                     -2, -2, 1, 2, 1, 2, -1, -1, 1, 1, 2, 2, -2, 1, 1, 1, 1,
                     -1, 1, -2, -2, -1, -2, -1, -2, -2, -1, -1, 2, 2, 2, 1, -2,
                     2,
                     -2, 1, 1, -2, 1, -2, -1, 1, -1, -1, 0, -1, 0, -2, -1, 0,
                     0,
                     -1, -2, 0, -1, 0, 1, 2, 1, -1, 2, 1, -2, 2, 2, 1, 1, 2,
                     1, 2, 1, 2, 2, 1, 2, -1, -1, -1, 1, 2, -1, -1, -1, -1, 1,
                     -1, -1, -1, -1, -2, 1, 2, -1, 1, -2, -1, -1, 1, 2, 2, 2,
                     2,
                     2, 1, 2, 2, -2, 1, 2, -2, 1, -2, -2, 1, -1, 1, 0, -1, 0,
                     -2, -1, 0, 0, -1, -2, 0, 1, 0, -2, -2, -2, -2, -2, -1, -2,
                     -2,
                     -2, -1, -1, -2, -2, 2, -2, -2, 1, -2, -1, 1, 1, 2, -1, 2,
                     -1,
                     -1, 1, 1, 1, 1, -1, -1, 1, -2, 2, 1, -1, 1, 1, 1, -2, -1,
                     -1, -2, 2, -1, -1, -2, -2, 1, -2, 2, 2, 1, 2, -2, 2, 2,
                     -1,
                     1, 0, -2, 0, -1, 1, 0, 0, 2, 2, 0, -1, 0, -1, -1, 2, 2,
                     2, 1, 2, 1, 1, 2, 1, -1, -2, -2, -2, -2, -1, -2, 2, 1, 1,
                     2, 1, 2, -1, -1, 1, -1, -1, -1, -2, -1, -1, -2, 2, 2, 2,
                     2,
                     1, 2, -1, 2, 1, 2, 2, -1, 2, -1, 2, 2, -1, -2, 1, -2, 2,
                     -1, -2, 1, -2, -1, 0, -2, 0, -2, -1, 0, 0, 1, -1, 0, -1,
                     0,
                     2, 2, 1, -1, 2, 1, 1, 2, 2, 2, -2, 1, -2, -1, -2, 1, 1,
                     -2, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, -2, -1, -2, 1, 1, -1,
                     2, 1, 1, 2, 2, 2, 1, 2, -2, -2, 1, -2, -1, -2, -1, -2, -2,
                     2, 2, 1, 2, -1, -2, -2, -1, 1, 0, -2, 0, -2, -2, 0, 0, -2,
                     -2, 0, 1, 0, 0, 0, -2, -2, -1, -1, -1, 0, 0, 0, -2, -1,
                     -2,
                     1, -2, 0, 0, 0, 2, -1, -1, 2, 1, 0, 0, 0, -1, -1, -2, -1,
                     -2, 0, 0, 0, 1, -1, 2, 2, 2, 0, 0, 0, -2, 1, 1, -2, -2,
                     0, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 2, 0, -1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_wildy_rotate_2_sig():
    return np.array([0, 0, 0, 0, -1, 0, -1, -2, 0, 0, 0, 1, -2, -1, -2, -2, 0,
                     0, 0, 2, 1, 2, 2, 2, 0, 0, 0, -1, 2, 2, 2, 1, 0, 0,
                     0, -2, 1, -2, -2, -2, 0, 0, 0, -1, 1, -2, -2, 1, 0, 0, 0,
                     -1, 2, -2, -1, 2, 0, 0, 0, -2, 1, -2, 1, 1, 0, 0, 0, -1,
                     0, 1, 1, 0, 0, 1, 1, 0, -1, 0, -1, -2, 2, 2, -2, 1, -2,
                     -1, -2, -1, 2, -2, -2, 2, -1, -1, 2, 2, -2, -2, 2, 1, -1,
                     2,
                     2, 2, -1, 2, 2, 1, 1, 2, 2, -1, 2, 2, 2, -1, 2, 2, -1,
                     1, -1, 1, 2, -2, 2, -2, -2, -1, -2, -1, -1, -2, -1, -2,
                     -2, -1,
                     -1, -1, 0, 1, 0, -2, -1, 0, 0, 1, 1, 0, -2, 0, -1, -2, 2,
                     2, 1, 2, 2, 2, 1, 2, 1, -2, -2, -2, -1, -2, -2, -2, -2,
                     -2,
                     -2, 1, 1, -1, -2, -2, -2, -2, -2, -1, -2, -2, -2, -2, 1,
                     1, 2,
                     2, 1, 2, 1, 1, -1, 2, 2, -1, 2, -1, -1, -1, 1, 2, 2, -2,
                     2, -2, -2, 1, 1, 1, 0, -2, 0, -2, -2, 0, 0, 1, -2, 0, -2,
                     0, 2, -1, 2, -1, 2, 2, 1, 2, 2, 1, -2, 2, 1, -1, -1, 2,
                     -1, 1, 2, 2, 2, 1, -1, -1, 1, 2, 2, 2, -2, 1, -2, 1, 2,
                     2, 2, -1, 1, 2, 1, 2, 2, -2, -1, 1, 2, -1, -1, 2, -2, 1,
                     1, 2, 2, 1, 2, -2, 1, 1, -1, 2, 0, -2, 0, -2, -2, 0, 0,
                     -2, -2, 0, -2, 0, -1, -1, 1, -2, -2, 2, -2, 1, 1, -1, -1,
                     1,
                     1, 2, 1, 2, 2, 1, -1, -1, -1, -1, 1, 1, 1, -1, -2, -2, -2,
                     -1, 2, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 2, 2,
                     2, 2,
                     2, 2, 2, 1, -1, -1, 2, -2, 1, 2, -1, 2, -1, 2, 0, -1, 0,
                     -2, 2, 0, 0, 1, -1, 0, -1, 0, 1, -1, 1, -1, -2, 1, -1, 1,
                     -1, -2, 1, -2, -1, 1, -1, 1, -2, -2, -1, -1, 1, 1, -1, -1,
                     -1,
                     -1, 1, 2, 2, 1, -2, -1, 1, -1, 2, 2, -2, 2, 2, 2, 1, 1,
                     2, -2, -2, -2, -2, -2, -2, -1, -1, 1, 2, 2, 2, 1, 2, 2,
                     -2,
                     -2, 0, -2, 0, -1, -2, 0, 0, -1, -1, 0, -2, 0, -1, -1, 1,
                     1,
                     -1, 2, -2, 1, 1, -2, 2, 2, 1, 2, -1, 2, -1, -1, 2, 1, 1,
                     1, 1, -1, -1, 1, 1, -1, -2, -1, -2, -1, -1, -2, 1, -1, 2,
                     2,
                     -1, 1, 1, -1, -1, 2, -1, 1, 2, 1, -1, -1, 1, -2, 1, -2,
                     -2,
                     -2, -2, 1, -2, 2, 0, 2, 0, -1, 2, 0, 0, 1, -1, 0, -1, 0,
                     -2, 1, 1, -1, -2, 1, -2, -1, 1, -2, 2, 1, 1, 2, -1, 2, 1,
                     1, 1, 1, 1, 1, 1, 2, 1, 2, -1, 1, -1, -1, -1, -1, 1, 1,
                     2, -1, -1, 1, -1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1,
                     2, 1, -1, 2, 2, 2, 2, -1, -2, 0, -2, 0, 1, 1, 0, 0, 2,
                     1, 0, 2, 0, 0, 0, -1, -1, -2, -2, -2, 0, 0, 0, 2, -1, -2,
                     2, -1, 0, 0, 0, -1, -1, 1, 1, 1, 0, 0, 0, -2, -1, -2, -1,
                     -1, 0, 0, 0, -1, -2, -2, 1, 1, 0, 0, 0, -2, -2, -2, -1, 1,
                     0, 0, 0, -2, -2, -1, -1, -1, 0, 0, 0, -2, -1, 0, 1, 0, 0,
                     0, 0], dtype=np.int8)


@pytest.fixture
def ref_dist_blacky_to_blacky():
    return 0.0


@pytest.fixture
def ref_dist_blacky_to_blurry():
    return 0.7326422768871266


@pytest.fixture
def ref_dist_blacky_to_comfy():
    return 0.7440943962886936


@pytest.fixture
def ref_dist_blacky_to_spoony():
    return 0.7336452099738995


@pytest.fixture
def ref_dist_blacky_to_wildy():
    return 0.7128030831121016


@pytest.fixture
def ref_dist_wildy_to_wildy_blurry():
    return 0.04696682183138621


@pytest.fixture
def ref_dist_wildy_to_wildy_crop():
    return 0.04696682183138621


@pytest.fixture
def ref_dist_wildy_to_wildy_inverted():
    return 1.0


@pytest.fixture
def ref_dist_wildy_to_wildy_rotate_1():
    return 0.5355041604715625


@pytest.fixture
def ref_dist_wildy_to_wildy_rotate_2():
    return 0.7112540705972631
