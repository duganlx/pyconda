# 安装pygsf, 请使用以下命令
# pip install -U pygsf -i https://jfrog.jhlfund.com/artifactory/api/pypi/py/simple
import json
from pygsf import PyGsfClient, PyGsfRpc

def indexDs():
  params = {
      # "date": 20240305,
      "benchmark": "000016.SH",
  }

  cli = PyGsfClient(host="192.168.1.192", port=58005)
  df = cli.get_data(serviceName="IndexDs", dataName="sz50_weight", params=json.dumps(params))
  return df


def barDs():
  params = {
        # "date": 20240220,
        "last_good": False,
        "length": 260,
        "start": 0,
        "auction": True
    }
  
  cli = PyGsfClient(host='192.168.1.187', port=40025)
  df = cli.get_data(serviceName="BarDs", dataName='OPEN', params=json.dumps(params))
  return df


def kLineDs():
  params = {
      # "date": 20240305,
      "last_good": False,
      "start": 0,
      "length": 260,
      "universe": ["600028.SH", "600030.SH"],
      "auction": True,
  }

  cli = PyGsfClient(host="192.168.1.187", port=60009)
  df = cli.get_data(serviceName="KLineDs", dataName="*", params=json.dumps(params))
  return df


if __name__ == '__main__':
  # df = barDs()
  df = indexDs()
  print(df)
