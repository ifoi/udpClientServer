import pytest


# test command line argument

# verify  input

cmd_inputs = [("client", "client"),
              ("server", "server"),
              ("misc", "tryAgain")]


@pytest.mark.parametrize("str, cmd_input", cmd_inputs)
def test_cmd_input(str, cmd_input):
    assert str == cmd_input


# call client

# call server
