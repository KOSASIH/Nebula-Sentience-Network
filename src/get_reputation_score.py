class ReputationSystem:
    def __init__(self):
        self.reputation_scores = {}

    def rate_contribution(self, contributor, rating):
        if contributor not in self.reputation_scores:
            self.reputation_scores[contributor] = []
        self.reputation_scores[contributor].append(rating)

    def get_reputation_score(self, contributor):
        if contributor not in self.reputation_scores:
            return 0
        return sum(self.reputation_scores[contributor]) / len(self.reputation_scores[contributor])

    def display_reputation_scores(self):
        for contributor, scores in self.reputation_scores.items():
            avg_score = sum(scores) / len(scores)
            print(f"{contributor}: Reputation Score - {avg_score}")


# Example usage
reputation_system = ReputationSystem()

# Rate contributions
reputation_system.rate_contribution("User1", 4)
reputation_system.rate_contribution("User1", 5)
reputation_system.rate_contribution("User2", 3)
reputation_system.rate_contribution("User3", 4)
reputation_system.rate_contribution("User3", 2)

# Get and display reputation scores
reputation_system.display_reputation_scores()
