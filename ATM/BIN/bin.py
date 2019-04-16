import sys,os

enviro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(enviro_path)

from SHOP import shopping
from CARD import trading,manage

shopping.shopping()     #信用卡购物
# trading.atm()        #信用卡转账/提现/还款
# manage.cardmanage()     #信用卡管理 添加/提额/冻结
