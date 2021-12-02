from ruamel import yaml
#yaml_file 是yml后缀文件的路径
#d是读取yml文件得到的dictionary
def readYaml(yaml_file):
    gt_dic = {}
    f = open(yaml_file , 'r', encoding='utf-8')
    cfg = f.read()
    d= yaml.safe_load(cfg)
    return d
