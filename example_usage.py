"""
Demonstration of genpark-multi-agent-round-robin-turn-orchestrator-skill
"""

from client import RoundRobinTurnOrchestratorClient

def main():
    agents = ["Researcher", "Coder", "Reviewer"]
    orchestrator = RoundRobinTurnOrchestratorClient(agents, max_turns=5)

    print("Initial Speaker:", orchestrator.get_next_speaker())

    # Turn 1: Researcher speaks, hands off to Coder
    t1 = orchestrator.submit_turn("Researcher", "Found the API docs. @Coder please implement the fetcher.")
    print("Turn 1 Result:", t1)

    # Turn 2: Coder implements and passes to Reviewer
    t2 = orchestrator.submit_turn(t1["next_speaker"], "Fetcher implemented. @Reviewer check the logic.")
    print("Turn 2 Result:", t2)

    # Turn 3: Reviewer approves with TERMINATE
    t3 = orchestrator.submit_turn(t2["next_speaker"], "Code verified and passes all tests. TERMINATE")
    print("Turn 3 Result:", t3)

if __name__ == "__main__":
    main()
