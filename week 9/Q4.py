import re

def validate_pattern(input_string, pattern):
    if re.match(pattern, input_string):
        return True
    else:
        return False


email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email = 'example@email.com'
is_valid_email = validate_pattern(email, email_pattern)
print(f"Is {email} a valid email address? {is_valid_email}")


bd_mobile_pattern = r'^01\d{9}$'
bd_mobile = '01712345678'
is_valid_bd_mobile = validate_pattern(bd_mobile, bd_mobile_pattern)
print(f"Is {bd_mobile} a valid Bangladesh mobile number? {is_valid_bd_mobile}")


us_telephone_pattern = r'^\d{10}$'
us_telephone = '1234567890'
is_valid_us_telephone = validate_pattern(us_telephone, us_telephone_pattern)
print(f"Is {us_telephone} a valid USA telephone number? {is_valid_us_telephone}")


password_pattern = r'^[A-Za-z0-9!@#$%^&*()_+=\-[\]{}|;:\'",.<>?]{16}$'
password = 'MyP@ssw0rd123456!'
is_valid_password = validate_pattern(password, password_pattern)
print(f"Is '{password}' a valid 16-character Alpha-Numeric password? {is_valid_password}")
