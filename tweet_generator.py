from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from mock_data import social_media_data, generate_mock_onchain_data
from llm import llm

# prompt template for generating tweets
tweet_prompt = PromptTemplate(
    input_variables=["data", "social_media_data"],
    template="""
    Generate 5 viral cryptocurrency tweets based on this on-chain data and social media activity:
    On-chain data: {data}
    Social media mentions: {social_media_data}
    
    Use crypto slang, emojis, and start each tweet with a different emoji. Include hashtags, numbers and relevant influencers in the tweets. 
    You can also tweet about the trending tokens and their recent activities.

    Format:
    1. [Tweet 1]
    2. [Tweet 2]
    3. [Tweet 3]
    4. [Tweet 4]
    5. [Tweet 5]
    """
)

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt) 

def generate_tweets():
    onchain_data = generate_mock_onchain_data()
    
    formatted_data = "\n".join([f"{k}: {v}" for k, v in onchain_data.items()])
    
    # Format social media data
    social_media_mention_data = "\n".join([f"Token {k}: Mentions - {v['mentions']}, Influencers - {', '.join(v['influencers_following'])}" for k, v in social_media_data.items()])
    
    # Generate tweets using the model
    response = tweet_chain.run(data=formatted_data, social_media_data=social_media_mention_data)
    
    # Split response into individual tweets
    tweets = response.split('\n')
    tweet1 = tweets[0].replace('1. ', '').strip()
    tweet2 = tweets[1].replace('2. ', '').strip()
    tweet3 = tweets[2].replace('3. ', '').strip()
    tweet4 = tweets[3].replace('4. ', '').strip()
    tweet5 = tweets[4].replace('5. ', '').strip()

    # Return the tweets as JSON
    return {
        'tweet1': tweet1,
        'tweet2': tweet2,
        'tweet3': tweet3,
        'tweet4': tweet4,
        'tweet5': tweet5
    }
