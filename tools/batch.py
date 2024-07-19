from .base import *
from ._batch import _import, export

tool = Tool(1)
tool.name = 'Batch'
tool.name_zh = '批量'
tool.action.tools = [_import.tool, export.tool]
