# -*- coding: utf-8 -*-
"""Minimum working example for a bug in pyqtgraph's parametertree. Calling a ParameterItems hide()/show() raises a TypeError in version 0.10.0."""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.parametertree import Parameter, ParameterTree

app = QtGui.QApplication([])

params = [{'name': 'Dummy', 'type': 'int', 'value': 10}]

p = Parameter.create(name='params', type='group', children=params)
t = ParameterTree()
t.setParameters(p, showTop=False)

p.param('Dummy').setValue(3.14159)
v = p.param('Dummy').value()
print(v, type(v).__name__)

win = QtGui.QMainWindow()
win.setCentralWidget(t)
win.show()

QtGui.QApplication.instance().exec_()        
