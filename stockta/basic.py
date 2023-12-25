import os
import sys

# 解决 ModuleNotFoundError: No module named 'xxx' 问题
this_file_full_path_name = os.path.abspath(__file__)
this_file_folder_path = os.path.dirname(this_file_full_path_name)
parent_folder_path = os.path.dirname(this_file_folder_path)
sys.path.append(parent_folder_path)


from inout.eampysdk import EamPySdk
from inout.localpysdk import LocalPySdk
from ta import StockTA

if __name__ == '__main__':
  choose = False
  if choose:
    eamsdk = EamPySdk()
    df = eamsdk.getBardayData(universe=['600519.SH'])
  else:
    lcsdk = LocalPySdk()
    df = lcsdk.getData(filename='gzmt.csv')

  stockTa = StockTA(df)

  # ma = stockTa.ma(5)
  # ema = stockTa.expma(5)
  # macd = stockTa.macd()
  # kdj = stockTa.kdj()
  # boll = stockTa.boll()
  # mtm = stockTa.mtm()
  # rsi = stockTa.rsi()
  # dmi = stockTa.dmi()
  # dma = stockTa.dma()
  # brar = stockTa.brar()
  # obv = stockTa.obv(offset=32.352-815.769, verbose=True)
  wr = stockTa.wr(n=10)

  print(wr)