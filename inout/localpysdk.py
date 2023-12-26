import os
import pandas as pd

class LocalPySdk(object):
  datafolder_path = ''

  def __init__(self) -> None:
    current_path = os.path.dirname(os.path.abspath(__file__))
    # pyfolder_path = os.path.dirname(current_path)
    rootfolder_path = os.path.dirname(current_path)
    datafolder_path = f"{rootfolder_path}/data"

    self.datafolder_path = datafolder_path

  def getData(self, dir='', filename=''):
    if self.datafolder_path == '':
      raise Exception("data folder path is not configured")

    if len(dir) > 0:
      df = pd.read_csv(f"{self.datafolder_path}/{dir}/{filename}")
    else:
      df = pd.read_csv(f"{self.datafolder_path}/{filename}")

    return df

  def savedf(self, df: pd.DataFrame, dir: str = '', filename: str = ''):
    if self.datafolder_path == '':
      raise Exception("data folder path is not configured")

    if len(dir) > 0:
      df.to_csv(f"{self.datafolder_path}/{dir}/{filename}", index=False)
      print(f"df has save in {self.datafolder_path}/{dir}/{filename}")
    else:
      df.to_csv(f"{self.datafolder_path}/{filename}", index=False)
      print(f"df has save in {self.datafolder_path}/{filename}")