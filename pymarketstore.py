## marketstore historical datafeed

            import backtrader as bt
            from ..utils import date2num
            import backtrader.feed as feed
            import datetime
            import pytz
            import pymarketstore as pymkts


            class MarketStore(feed.DataBase):

                params = (
                    ('dataname', None),
                    ('fromdate', datetime.date(1990, 1, 1)),
                    ('todate', datetime.date(2050,1,1)),
                    ('name', ''),
                    ('compression', 1),
                    ('timeframe', bt.TimeFrame.Days),
                    ('host', '127.0.0.1'),
                    ('port', '5993'),
                    ('symbol', None),
                    ('query_timeframe', None),

                )

                def start(self):
                    super(MarketStore, self).start()

                    self.ndb = pymkts.Client('http://{host}:{port}/rpc'.format(
                        host=self.p.host,
                        port=self.p.port
                    ))

                    # The query could already consider parameters like fromdate and todate
                    # to have the database skip them and not the internal code

                    qstr = pymkts.Params(self.p.symbol,
                                         self.p.query_timeframe,
                                         'OHLCV',
                                         start=self.p.fromdate.isoformat(),
                                         end=self.p.todate.isoformat())


                    dbars = list(self.ndb.query(qstr).first().array)

                    self.biter = iter(dbars)


                def _load(self):
                    try:
                        bar = next(self.biter)
                    except StopIteration:
                        return False


                    self.l.datetime[0] = date2num(datetime.datetime.fromtimestamp(bar[0],pytz.utc))
                    self.l.open[0] = bar[1]
                    self.l.high[0] = bar[2]
                    self.l.low[0] = bar[3]
                    self.l.close[0] = bar[4]
                    self.l.volume[0] = bar[5]

                    return True
