import logging,os
def log(a,b):
    logger = logging.getLogger("购物日记")
    fomatter = logging.Formatter("%(asctime)s:  %(message)s")
    filehandler = logging.FileHandler(os.path.join(os.path.abspath(".."),r"LOG\shoplog.txt"),encoding = "utf8")
    filehandler.formatter = fomatter
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)

    return logger.info("购入 %s 花费 %d"%(a,b))


def logcard(a,b):
    logger= logging.getLogger("信用卡消费日记")
    fomatter = logging.Formatter("%(asctime)s:  %(message)s")
    filehandler = logging.FileHandler(os.path.join(os.path.abspath(".."),r"LOG\cardlog.txt"),encoding = "utf8")
    filehandler.formatter = fomatter
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)

    return  logger.info("信用卡消费 %d 元，可用余额 %d 元。"%(a,b))

def logcash(a,b):
    logger= logging.getLogger("信用卡提现")
    fomatter = logging.Formatter("%(asctime)s:  %(message)s")
    filehandler = logging.FileHandler(os.path.join(os.path.abspath(".."),r"LOG\cashlog.txt"),encoding = "utf8")
    filehandler.formatter = fomatter
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)

    return  logger.info("信用卡提现 %f 元，可用余额 %f 元。"%(a,b))

def logtrans(a):
    logger = logging.getLogger("信用卡转账")
    fomatter = logging.Formatter("%(asctime)s:  %(message)s")
    filehandler = logging.FileHandler(os.path.join(os.path.abspath(".."), r"LOG\translog.txt"), encoding="utf8")
    filehandler.formatter = fomatter
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)

    return logger.info("你成功转账 %f 元。" %float(a))

def logrepay(a,b):
    logger = logging.getLogger("信用卡还款")
    fomatter = logging.Formatter("%(asctime)s:  %(message)s")
    filehandler = logging.FileHandler(os.path.join(os.path.abspath(".."), r"LOG\repaylog.txt"), encoding="utf8")
    filehandler.formatter = fomatter
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)

    return logger.info("你已还款 %f 元，账户余额 %f 元。" % (a,b))

if __name__ == "__main__":
    logcard(123,12)