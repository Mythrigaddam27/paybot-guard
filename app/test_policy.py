from app.policy import Policy, evaluate

p = Policy()

def test_auto_approve():
    assert evaluate(10, "books", 0, p)["decision"] == "approve"

def test_needs_approval():
    assert evaluate(40, "books", 0, p)["decision"] == "needs_approval"

def test_over_cap_denied():
    assert evaluate(80, "books", 0, p)["decision"] == "deny"

def test_budget_exceeded():
    assert evaluate(20, "books", 140, p)["decision"] == "deny"

def test_bad_category():
    assert evaluate(5, "gambling", 0, p)["decision"] == "deny"