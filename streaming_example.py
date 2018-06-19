import pymarketstore as pymkts

conn = pymkts.StreamConn('ws://localhost:5993/ws')

@conn.on(r'^BTC/')



def on_btc(conn, msg):
    print(msg['data'])
    # print(msg['data']['Epoch'])

conn.run(['BTC/1Min/OHLCV'])  # runs until exception
