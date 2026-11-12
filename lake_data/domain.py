"""核对统计字段编号与文件数量，不裁剪。"""
from .io import unique,integer

def summarize(v,root):
    fields={f['id'] for f in v['schema']};unique(v['files'],'id')
    for f in v['files']:
        integer(f['record_count'])
        if any(int(k) not in fields for k in f['metrics']):raise ValueError('统计引用未知列')
    return {'files':len(v['files']),'fields':len(fields),'declared_rows':sum(f['record_count'] for f in v['files'])}
