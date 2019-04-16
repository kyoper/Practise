import sys, os, json

enviro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(enviro_path)
from LOG import logger



def authentication(f):
    def inner():
        choose = input("确定使用建行信用卡 y/n:")
        if choose == "y":
            f()
        else:
            print("大兄弟你再考虑一下。")
    return inner

@authentication
def atm():
    flag = True
    while flag:
        cardid = input("请输入你的卡号：")
        cardpword = input("请输入你的密码：")
        with open(os.path.join(enviro_path, r"CARD\pcard"), "r", encoding="utf8") as card_data:
            card_data = json.load(card_data)
        for p in card_data:
            if cardid == card_data[p]["卡号"] and cardpword == card_data[p]["密码"]:
                option = input("请输入你的操作 提现/转账/还款 ：")
                if option == "提现":
                    getmoney = input("请输入要提现的金额，可提取最大金额 %f:" % (float(card_data[p]["余额"]) / 1.05))
                    card_data[p]["余额"] = float(card_data[p]["余额"]) - float(getmoney) * 1.05
                    logger.logcash(float(getmoney), card_data[p]["余额"])
                    with open(os.path.join(enviro_path, r"CARD\pcard"), "w", encoding="utf8") as card_write:
                        json.dump(card_data, card_write, ensure_ascii=False)
                    print("提现成功！")
                    flag = False
                if option  == "转账":
                    to_person = input("请输入对方账号：")
                    transmoney = input("请输入转账金额：")
                    for x in card_data:
                        if card_data[x]["卡号"] == to_person:
                            card_data[p]["余额"] = float(card_data[p]["余额"]) - float(transmoney)
                            card_data[x]["余额"] = float(card_data[x]["余额"]) + float(transmoney)
                            with open(os.path.join(enviro_path, r"CARD\pcard"), "w", encoding="utf8") as card_write:
                                data = json.dumps(card_data,ensure_ascii=False)
                                card_write.write(data)
                            print("转账成功！")
                            logger.logtrans(transmoney)
                            flag = False
                if option == "还款":
                    debt = card_data[p]["额度"] - float(card_data[p]["余额"])
                    print("你本月应还 %f 元。"%debt)
                    repay = input("还款金额：")
                    card_data[p]["余额"] = float(card_data[p]["余额"]) + float(repay)
                    with open(os.path.join(enviro_path, r"CARD\pcard"), "w", encoding="utf8") as card_write:
                        data = json.dumps(card_data, ensure_ascii=False)
                        card_write.write(data)
                    logger.logrepay(float(repay),card_data[p]["余额"])
                    print("你已还 %f 元，账户余额 %f 元。"%(float(repay),card_data[p]["余额"]))
                    flag = False
        list_pvalues = list(card_data.values())
        list_cvalues = []
        for i in list_pvalues:
            list_cvalues.append(i["卡号"])
        if cardid not in list_cvalues:
            print("你输入的卡号或密码不正确请重新输入：")


if __name__ == "__main__":
    # getmoney()
    atm()