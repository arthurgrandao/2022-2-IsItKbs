# Os testes estão aqui pois o arquivo existente no projeto utiliza o pacote no pip para realização dos testes,
# então para efeitos práticos, eu coloquei o arquivo no mesmo módulo em que se encontra a classe com a funcionalidade
# a ser testada

import pytest
from .ks import isitkbs

rf_object = isitkbs("randomforest")

# TDD PTOSS4
@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Hello there xsadaddsa son", "Hello there son", "1"),
])
def test_custom_replace_kbs_remove_instance(monkeypatch, string, expected_output, user_inputs):
    monkeypatch.setattr('builtins.input', lambda x: user_inputs)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output


@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Hello there xsadaddsa son", "Hello there my son", ["2", "my"]),
])
def test_custom_replace_kbs_replace_instance(monkeypatch, string, expected_output, user_inputs):
    user_input_index = 0
    def mock_input(prompt):
        nonlocal user_input_index
        user_input = user_inputs[user_input_index]
        user_input_index += 1
        return str(user_input)

    monkeypatch.setattr('builtins.input', mock_input)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output


@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Replace xajdkas and xajdkas", "Replace here and here", ["3", "here"]),
])
def test_custom_replace_kbs_replace_all_instances(monkeypatch, string, expected_output, user_inputs):
    user_input_index = 0
    def mock_input(prompt):
        nonlocal user_input_index
        user_input = user_inputs[user_input_index]
        user_input_index += 1
        return str(user_input)

    monkeypatch.setattr('builtins.input', mock_input)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output


@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Ignore akfjkalf delete xxxxx ignore akfjkalf", "Ignore akfjkalf delete ignore akfjkalf", ["5", "1"]),
])
def test_custom_replace_kbs_ignore_all_instances(monkeypatch, string, expected_output, user_inputs):
    user_input_index = 0
    def mock_input(prompt):
        nonlocal user_input_index
        user_input = user_inputs[user_input_index]
        if user_input_index <= 1: user_input_index += 1
        return str(user_input)

    monkeypatch.setattr('builtins.input', mock_input)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output


@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Ignore akfjkalf ajfklajf jakljlkfj jklafjkl lkjak", "Ignore akfjkalf ajfklajf jakljlkfj jklafjkl lkjak", ["4", "6"])
])
def test_custom_replace_kbs_ignore_and_quit(monkeypatch, string, expected_output, user_inputs):
    user_input_index = 0
    def mock_input(prompt):
        nonlocal user_input_index
        user_input = user_inputs[user_input_index]
        if user_input_index <= 1: user_input_index += 1
        return str(user_input)

    monkeypatch.setattr('builtins.input', mock_input)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output


@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Ignore akfjkalf jklafjkl akfjkalf jklafjkl akfjkalf", "Ignore akfjkalf replace akfjkalf replace2 akfjkalf", ["5", "2", "replace", "2", "replace2"])
])
def test_custom_replace_kbs_ignore_and_remove(monkeypatch, string, expected_output, user_inputs):
    user_input_index = 0
    def mock_input(prompt):
        nonlocal user_input_index
        user_input = user_inputs[user_input_index]
        user_input_index += 1
        return str(user_input)

    monkeypatch.setattr('builtins.input', mock_input)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output


@pytest.mark.parametrize("string, expected_output, user_inputs", [
    ("Ignore akfjkalf jklafjkl akfjkalf jklafjkl akfjkalf", "Ignore replace jklafjkl replace jklafjkl replace", ["3", "replace", "5"])
])
def test_custom_replace_kbs_replace_and_ignore(monkeypatch, string, expected_output, user_inputs):
    user_input_index = 0
    def mock_input(prompt):
        nonlocal user_input_index
        user_input = user_inputs[user_input_index]
        user_input_index += 1
        return str(user_input)

    monkeypatch.setattr('builtins.input', mock_input)  # Mock user input
    
    result = rf_object.custom_replace_kbs(string)
    assert result == expected_output
    

def test_custom_replace_kbs_blank():
    assert rf_object.custom_replace_kbs("") == ""