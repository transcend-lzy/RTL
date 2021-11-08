from ruamel import yaml

def readYaml(yaml_file):
    gt_dic = {}
    f = open(yaml_file , 'r', encoding='utf-8')
    cfg = f.read()
    d= yaml.safe_load(cfg)
    return d
