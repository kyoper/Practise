import sys,os

enviro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(enviro_path)

import json
from LOG import logger
def shopping():
    with open(os.path.join(os.path.abspath(".."),r"SHOP\userid.txt"),"r",encoding="utf8") as f:
        user = f.read()
    user_data = json.loads(user)

    flag = True
    while flag:
        userid = input("请输入用户名:")
        userpword = input("请输入密码:")
        for p in user_data:
            if user_data[p]["账户"] == userid and user_data[p]["密码"] == userpword :
                with open(os.path.join(os.path.abspath(".."),r"SHOP\goods.txt"),"r",encoding = "utf8") as f_goods:
                    goods_list = json.loads(f_goods.read())
                for items in goods_list:
                    print("    ".join((items,goods_list[items])))
                customer_choose = input("请输入你购买的商品：")
                if customer_choose in goods_list:
                    pcardpath =os.path.join(os.path.abspath(".."),r"CARD\pcard")
                    with open(pcardpath,"r",encoding="utf8") as pcardread:
                        card_data = json.loads(pcardread.read())

                    flag1 = True
                    while   flag1 :
                        cardid = input("请输入你的卡号：")
                        cardpword = input("请输入你的密码：")
                        if cardid == card_data[p]["卡号"] and cardpword == card_data[p]["密码"]:
                            flag1 = False
                            money = float(card_data[p]["余额"]) - float(goods_list[customer_choose])
                            card_data[p]["余额"] = money

                            if money < float(goods_list[customer_choose]):
                                print("你的余额不足无法购买！")
                            else:

                                logger.logcard(float(goods_list[customer_choose]),money)
                                logger.log(customer_choose, float(goods_list[customer_choose]))
                                print("你已购买%s,余额为%d,欢迎下次光临！"%(customer_choose,money))
                                with open(pcardpath,"w",encoding = "utf8") as pcardwrite:
                                    json.dump(card_data,pcardwrite,ensure_ascii = False)




                        else:
                            print("输入的卡号或密码不正确请重新输入")

                else:
                    print("输入非法请重新输入：")

                print("开始购物")
                flag = False
        if flag == True:
            print("你输入的用户名或密码不正确请重新输入：")


if __name__ == "__main__":

    shopping()

