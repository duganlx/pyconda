from eampysdk import EamPySdk
from localpysdk import LocalPySdk

if __name__ == '__main__':

  eamsdk = EamPySdk()
  df = eamsdk.getBardayData(universe=['600519.SH'])
  eamsdk.savedf(df, filename='gzmt.csv')

  lcsdk = LocalPySdk()
  df = lcsdk.getData(filename='gzmt.csv')
  print(df)