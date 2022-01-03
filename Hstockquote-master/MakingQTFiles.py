

#get to the directory your name file is in

#chdir desktop

#changes the ui file to py file for use

#C:/Python27/Lib/site-packages/PyQt4/pyuic4 name.ui -o name.py


#!/usr/bin/python -d
 
import sys
import os

dir_name = os.path.join(os.path.expanduser('~'), 'Desktop')
sys.path.append(dir_name)
from PyQt4 import QtCore, QtGui
from Market_History import Ui_Form

import hstockquote 

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    NasdaqList = hstockquote.Nasdaq_List_Maker('stocklist')
    for x in xrange(len(NasdaqList)-1):
        self.ui.comboBox.addItem(NasdaqList[x])
    NasdaqNameList = hstockquote.Nasdaq_Name_List_Maker('stocklist')
    for x in xrange(len(NasdaqNameList)-1):
        self.ui.comboBox_2.addItem(NasdaqNameList[x])
    MarketNameList = hstockquote.Nasdaq_Name_List_Maker('stocklist')
    MarketName = ['^GSPC|S&P500','^IXIC|Nasdaq Composite','^NDX|Nasdaq 100','DJIA|Dow Jones Industial Average','^DJA|Dow Jones Average Composite']
    MarketNameList.pop()
    for x in xrange(len(MarketName)):
        MarketNameList.append(MarketName[x])
    for x in xrange(len(MarketNameList)):
        self.ui.comboBox_3.addItem(MarketNameList[x])        
    MarketList = hstockquote.Nasdaq_List_Maker('stocklist')
    marketSym = ['^GSPC','^IXIC','^NDX','DJIA','^DJA']
    MarketList.pop()
    for x in xrange(len(marketSym)):
        MarketList.append(marketSym[x])
    for x in xrange(len(MarketList)):
        self.ui.comboBox_4.addItem(MarketList[x])
           
    QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.button_Clicked)
  def button_Clicked(self):
      #self.ui.webView.stop()
      graphtype = 10
      if self.ui.radioButton_3.isChecked():
        graphtype = 0    
      if self.ui.radioButton.isChecked():
        graphtype = 2      
      if self.ui.radioButton_2.isChecked():
        graphtype = 1
      if self.ui.radioButton.isChecked() and self.ui.radioButton_2.isChecked():
        graphtype = 3
      if self.ui.radioButton_2.isChecked() and self.ui.radioButton_3.isChecked():
        graphtype = 4
      if self.ui.radioButton.isChecked() and self.ui.radioButton_3.isChecked():
        graphtype = 5
      if self.ui.radioButton.isChecked() and self.ui.radioButton_2.isChecked() and self.ui.radioButton_3.isChecked():
        graphtype = 6
      self.ui.label_img.setPixmap(QtGui.QPixmap(os.path.join(dir_name + '\Python.png')))
      free = os.path.join(dir_name + '\example_02.png')
      os.remove(free)
      temp_date = self.ui.dateEdit.date() 
      date_b = temp_date.toPyDate()
      date_b = str(date_b)
      date_b = date_b.replace('-', '')
      temp_date_2 = self.ui.dateEdit_2.date() 
      date_e = temp_date_2.toPyDate()
      date_e = str(date_e)
      date_e = date_e.replace('-', '')
      begin = date_b
      end = date_e
      stock_1 = self.ui.comboBox.currentText()
      market_1 = self.ui.comboBox_4.currentText()
      stock_2 = self.ui.comboBox_2.currentText()
      market_2 = self.ui.comboBox_3.currentText()
      if stock_1 == 'Symbol' :
        if stock_2 == 'Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size':
          None
        else:
          stock_2 = stock_2.split('|')
          stock = stock_2[0]
      else:
        stock = stock_1
      if market_1 == 'Symbol':
        if market_2 == 'Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size':
          None
        else:
          market_2 = market_2.split('|')
          market = market_2[0]
      else:
        market = market_1
      stock =str(stock)
      market = str(market)
      hstockquote.graphKeyer(stock, market, begin, end, graphtype)
      Betas = hstockquote.Beta(stock, market, begin, end)
      self.ui.lineEdit.setText(Betas[3])
      self.ui.lineEdit_2.setText(Betas[4])
      self.ui.lineEdit_3.setText(Betas[2])
      self.ui.lineEdit_4.setText(Betas[0])
      self.ui.lineEdit_5.setText(Betas[1])
      self.ui.label_img.setPixmap(QtGui.QPixmap(os.path.join(dir_name + '\example_02.png')))
      #self.ui.webView.setUrl(QtCore.QUrl(os.path.join(dir_name + '\example_02.png')))
      #self.ui.webView.show()
      
if __name__ == "__main__":  
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
