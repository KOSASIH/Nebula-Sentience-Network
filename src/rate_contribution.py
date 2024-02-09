class ReputationSystem:
    def __init__(self):
        self.reputation_scores = {}

    def rate_contribution(self, user_id, rating):
        if user_id not in self.reputation_scores:
            self.reputation_scores[user_id] = []
        self.reputation_scores[user_id].append(rating)

    def get_reputation_score(self, user_id):
        if user_id not in self.reputation_scores:
            return 0
        return sum(self.reputation_scores[user_id]) / len(self.reputation_scores[user_id])

    def display_reputation_scores(self):
        for user_id, scores in self.reputation_scores.items():
            avg_score = sum(scores) / len(scores)
            print(f"User {user_id}: Reputation Score {avg_score}")


# Example usage
reputation_system = ReputationSystem()

# Rate contributions
reputation_system.rate_contribution("user1", 4)
reputation_system.rate_contribution("user1", 5)
reputation_system.rate_contribution("user2", 3)
reputation_system.rate_contribution("user2", 2)
reputation_system.rate_contribution("user2", 4)

# Display reputation scores
reputation_system.display_reputation_scores()
