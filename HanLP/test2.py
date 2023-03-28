from hanlp_restful import HanLPClient
HanLP = HanLPClient('https://www.hanlp.com/api', auth=None, language='zh') # auth不填则匿名，zh中文，mul多语种

print(HanLP.tokenize('商品和服务。阿婆主来到北京立方庭参观自然语义科技公司。'))


HanLP('商品和服务。阿婆主来到北京立方庭参观自然语义科技公司。', tasks='tok').pretty_print()