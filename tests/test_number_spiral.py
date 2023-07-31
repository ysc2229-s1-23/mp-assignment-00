from questions.number_spiral import number_spiral

def test_number_spiral():
    assert number_spiral(1, 1) == 1
    assert number_spiral(2, 3) == 8
    assert number_spiral(3, 1) == 5
    assert number_spiral(170550340, 943050741) == 889344699930098742
    assert number_spiral(121998376, 943430501) == 890061110095112626
    assert number_spiral(689913499, 770079066) == 593021767041187724
    assert number_spiral(586095107, 933655238) == 871712102163621276
    assert number_spiral(704012672, 608536365) == 495633841728043220
    assert number_spiral(982851657, 940887637) == 965997378642829973
    assert number_spiral(934775085, 320910984) == 873804457988118040
    assert number_spiral(315532821, 833740973) == 695124009743453909
    assert number_spiral(5778293, 8061369) == 64985664375869
    assert number_spiral(941416062, 502819867) == 886264201288767978
