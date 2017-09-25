import pyqtgraph as pg 
from PyQt4 import QtGui 
import numpy as np 
import sys 
def main(): 
    app = QtGui.QApplication(sys.argv) 
    widg = QtGui.QWidget() 
    widg.move(100, 100) 
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k') 

    pgWidg = pg.GraphicsLayoutWidget()   
    pgWidg.resize(750, 250)  

    graph1 = pgWidg.addPlot(row=1, col=1) 
    graph2 = pgWidg.addPlot(row=1, col=2)
    curve1 = graph1.plot(y=np.sin(np.linspace(1, 21, 1000)), pen='k') 
    curve2 = graph2.plot(y=np.sin(np.linspace(1, 21, 1000)), pen='k') 

    graph1.addItem(curve1) 
    graph2.addItem(curve2) 
    graph1.setMouseEnabled(x=False, y=True)
    graph2.setMouseEnabled(x=False, y=True)

    graph1Text = pg.TextItem(text = 'A1', color=(0, 0, 0))
    graph1.addItem(graph1Text)
    # graph1_vb = graph1.getViewBox()
    # graph1Text.setParentItem(graph1_vb)
    graph1Text.setPos(150, 1)

    legend = graph2.addLegend()
    style = pg.PlotDataItem(pen='w')
    legend.addItem(style, 'A2')

    grid = QtGui.QGridLayout() 
    grid.addWidget(pgWidg, 0,0)          
    widg.setLayout(grid) 
    widg.show() 
    sys.exit(app.exec_()) 

if __name__ == '__main__':  
    main()