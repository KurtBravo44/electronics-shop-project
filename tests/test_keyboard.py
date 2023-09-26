from src.keyboard import Keyboard

kb_1 = Keyboard('Varmillo', 20000, 5)
def test_change_lang():
    assert kb_1.language == 'EN'
    kb_1.change_lang()
    assert kb_1.language == 'RU'
    kb_1.change_lang()
    assert kb_1.language == 'EN'