# -*- coding: utf-8 -*-

"""Tests for signature generation.
"""
import pytest

from image_match import ImageSignature, normalized_distance


@pytest.fixture
def sig():
    s = ImageSignature()
    return s


# reference signatures ========================================================


def test_blacky(sig, ref_blacky_sig):
    ref = ref_blacky_sig
    res = sig.generate_signature('../diamond_eye/images/blacky.jpg')
    assert pytest.approx(res) == ref


def test_blurry(sig, ref_blurry_sig):
    ref = ref_blurry_sig
    res = sig.generate_signature('../diamond_eye/images/blurry.jpg')
    assert pytest.approx(res) == ref


def test_comfy(sig, ref_comfy_sig):
    ref = ref_comfy_sig
    res = sig.generate_signature('../diamond_eye/images/comfy.jpg')
    assert pytest.approx(res) == ref


def test_spoony(sig, ref_spoony_sig):
    ref = ref_spoony_sig
    res = sig.generate_signature('../diamond_eye/images/spoony.jpg')
    assert pytest.approx(res) == ref


def test_wildy(sig, ref_wildy_sig):
    ref = ref_wildy_sig
    res = sig.generate_signature('../diamond_eye/images/wildy.jpg')
    assert pytest.approx(res) == ref


def test_wildy_blurry(sig, ref_wildy_blurry_sig):
    ref = ref_wildy_blurry_sig
    res = sig.generate_signature('../diamond_eye/images/wildy_blurry.jpg')
    assert pytest.approx(res) == ref


def test_wildy_crop(sig, ref_wildy_crop_sig):
    ref = ref_wildy_crop_sig
    res = sig.generate_signature('../diamond_eye/images/wildy_crop.jpg')
    assert pytest.approx(res) == ref


def test_wildy_inverted(sig, ref_wildy_inverted_sig):
    ref = ref_wildy_inverted_sig
    res = sig.generate_signature('../diamond_eye/images/wildy_inverted.jpg')
    assert pytest.approx(res) == ref


def test_wildy_rotate_1(sig, ref_wildy_rotate_1_sig):
    ref = ref_wildy_rotate_1_sig
    res = sig.generate_signature('../diamond_eye/images/wildy_rotate_1.jpg')
    assert pytest.approx(res) == ref


def test_wildy_rotate_2(sig, ref_wildy_rotate_2_sig):
    ref = ref_wildy_rotate_2_sig
    res = sig.generate_signature('../diamond_eye/images/wildy_rotate_2.jpg')
    assert pytest.approx(res) == ref


# reference distances =========================================================


def test_blacky_to_blacky(ref_blacky_sig, ref_dist_blacky_to_blacky):
    ref = ref_dist_blacky_to_blacky
    res = normalized_distance(ref_blacky_sig, ref_blacky_sig)
    assert pytest.approx(res) == ref


def test_blacky_to_blurry(ref_blacky_sig, ref_blurry_sig,
                          ref_dist_blacky_to_blurry):
    ref = ref_dist_blacky_to_blurry
    res = normalized_distance(ref_blacky_sig, ref_blurry_sig)
    assert pytest.approx(res) == ref


def test_blurry_to_blacky(ref_blacky_sig, ref_blurry_sig,
                          ref_dist_blacky_to_blurry):
    ref = ref_dist_blacky_to_blurry
    res = normalized_distance(ref_blurry_sig, ref_blacky_sig)
    assert pytest.approx(res) == ref


def test_blacky_to_comfy(ref_blacky_sig, ref_comfy_sig,
                         ref_dist_blacky_to_comfy):
    ref = ref_dist_blacky_to_comfy
    res = normalized_distance(ref_blacky_sig, ref_comfy_sig)
    assert pytest.approx(res) == ref


def test_blacky_to_spoony(ref_blacky_sig, ref_spoony_sig,
                          ref_dist_blacky_to_spoony):
    ref = ref_dist_blacky_to_spoony
    res = normalized_distance(ref_blacky_sig, ref_spoony_sig)
    assert pytest.approx(res) == ref


def test_blacky_to_wildy(ref_blacky_sig, ref_wildy_sig,
                         ref_dist_blacky_to_wildy):
    ref = ref_dist_blacky_to_wildy
    res = normalized_distance(ref_blacky_sig, ref_wildy_sig)
    assert pytest.approx(res) == ref


# reference distances for similar images ======================================


def test_wildy_to_wildy_blurry(ref_wildy_sig, ref_wildy_blurry_sig,
                               ref_dist_wildy_to_wildy_blurry):
    ref = ref_dist_wildy_to_wildy_blurry
    res = normalized_distance(ref_wildy_sig, ref_wildy_blurry_sig)
    assert pytest.approx(res) == ref


def test_wildy_to_wildy_crop(ref_wildy_sig, ref_wildy_blurry_sig,
                             ref_dist_wildy_to_wildy_crop):
    ref = ref_dist_wildy_to_wildy_crop
    res = normalized_distance(ref_wildy_sig, ref_wildy_blurry_sig)
    assert pytest.approx(res) == ref


def test_wildy_to_wildy_inverted(ref_wildy_sig, ref_wildy_inverted_sig,
                                 ref_dist_wildy_to_wildy_inverted):
    ref = ref_dist_wildy_to_wildy_inverted
    res = normalized_distance(ref_wildy_sig, ref_wildy_inverted_sig)
    assert pytest.approx(res) == ref


def test_wildy_to_wildy_rotate_1(ref_wildy_sig, ref_wildy_rotate_1_sig,
                                 ref_dist_wildy_to_wildy_rotate_1):
    ref = ref_dist_wildy_to_wildy_rotate_1
    res = normalized_distance(ref_wildy_sig, ref_wildy_rotate_1_sig)
    assert pytest.approx(res) == ref


def test_wildy_to_wildy_rotate_2(ref_wildy_sig, ref_wildy_rotate_2_sig,
                                 ref_dist_wildy_to_wildy_rotate_2):
    ref = ref_dist_wildy_to_wildy_rotate_2
    res = normalized_distance(ref_wildy_sig, ref_wildy_rotate_2_sig)
    assert pytest.approx(res) == ref
