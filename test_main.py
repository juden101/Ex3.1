import gross_pay  # Import the student script (note: the student script will run upon import)

def test_gross_pay():
    # The test should verify the output; since there's no function, 
    # the test relies on capturing the printed output.
    assert gross_pay.pay == 498.75
