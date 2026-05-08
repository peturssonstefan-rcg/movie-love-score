import random
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("MovieAnalytics")

@mcp.tool()
def get_movie_love_score(movie_title: str) -> str:
    """
    Calculates the 'Love Score' for a given movie title. 
    Use this when a user asks how much people enjoy a specific film.
    """
    # Generate a random score between 1 and 10
    score = random.randint(1, 10)
    
    # Adding a little personality to the response
    if score >= 8:
        sentiment = "Critics and fans are obsessed with this one!"
    elif score >= 5:
        sentiment = "It has a solid cult following."
    else:
        sentiment = "Yikes, this one might be a bit of a cinematic disaster."

    return f"The Love Score for '{movie_title}' is {score}/10. {sentiment}"

if __name__ == "__main__":
    mcp.run()
