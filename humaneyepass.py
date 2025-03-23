import argparse
import secrets

_DEFAULT_UPPERCASE = "ABCDFGHJKLMNPQRTUVWXYZ"
_DEFAULT_LOWERCASE = "abcdefghikmnpqrtuvwxyz"
_DEFAULT_DIGITS = "23456789"
_DEFAULT_SPECIAL = "!@#$&*-"

def generate_password(length=12, uppercase_chars=None,
                      lowercase_chars=None, digit_chars=None,
                      special_chars=None):
    categories = {
        "uppercase": list(uppercase_chars),
        "lowercase": list(lowercase_chars),
        "digits": list(digit_chars),
        "special": list(special_chars)
    }

    password = [
        secrets.choice(categories["uppercase"]),
        secrets.choice(categories["lowercase"]),
        secrets.choice(categories["digits"]),
        secrets.choice(categories["special"])
    ]

    for _ in range(length - 4):
        category_type = secrets.choice(list(categories.values()))
        password.append(secrets.choice(category_type))
    
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(
        description="人間が読みやすいパスワード生成ツール",
        epilog="例: python humaneyepass.py -l 'abcxyz' -u 'ABCD' --specialChars '!@#$' -n 20",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-l', '--lowerChars',
                        default=_DEFAULT_LOWERCASE,
                        help=f"小文字の許可リスト。デフォルト: {_DEFAULT_LOWERCASE}")
    
    parser.add_argument('-u', '--upperChars',
                        default=_DEFAULT_UPPERCASE,
                        help=f"大文字の許可リスト。デフォルト: {_DEFAULT_UPPERCASE}")

    parser.add_argument('-d', '--digits',
                        default=_DEFAULT_DIGITS,
                        help=f"数字の許可リスト。デフォルト: {_DEFAULT_DIGITS}")
    
    parser.add_argument('-s', '--specialChars',
                        default=_DEFAULT_SPECIAL,
                        help=f"特殊文字の許可リスト。デフォルト: {_DEFAULT_SPECIAL}")
    
    parser.add_argument('-n', '--length',
                        type=int, default=12,
                        help="パスワードの総文字数。デフォルト: 12")

    args = parser.parse_args()

    uppercase = args.upperChars or _DEFAULT_UPPERCASE
    lowercase = args.lowerChars or _DEFAULT_LOWERCASE
    digits_set = args.digits or _DEFAULT_DIGITS
    special = args.specialChars or _DEFAULT_SPECIAL

    password = generate_password(
        length=args.length,
        uppercase_chars=uppercase,
        lowercase_chars=lowercase,
        digit_chars=digits_set,
        special_chars=special
    )

    print(f"生成されたパスワード: {password}")

if __name__ == "__main__":
    main()