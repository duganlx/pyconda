import re

if __name__ == '__main__':
  strs = [
    'ssh root@192.168.1.192 "docker pull jfrog.jhlfund.com/docker/eam/wwds:1.1.6"',
    'ssh root@192.168.1.192 \'docker pull jfrog.jhlfund.com/docker/eam/wwds:1.1.6\''
  ]

  for str in strs:
    aim = re.findall(r"docker pull ([^\"\']*)", str)[0] # jfrog.jhlfund.com/docker/eam/wwds:1.1.6
    # aim = re.findall(r"docker pull .*:([^\"\']*)", str)[0] # 1.1.6
    print(aim)
