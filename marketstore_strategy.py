
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pytz
import datetime
import backtrader as bt

class Master(bt.Strategy):

    def __init__(self):
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        self.dataclose = self.datas[0].close
        self.datavolume = self.datas[0].volume


    def next(self):
        # self.log('Line')

        print(self.datas[0].datetime.date(0), self.datas[0].datetime.time(0),
              self.dataopen[0],
              self.datahigh[0],
              self.datalow[0],
              self.dataclose[0],
              round(self.datavolume[0],2),
              self.datas[0]._name
              )

def runstrat():
    cerebro = bt.Cerebro()

    cerebro.broker.setcash(550000.0)

    data123 = bt.feeds.MarketStore(
        symbol='BTC',
        name='BTC',
        query_timeframe='1Min',
        timeframe=bt.TimeFrame.Minutes,
        fromdate=datetime.date(2018,6,7),
        # todate=datetime.date(2018, 6,6),
        # sessionstart=datetime.time(7),
        # sessionend=datetime.time(10),
        tz=pytz.timezone('US/Eastern'),

    )

    cerebro.adddata(data123)


    cerebro.addstrategy(Master)

    cerebro.run()

    print('finished')

if __name__ == '__main__':
    runstrat()
