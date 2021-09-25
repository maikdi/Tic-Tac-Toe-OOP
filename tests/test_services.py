from tictactoe import service

def test_should_switch_turn_after_set_piece():
    test_service = service.TictactoeService()
    current_turn = test_service.get_current_turn()
    test_service.set_piece(0,0)
    assert current_turn != test_service.get_current_turn()

def test_check_draw_return_false():
    test_service = service.TictactoeService()
    assert test_service.check_draw() == False

