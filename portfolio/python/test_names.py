# from names import make_full_name, \
#     extract_family_name, extract_given_name
# import pytest

# def test_make_full_name():
    
#     assert make_full_name('Efe', 'Enahoro') == 'Enahoro; Efe'    

# def test_extract_family_name():
    
#     assert extract_family_name('Enahoro; Efe') == 'Enahoro'

# def test_extract_given_name():
    
#     assert extract_given_name('Enahoro; Efe') == 'Efe'

# pytest.main(["-v", "--tb=line", "-rN", __file__])  
    

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    #assert make_full_name('Kija', 'Hesron') == 'Hesron; Kija'
    assert make_full_name('Efe', 'Enahoro') == 'Enahoro; Efe'
    assert make_full_name('Joyce',  'Jensen') == 'Jensen; Joyce'
    assert make_full_name('Natalie', 'Jonhson') == 'Jonhson; Natalie'

def test_extract_family_name():
    assert extract_family_name('Kija; Hesron') == 'Kija'
    assert extract_family_name('Enahoro; Efe' ) == 'Enahoro'
    assert extract_family_name('Jensen; Joyce') == 'Jensen'
    assert extract_family_name('Jonhson; Natalie') == 'Jonhson'
    
def test_extract_given_name():
    assert extract_given_name('Kija; Hesron') == 'Hesron'
    assert extract_given_name('Enahoro; Efe' ) == 'Efe'
    assert extract_given_name('Jensen; Joyce') == 'Joyce'
    assert extract_given_name('Jonhson; Natalie') == 'Natalie'
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])