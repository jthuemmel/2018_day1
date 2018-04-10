from auth import *
import pytest


#pwdb_path = tempfile.gettempdir() / PWDB_FLNAME
pwdb_path = 'pwdb.pkl'
try:
    pwdb_file = open(pwdb_path, 'rb+')
except FileNotFoundError:
    pwdb_file = open(pwdb_path, 'wb+')

def test_get_salt():
    salt = get_salt()
    assert len(salt) == 10
    assert all(c in CHARS for c in salt)

def test_authenticate():
    salt = get_salt()
    name = 'user'
    wrong_name = 'not_a_user'
    valid_pw = 'valid'
    invalid_pw = 'invalid'
    pwdb = {name:(pwhash(valid_pw,salt),salt)}
    assert authenticate(name,valid_pw,pwdb)
    assert not authenticate(name,invalid_pw,pwdb)
    assert not authenticate(wrong_name,valid_pw,pwdb)

def test_read_write():
    salt = get_salt()
    name = 'user'
    pw = 'password'
    pwdb = {name:(pwhash(pw,salt),salt)}
    write_pwdb(pwdb,pwdb_file)
    pwdb_read = read_pwdb(pwdb_file)
    assert pwdb == pwdb_read
