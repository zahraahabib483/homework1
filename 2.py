def is_valid_binary(binary_str):
    """التحقق مما إذا كانت السلسلة المدخلة رقم ثنائي صالح."""
    for char in binary_str:
        if char not in ('0', '1'):
            return False
    return True

def binary_to_decimal(binary_str):
    """تحويل سلسلة ثنائية إلى رقم عشري."""
    decimal_number = 0
    binary_str = binary_str[::-1]  # عكس السلسلة لتسهيل الحساب
    for i in range(len(binary_str)):
        decimal_number += int(binary_str[i]) * (2 ** i)
    return decimal_number

def main():
    while True:
        binary_str = input("أدخل رقمًا ثنائيًا: ").strip()
        if is_valid_binary(binary_str):
            decimal_number = binary_to_decimal(binary_str)
            print(f"المكافئ العشري للرقم الثنائي {binary_str} هو {decimal_number}.")
            break
        else:
            print("إدخال غير صالح. يرجى إدخال رقم ثنائي صحيح (يحتوي فقط على 0 و 1).")

if __name__ == "__main__":
    main()
