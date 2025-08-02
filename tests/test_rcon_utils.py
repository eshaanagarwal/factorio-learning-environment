import pytest

from fle.env.utils.rcon import (
    LuaConversionError,
    _check_output_for_errors,
    _lua2python,
)


@pytest.fixture()
def game(instance):
    instance.reset()
    yield instance.namespace


def test_lua_2_python():
    lua_response = '{ ["a"] = false,["b"] = ["string global"],}'
    command = "pcall(global.actions.move_to,1,11.5,20)"
    response, timing = _lua2python(command, lua_response)

    assert response == {"a": False, "b": "string global", 2: "]"}
    assert timing >= 0


def test_lua2python_error():
    error_output = "Unexpected end of string while parsing Lua string."

    with pytest.raises(LuaConversionError):
        _check_output_for_errors("cmd", "resp", error_output)
