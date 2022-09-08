def say_hi_bye(name, num):
    # write your code here
    if num == int(0):
        return "Bye" + ' ' + name
    else:
        return "Hi" + ' ' + name


def say_hi_bye1(name: str, num: int): return "Bye %s" % name if num == int(0) else "Hi %s" % name
