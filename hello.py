def check_score(score):
    try:
        score = int(score)
        if score < 0 or score > 100:
            raise ValueError
    except ValueError:
        return "Invalid score"
    else:
        return "Valid score"
print(check_score("85"))     # Valid score
print(check_score("hello"))  # Invalid score
print(check_score("-10"))    # Invalid score
print(check_score("120"))    # Invalid score
