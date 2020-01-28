#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cdoslom
----------------------------------

Tests for `cdoslom` module.
"""

import os
import sys
import unittest
import tempfile
import shutil


from cdoslom import cdoslom


class TestCdoslom(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_args(self):
        myargs = ['inputarg']
        res = cdoslom._parse_arguments('desc', myargs)
        self.assertEqual('inputarg', res.input)
        self.assertEqual(False, res.directed)
        self.assertEqual(False, res.nosinglet)
        self.assertEqual(-1, res.seed)
        self.assertEqual(0.1, res.p_val)
        self.assertEqual(0.5, res.cp)

    def test_run_gprofiler_no_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            myargs = [tfile]
            theargs = cdoslom._parse_arguments('desc', myargs)
            res = cdoslom.run_oslom(tfile, theargs)
            self.assertEqual(3, res)
        finally:
            shutil.rmtree(temp_dir)

    def test_run_oslom_empty_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            open(tfile, 'a').close()
            myargs = [tfile]
            theargs = cdoslom._parse_arguments('desc', myargs)
            res = cdoslom.run_oslom(tfile, theargs)
            self.assertEqual(4, res)
        finally:
            shutil.rmtree(temp_dir)

    def test_main_invalid_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            myargs = ['prog', tfile]
            res = cdoslom.main(myargs)
            self.assertEqual(3, res)
        finally:
            shutil.rmtree(temp_dir)

    def test_main_empty_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            open(tfile, 'a').close()
            myargs = ['prog', tfile]
            res = cdoslom.main(myargs)
            self.assertEqual(4, res)
        finally:
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    sys.exit(unittest.main())
