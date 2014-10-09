#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest

from gyazo import Image, ImageList


class TestImage(unittest.TestCase):
    def setUp(self):
        self.samples = []
        self.samples.append({
            'url': 'https://i.gyazo.com/2c9044330d710fca3da64b222eddf5b5.png',
            'type': 'png',
            'created_at': '2014-07-25T08:29:51+0000',
            'image_id': '2c9044330d710fca3da64b222eddf5b5',
            'thumb_url': 'https://i.gyazo.com/thumb/180/_242799a7d541869e0b73dc93ee113fb5.png',
            'permalink_url': 'http://gyazo.com/2c9044330d710fca3da64b222eddf5b5'})
        self.samples.append({
            'url': 'https://i.gyazo.com/9d04d2da1b4daaaa234c68b5219dc1e3.png',
            'type': 'png',
            'created_at': '2014-07-20T03:09:34+0900',
            'image_id': '9d04d2da1b4daaaa234c68b5219dc1e3',
            'thumb_url': 'https://i.gyazo.com/thumb/180/_eadaaad52408b1e53c09111d6959139f.png',
            'permalink_url': 'http://gyazo.com/9d04d2da1b4daaaa234c68b5219dc1e3'})
        self.samples.append({
            'url': '',
            'type': 'png',
            'created_at': '2014-06-21T13:45:46+0000',
            'image_id': '',
            'thumb_url': 'https://i.gyazo.com/thumb/180/_ebb000813faac4c0572cc0fc0b2d8ede.png',
            'permalink_url': ''})

    def test_from_dict(self):
        for sample in self.samples:
            image = Image.from_dict(sample)
            self.assertIsNotNone(image)

    def test_to_dict(self):
        for sample in self.samples:
            image = Image.from_dict(sample).to_dict()
            for key in sample:
                if sample[key] is not None and sample[key] != '':
                    self.assertEqual(sample[key], image[key])


class TestImageList(unittest.TestCase):
    def test_has_next_page(self):
        il = ImageList()
        il.total_count = 23
        il.per_page = 10
        il.current_page = 0
        self.assertTrue(il.has_next_page())
        il.current_page = 3
        self.assertFalse(il.has_next_page())
        il.total_count = 20
        il.current_page = 0
        self.assertTrue(il.has_next_page())
        il.current_page = 2
        self.assertFalse(il.has_next_page())
        il.current_page = 4
        self.assertFalse(il.has_next_page())

    def test_has_previous_page(self):
        il = ImageList()
        il.current_page = 0
        self.assertFalse(il.has_previous_page())
        il.current_page = 1
        self.assertTrue(il.has_previous_page())