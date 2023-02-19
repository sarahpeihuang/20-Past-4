import cohere
from cohere.classify import Example
co = cohere.Client('yhlIG1WYyeUVrAJ2NzhQwYKnghq6sbs8DfWCPulm') # This is your trial API key

def printClass(msg):
  response = co.classify(
  model='large',
  inputs=[msg],
  examples=[Example("Ummm, I don't know.", "Negative"), Example("Maybe next time.", "Negative"), Example("Yeah, sure.", "Negative"), Example("I think, maybe not.", "Negative"), Example("Sounds good.", "Negative"), Example("I want to but I'm scared", "Negative"), Example("Yes, of course.", "Negative"), Example("Should I?", "Negative"), Example("Is your friend joining?", "Negative"), Example("Do you want me to?", "Negative"), Example("How about no?", "Negative"), Example("No, thank you.", "Positive"), Example("I don't smoke.\n", "Positive"), Example("I'm good, thanks.\n", "Positive"), Example("It's just not for me.", "Positive"), Example("I don't want to.\n", "Positive"), Example("I don't smoke weed.\n", "Positive"), Example("I'm not into it.\n", "Positive"), Example("I have to pass.\n", "Positive"), Example("I'm good, I'll just stick with water.\n", "Positive"), Example("I don't want to risk it.\n", "Positive"), Example("I'm good, I'll just watch.\n", "Positive"), Example("I'm not interested.\n", "Positive"), Example("I'm allergic to it.\n", "Positive"), Example("I prefer to stay sober.\n", "Positive"), Example("I have to focus on something important later.\n", "Positive")])
  print("hi")
  return response.classifications[0].prediction
