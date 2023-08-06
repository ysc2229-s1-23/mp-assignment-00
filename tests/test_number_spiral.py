from questions.number_spiral import number_spiral

def test_number_spiral():
    assert number_spiral(1, 1) == 1, "Test 1 failed"
    assert number_spiral(2, 3) == 8, "Test 2 failed"
    assert number_spiral(3, 1) == 5, "Test 3 failed"
    assert number_spiral(170550340, 943050741) == 889344699930098742, "Test 4 failed"
    assert number_spiral(121998376, 943430501) == 890061110095112626, "Test 5 failed"
    assert number_spiral(689913499, 770079066) == 593021767041187724, "Test 6 failed"
    assert number_spiral(586095107, 933655238) == 871712102163621276, "Test 7 failed"
    assert number_spiral(704012672, 608536365) == 495633841728043220, "Test 8 failed"
    assert number_spiral(982851657, 940887637) == 965997378642829973, "Test 9 failed"
    assert number_spiral(934775085, 320910984) == 873804457988118040, "Test 10 failed"
    assert number_spiral(315532821, 833740973) == 695124009743453909, "Test 11 failed"
    assert number_spiral(5778293, 8061369) == 64985664375869, "Test 12 failed"
    assert number_spiral(941416062, 502819867) == 886264201288767978, "Test 13 failed"
