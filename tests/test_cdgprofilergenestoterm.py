#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cdgprofilergenestoterm
----------------------------------

Tests for `cdgprofilergenestoterm` module.
"""

import os
import sys
import unittest
import tempfile
import shutil
from unittest.mock import MagicMock
import pandas as pd

from cdgprofilergenestoterm import cdgprofilergenestoterm


class TestCdgprofilergenestoterm(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_inputfile(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            with open(tfile, 'w') as f:
                f.write('hellothere')
            res = cdgprofilergenestoterm.read_inputfile(tfile)
            self.assertEqual('hellothere', res)
        finally:
            shutil.rmtree(temp_dir)

    def test_parse_args(self):
        myargs = ['inputarg']
        res = cdgprofilergenestoterm._parse_arguments('desc',
                                                      myargs)
        self.assertEqual('inputarg', res.input)
        self.assertEqual(0.00001, res.maxpval)
        self.assertEqual('hsapiens', res.organism)

    def test_run_gprofiler_no_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            myargs = [tfile]
            theargs = cdgprofilergenestoterm._parse_arguments('desc',
                                                              myargs)
            try:
                cdgprofilergenestoterm.run_gprofiler(tfile,
                                                     theargs)
                self.fail('Expected FileNotFoundError')
            except FileNotFoundError:
                pass
        finally:
            shutil.rmtree(temp_dir)

    def test_run_gprofiler_empty_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            open(tfile, 'a').close()
            myargs = [tfile]
            theargs = cdgprofilergenestoterm._parse_arguments('desc',
                                                              myargs)
            res = cdgprofilergenestoterm.run_gprofiler(tfile,
                                                       theargs)
            self.assertEqual(None, res)
        finally:
            shutil.rmtree(temp_dir)

    def test_run_gprofiler_with_empty_result(self):
        temp_dir = tempfile.mkdtemp()
        try:
            mygprofiler = MagicMock()
            mygprofiler.profile = MagicMock(return_value=pd.DataFrame())
            tfile = os.path.join(temp_dir, 'foo')
            with open(tfile, 'w') as f:
                f.write('a,b,c')
            myargs = [tfile]
            theargs = cdgprofilergenestoterm._parse_arguments('desc',
                                                              myargs)
            res = cdgprofilergenestoterm.run_gprofiler(tfile,
                                                       theargs,
                                                       gprofwrapper
                                                       =mygprofiler)
            self.assertEqual(None, res)
            mygprofiler.profile.assert_called_once_with(query=['a', 'b', 'c'],
                                                        domain_scope='known',
                                                        organism='hsapiens',
                                                        user_threshold=0.00001,
                                                        no_evidences=False)
        finally:
            shutil.rmtree(temp_dir)

    def test_run_gprofiler_with_valid_result(self):
        temp_dir = tempfile.mkdtemp()
        try:
            mygprofiler = MagicMock()

            df = pd.DataFrame(columns=['name',
                                       'source',
                                       'p_value',
                                       'description',
                                       'intersections',
                                       'precision',
                                       'recall'],
                              data=[['name1',
                                     'source1',
                                     0.1,
                                     'desc1',
                                     ['hi'],
                                     0.5,
                                     0.7],
                                    ['name2',
                                     'source2',
                                     0.5,
                                     'desc2',
                                     ['bye'],
                                     0.6,
                                     0.8]])
            mygprofiler.profile = MagicMock(return_value=df)
            tfile = os.path.join(temp_dir, 'foo')
            with open(tfile, 'w') as f:
                f.write('a,b,c,')
            myargs = [tfile]
            theargs = cdgprofilergenestoterm._parse_arguments('desc',
                                                              myargs)
            res = cdgprofilergenestoterm.run_gprofiler(tfile,
                                                       theargs,
                                                       gprofwrapper
                                                       =mygprofiler)
            self.assertEqual('name2', res['name'])
            mygprofiler.profile.assert_called_once_with(query=['a', 'b', 'c'],
                                                        domain_scope='known',
                                                        organism='hsapiens',
                                                        user_threshold=0.00001,
                                                        no_evidences=False)
        finally:
            shutil.rmtree(temp_dir)

    def test_main_invalid_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            myargs = ['prog', tfile]
            res = cdgprofilergenestoterm.main(myargs)
            self.assertEqual(2, res)
        finally:
            shutil.rmtree(temp_dir)

    def test_main_empty_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tfile = os.path.join(temp_dir, 'foo')
            open(tfile, 'a').close()
            myargs = ['prog', tfile]
            res = cdgprofilergenestoterm.main(myargs)
            self.assertEqual(0, res)
        finally:
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    sys.exit(unittest.main())
