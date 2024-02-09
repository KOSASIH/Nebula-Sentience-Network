class ReputationSystem:
    def __init__(self):
        self.reputation_scores = {}

    def rate_contribution(self, contributor, rating):
        if contributor in self.reputation_scores:
            self.reputation_scores[contributor].append(rating)
        else:
            self.reputation_scores[contributor] = [rating]

    def get_reputation_score(self, contributor):
        if contributor in self.reputation_scores:
            ratings = self.reputation_scores[contributor]
            return sum(ratings) / len(ratings)
        else:
            return 0

    def review_contribution(self, contributor, review):
        # Implement your review functionality here
        pass

# Example usage
reputation_system = ReputationSystem()

# Rate a contribution
reputation_system.rate_contribution("user1", 4)
reputation_system.rate_contribution("user1", 5)
reputation_system.rate_contribution("user2", 3)
reputation_system.rate_contribution("user2", 5)

# Get reputation score
user1_reputation = reputation_system.get_reputation_score("user1")
user2_reputation = reputation_system.get_reputation_score("user2")

# Review a contribution
reputation_system.review_contribution("user1", "Great contribution!")
reputation_system.review_contribution("user2", "Could have been better.")
