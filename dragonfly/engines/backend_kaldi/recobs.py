﻿#
# This file is part of Dragonfly.
# (c) Copyright 2018 by Dane Finlay
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
Recognition observer class for Kaldi backend
"""

from ..base import RecObsManagerBase


class KaldiRecObsManager(RecObsManagerBase):
    """
    This class's methods are called by the engine directly, rather than through a
    grammar.
    """
    def __init__(self, engine):
        RecObsManagerBase.__init__(self, engine)

    # The following methods must be implemented by RecObsManagers.
    def _activate(self):
        pass

    def _deactivate(self):
        pass