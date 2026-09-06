"""
Multi-Agent Round-Robin Turn Orchestrator and Speaker Router.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any, Optional

class RoundRobinTurnOrchestratorClient:
    """
    Coordinates turn-taking across multi-agent group chats (AutoGen / CrewAI style):
    - Round-robin circular queue
    - Dynamic next-speaker override via `@mention` tags
    - Max turn ceilings and termination signal detection
    """

    def __init__(self, agent_roles: List[str], max_turns: int = 10, termination_keyword: str = "TERMINATE"):
        self.roles = agent_roles
        self.max_turns = max_turns
        self.term_kw = termination_keyword
        self.current_turn = 0
        self.history = []

    def get_next_speaker(self, last_message: Optional[str] = None) -> Optional[str]:
        """Determines the next speaker based on mentions or circular round-robin."""
        if self.current_turn >= self.max_turns:
            return None

        # Check for explicit mention: @Role
        if last_message:
            for role in self.roles:
                if f"@{role.lower()}" in last_message.lower():
                    return role

        # Standard circular round-robin
        speaker_idx = self.current_turn % len(self.roles)
        return self.roles[speaker_idx]

    def submit_turn(self, speaker: str, content: str) -> Dict[str, Any]:
        """Records agent utterance, checks termination conditions, and routes next speaker."""
        self.current_turn += 1
        entry = {"turn": self.current_turn, "speaker": speaker, "content": content}
        self.history.append(entry)

        is_terminated = (self.term_kw.lower() in content.lower()) or (self.current_turn >= self.max_turns)
        next_speaker = None if is_terminated else self.get_next_speaker(content)

        return {
            "recorded_turn": self.current_turn,
            "speaker": speaker,
            "terminated": is_terminated,
            "next_speaker": next_speaker,
            "turns_remaining": max(0, self.max_turns - self.current_turn)
        }
