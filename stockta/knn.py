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

  merged_df = pd.concat([df, labels], axis=1)
  return merged_df


def split_dataset(df):
  split_index = int(len(df) * 0.8)

  part1 = df.iloc[:split_index, :]
  part2 = df.iloc[split_index:, :]

  return part1, part2


def knn_classify(inx, dataset, labels, k):
  inxmat = pd.concat([inx] * len(dataset), axis=1).T.reset_index(drop=True)
  diffmat = inxmat - dataset
  sqDiffmat = diffmat ** 2
  sqdis = sqDiffmat.sum(axis='columns')
  sqdis = sqdis ** 0.5
  sqdis = pd.Series(sqdis, name='dis')
  euclideanDis = pd.concat([sqdis, labels], axis=1)
  sorteddf = euclideanDis.sort_values(by='dis')
  aimSorteddf = sorteddf.iloc[:k, :]
  labelcnt = aimSorteddf['label'].value_counts()
  if labelcnt['up'] > labelcnt['down']:
    return 'up'
  else:
    return 'down'


if __name__ == '__main__':
  choose = False
  filename = 'gzmt_dev.csv'
  lcsdk = LocalPySdk()

  if choose:
    eamsdk = EamPySdk()
    df = eamsdk.getBardayData(universe=['600519.SH'], where="trade_date > '2023-10-01'")
    eamsdk.savedf(df, filename=filename)
  else:  
    df = lcsdk.getData(filename=filename)

  # module 2: kNN
  # == begin ==
  traindf, testdf = split_dataset(df)
  xtraindf, ytrain = traindf.iloc[:, 2:-1], traindf.iloc[:, -1]
  xtestf, ytest = testdf.iloc[:, 2:-1], testdf.iloc[:, -1]
  for _, row in xtestf.iterrows():
    expected = knn_classify(row, xtraindf, ytrain, 10)
    print(expected)
    break
  # == end ==

  # module 1: data prepare 
  # == begin ==
  # df = normalize(df)
  # df = generate_label(df)
  # lcsdk.savedf(df, filename=filename)
  # == end ==
  
