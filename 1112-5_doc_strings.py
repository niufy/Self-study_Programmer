def retrun_float(str):
    """
    Convert to flat from string
    :param str: string.
    :param x  : float.
    :return   : x
    """

    try:
        x=float(str)
        return x
    except(ValueError):
        print("変換できませんでした。")

print(retrun_float("test"))
