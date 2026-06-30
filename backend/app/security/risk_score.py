def compute_score(
        vpn=False,
        multi_login=False,
        bad_agent=False,
        brute_force=False
):

    score=0

    if vpn:
        score+=25

    if multi_login:
        score+=25

    if bad_agent:
        score+=25

    if brute_force:
        score+=25

    return score
