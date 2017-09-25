# -*- coding: utf-8 -*-
"""Minimum working example for a bug in pyqtgraph's parametertree. Calling a ParameterItems hide()/show() raises a TypeError in version 0.10.0."""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.parametertree import Parameter, ParameterTree

app = QtGui.QApplication([])

params = [
    {'name': 'Dummy', 'type': 'int', 'value': 10},
    {'name': 'Show', 'type': 'action'},
    {'name': 'Hide', 'type': 'action'},
]

## Create tree of Parameter objects
p = Parameter.create(name='params', type='group', children=params)
t = ParameterTree()
t.setParameters(p, showTop=False)

p.param('Show').sigActivated.connect(lambda: p.param('Dummy').show())
p.param('Hide').sigActivated.connect(lambda: p.param('Dummy').hide())

win = QtGui.QMainWindow()
win.setCentralWidget(t)
win.show()

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
