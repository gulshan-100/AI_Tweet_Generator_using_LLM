import random

# Mock Social Media Data 
social_media_data = {
    "WOLO": {
        "influencers_following": ["@ansem", "@SmartWhaleTrader"],
        "mentions": ["@ansem mentioned $WOLO", "@CryptoWhale tweeted about $WOLO trending"]
    },
    "MOON": {
        "influencers_following": ["@SmartInvestor", "@TechTrader"],
        "mentions": ["@SmartInvestor is buying $MOON tokens", "@TechTrader shilled $MOON"]
    },
    "PEPE": {
        "influencers_following": ["@CryptoKing", "@TokenGuru"],
        "mentions": ["@TokenGuru hyped $PEPE", "@CryptoKing tweeted about $PEPE gains"]
    },
    "SHIB": {
        "influencers_following": ["@BigWhale", "@WhaleHunter"],
        "mentions": ["@BigWhale is buying $SHIB", "@WhaleHunter loves $SHIB"]
    },
    "DOGE": {
        "influencers_following": ["@DogecoinFan", "@SpaceTrader"],
        "mentions": ["@SpaceTrader is bullish on $DOGE", "@DogecoinFan tweeted about $DOGE being the next big thing"]
    }
}

# Mock On-Chain Data Generator
def generate_mock_onchain_data():
    tokens = ["WOLO", "MOON", "PEPE", "SHIB", "DOGE"]
    return {
        token: {
            "new_wallets": random.randint(5, 50),
            "large_transfers": random.randint(1, 10),
            "total_transfers": random.randint(100, 1000)
        } for token in tokens
    }
