import sys,os,json

enviro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(enviro_path)


def cardmanage():
    option = input("请输入你的操作 添加/提额/冻结：")
    if option == "添加":
        with open(os.path.join(enviro_path, r"CARD\pcard"), "r", encoding="utf8") as card_data:
            card_data = json.load(card_data)
        name = input("请输入你的姓名：")
        card_data[name] = {"卡号":"987654","密码":"987","余额":"15000","额度":"15000"}
        with open(os.path.join(enviro_path, r"CARD\pcard"), "w", encoding="utf8") as card_write:
            data = json.dump(card_data,card_write,ensure_ascii=False)
        print("添加账户成功！")

    if option == "提额":
        with open(os.path.join(enviro_path, r"CARD\pcard"), "r", encoding="utf8") as card_data:
            card_data = json.load(card_data)
            person = input("请输入提额姓名：")
            print("最大额度可调整为20000元。")
            card_data[person]["额度"] = 20000
            with open(os.path.join(enviro_path, r"CARD\pcard"), "w", encoding="utf8") as card_write:
                data = json.dumps(card_data, ensure_ascii=False)
                card_write.write(data)
            print("提额成功！")

    if option == "冻结":
        person = input("请输入你要冻结的账户：")
        with open(os.path.join(enviro_path, r"CARD\pcard"), "r", encoding="utf8") as card_data:
            card_data = json.load(card_data)
        del card_data[person]
        with open(os.path.join(enviro_path, r"CARD\pcard"), "w", encoding="utf8") as card_write:
            data = json.dumps(card_data, ensure_ascii=False)
            card_write.write(data)
        print("冻结成功！")


if __name__ == "__main__":
    cardmanage()