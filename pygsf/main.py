# 安装pygsf, 请使用以下命令
# pip install -U pygsf -i https://jfrog.jhlfund.com/artifactory/api/pypi/py/simple
import json
from pygsf import PyGsfClient, PyGsfRpc

if True:
  rpc = PyGsfRpc()
  
  wwds = rpc.GetClient("WWDS")
  bards = rpc.GetClient("BarDs")
  klineds = rpc.GetClient("KLineDs")
  
  # mids = wwds.GetData(
  #     dataName="mid",
  #     start=0,
  #     length=250,
  #     last_good=False,
  #     universe=["000001.SH", "000001.SZ"],
  # )
  # print(mids)

  # closes = bards.GetData(
  #   dataName="CLOSE",
  #   start=0,
  #   length=250,
  #   last_good=False,
  #   universe=["000001.SH", "000001.SZ"],
  #   # date=20231103,
  # )
  # print(closes)

  klines = klineds.GetData(
      dataName="*",
      start=0,
      length=250,
      last_good=False,
      universe=["000001.SH", "000001.SZ"],
      # date=20231103,
  )
  print(klines)

if False: 
  # 说明
  # date: 日期，格式为YYYYMMDD，获取指定日期的数据，如果不指定，则返回当日的数据
  # last_good: 是否返回已完成的bar, 默认为True
  # start: 开始的索引，从0开始
  # length: 返回的长度，如果不指定，则返回所有的数据
  # universe: 返回的股票列表，如果不指定，则返回所有的股票
  params1 = {
      # "date": 20240220,
      "last_good": False,
      "start": 0,
      "length": 260,
      "universe": ["000001.SZ"],
      "auction": True,
  }

  klineds192 = PyGsfClient(host="192.168.1.192", port=60010)  # 请填入实际的地址和端口
  # klineds188 = PyGsfClient(host="192.168.1.188", port=40015)  # 请填入实际的地址和端口
  # klineds187 = PyGsfClient(host="192.168.1.187", port=40015)  # 请填入实际的地址和端口

  df1 = klineds192.get_data(serviceName="KLineDs", dataName="*", params=json.dumps(params1))
  # df2 = klineds187.get_data(serviceName="KLineDs", dataName="*", params=json.dumps(params1))
  # df3 = klineds188.get_data(serviceName="KLineDs", dataName="*", params=json.dumps(params1))

  # df1.to_csv('klineds_data_prod192.csv', index=False, encoding='utf-8')
  # df2.to_csv('klineds_data_prod187.csv', index=False, encoding='utf-8')
  # df3.to_csv('klineds_data_prod188.csv', index=False, encoding='utf-8')

  print("\033[1;31m\n192打印\033[0m\n", df1)
  # print("\033[1;31m\n187打印\033[0m\n", df2)
  # print("\033[1;31m\n188打印\033[0m\n", df3)

if False: 
  params = {
        # "date": 20240220,
        "last_good": False,
        "length": 260,
        "start": 0,
        "auction": True
    }
  
  # client = PyGsfClient(host='192.168.35.14', port=58005)
  # client188 = PyGsfClient(host='192.168.1.188', port=40025)
  # client187 = PyGsfClient(host='192.168.1.187', port=40025)
  client192 = PyGsfClient(host='192.168.1.192', port=40037)
  client192.SetGoals(au_codes=['1000000'], goal_positions=[0], symbols=['688006.SH'])
  df192 = client192.get_data(serviceName="BarDs", dataName='OPEN', params=json.dumps(params))
  print(df192)