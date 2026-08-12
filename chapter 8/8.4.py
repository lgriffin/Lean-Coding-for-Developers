# AI-generated fix: retry until user appears
def test_user_exists():
    user = create_test_user()
    for attempt in range(5):
        if db.find_user(user.id):
            break
        time.sleep(0.1)
    assert db.find_user(user.id) is not None
