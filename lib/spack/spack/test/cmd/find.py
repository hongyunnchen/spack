##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################


import spack.cmd.find
import unittest

from spack.util.pattern import Bunch


class FindTest(unittest.TestCase):

    def test_query_arguments(self):
        query_arguments = spack.cmd.find.query_arguments
        # Default arguments
        args = Bunch(only_missing=False, missing=False,
                     unknown=False, explicit=False, implicit=False)
        q_args = query_arguments(args)
        self.assertTrue('installed' in q_args)
        self.assertTrue('known' in q_args)
        self.assertTrue('explicit' in q_args)
        self.assertEqual(q_args['installed'], True)
        self.assertEqual(q_args['known'], any)
        self.assertEqual(q_args['explicit'], any)
        # Check that explicit works correctly
        args.explicit = True
        q_args = query_arguments(args)
        self.assertEqual(q_args['explicit'], True)
        args.explicit = False
        args.implicit = True
        q_args = query_arguments(args)
        self.assertEqual(q_args['explicit'], False)
        args.explicit = True
        self.assertRaises(SystemExit, query_arguments, args)