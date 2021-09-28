def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def testt_abs2():
    assert abs(42) == 42, "Should be absolute vaaaalue of a number"

if __name__ == "__main__":
    test_abs1()
    testt_abs2()
    print("Everything passed")



s = 'My  Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('huh')
if index != -1:
    print(f'Substring found at index {index}')


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
test_substring('fulltext' , 'substring')


