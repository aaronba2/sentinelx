BAD_AGENTS=[
"curl",
"python",
"wget",
"sqlmap",
"nikto",
"nmap"
]

def suspicious_agent(agent):

    agent=agent.lower()

    for bad in BAD_AGENTS:
        if bad in agent:
            return True

    return False
