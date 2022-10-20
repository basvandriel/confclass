def test_import():
    import confclass

    assert confclass.__package__ == 'confclass'