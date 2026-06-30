from app.services.session_service import count_sessions

def detect_multiple_sessions(db,username):

    sessions=count_sessions(db,username)

    if sessions>=2:
        return True

    return False
