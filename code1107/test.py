def process_data(data):
    try:
        if not isinstance(data, int):
            raise TypeError("数据必须是整数")
        # 处理数据的代码
        return data * 2
    except TypeError as e:
        print("捕获到类型错误，重新抛出异常")
        raise

try:
    result = process_data("abc")
except TypeError as e:
    print(f"最终捕获到异常: {e}")