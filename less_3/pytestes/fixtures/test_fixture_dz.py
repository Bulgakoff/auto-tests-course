import pytest

# У нас есть набор тестов, который использует несколько фикстур.
# Посчитайте, сколько смайликов будет напечатано при
# выполнении этого тестового класса?
# выполднится только один раз для :
# def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")

# тут пройдет тк вписана аргментом в тест
@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")

#  autouse=True, который укажет, что фикстуру нужно
#  запустить для каждого теста даже без явного вызова: здесь
#  для   def test_first_smiling_faces() и
#  def test_second_smiling_faces(self, prepare_faces):
@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        ...
        # какие-то проверки
    # не смотря что вписана prepare_faces() не будет смайла "^_^" тк как
    # scope="class" , а произойдет teardown (yield
    #     print(":3", "\n"))
    def test_second_smiling_faces(self, prepare_faces):
        ...
        # какие-то проверки