# Write the main.py file in the current directory
with open("main.py&quot;, "w") as f:
    f.write("""
from recommender.outfit_recommender import OutfitRecommender
def main():
    recommender = OutfitRecommender("data/outfits.csv")
    print("Recommendations for color='Red', occasion='Party'")
    print(recommender.recommend(color='Red', occasion='Party'))
if __name__ == "__main__":
    main()
""")
