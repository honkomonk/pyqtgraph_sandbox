# -*- coding: utf-8 -*-
"""
Minimum working example for a bug in pyqtgraph's parametertree. 
Setting a ParameterItem of type int with a float value changes the variable internally to a float?
"""

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
