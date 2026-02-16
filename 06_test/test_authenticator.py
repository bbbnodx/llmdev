import pytest
from authenticator import Authenticator


@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth
    auth.users.clear()


def test_register(authenticator):
    authenticator.register("foo", "bar")
    assert "foo" in authenticator.users
    assert authenticator.users["foo"] == "bar"


def test_duplicated_register(authenticator):
    authenticator.register("foo", "bar")
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("foo", "foobar")


def test_login(authenticator):
    authenticator.register("foo", "bar")
    assert authenticator.login("foo", "bar") == "ログイン成功"


def test_login_failure(authenticator):
    authenticator.register("foo", "bar")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("foo", "foobar")
