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
import pandas as pd
import numpy as np


def normalize(df):
  numdf = df[['pre_close', 'open', 'high', 'low', 'close', 'total_vol', 'total_amt', 'upper_limit', 'lower_limit']]
  colsmax = numdf.max(axis="index")
  colsmin = numdf.min(axis="index")
  
  disdf = numdf - colsmin
  colsdis = colsmax - colsmin
  normdf = disdf / colsdis

  merged_df = pd.concat([df[['trade_date', 'symbol']], normdf], axis=1)
  return merged_df


def generate_label(df):
  keydf = df[['trade_date', 'pre_close', 'close']]
  labels = keydf['pre_close'] < keydf['close']
  labels = labels.replace({True: 'up', False: 'down'})
  labels = pd.Series(labels, name=f'label')

  return labels


def discretize(df):
  numdf = df[['pre_close', 'open', 'high', 'low', 'close', 'total_vol', 'total_amt', 'upper_limit', 'lower_limit']]

  def map_to_category(value):
    if value < 0.3:
      return 's'
    elif value < 0.5:
      return 'm'
    elif value < 0.9:
      return 'l'
    else:
      return 'xl'

  numdf = numdf.applymap(map_to_category)
  merged_df = pd.concat([df[['trade_date', 'symbol']], numdf], axis=1)
  return merged_df


def label_distribution(df):
  numdf = df[['pre_close', 'open', 'high', 'low', 'close', 'total_vol', 'total_amt', 'upper_limit', 'lower_limit']]
  # value_distribution = numdf.apply(pd.Series.value_counts)
  # value_distribution = value_distribution / len(numdf)
  # logdf = np.log2(value_distribution)
  # hdf = value_distribution * logdf

  print(numdf)


if __name__ == '__main__':
  choose = False
  filename = 'gzmt_decisiontree_dev.csv'
  lcsdk = LocalPySdk()

  if choose:
    eamsdk = EamPySdk()
    df = eamsdk.getBardayData(universe=['600519.SH'], where="trade_date > '2023-10-01'")
    eamsdk.savedf(df, filename=filename)
  else:  
    df = lcsdk.getData(filename=filename)
  
  # module 1: data prepare
  df = normalize(df)
  labels = generate_label(df)
  df = discretize(df)
  df = pd.concat([df, labels], axis=1)

  # module 2: decision tree
  label_distribution(df)

