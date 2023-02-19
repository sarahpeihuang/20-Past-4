import cohere
from cohere.classify import Example
co = cohere.Client('yhlIG1WYyeUVrAJ2NzhQwYKnghq6sbs8DfWCPulm') # This is your trial API key

def washroomResponse(msg):
  response = co.classify(
  model='large',
  inputs=[msg],
  examples=[Example("Ummm, I don't know.", "Negative"), Example("Maybe next time.", "Negative"), 
            Example("Yeah, sure.", "Negative"), Example("I think, maybe not.", "Negative"), 
            Example("Sounds good.", "Negative"), Example("I want to but I'm scared", "Negative"), 
            Example("Yes, of course.", "Negative"), Example("Should I?", "Negative"), 
            Example("Is your friend joining?", "Negative"), Example("Do you want me to?", "Negative"), 
            Example("How about no?", "Negative"), Example("No, thank you.", "Positive"), 
            Example("I don't smoke.\n", "Positive"), Example("I'm good, thanks.\n", "Positive"), 
            Example("It's just not for me.", "Positive"), Example("I don't want to.\n", "Positive"), 
            Example("I don't smoke weed.\n", "Positive"), Example("I'm not into it.\n", "Positive"), 
            Example("I have to pass.\n", "Positive"), Example("I'm good, I'll just stick with water.\n", "Positive"), 
            Example("I don't want to risk it.\n", "Positive"), Example("I'm good, I'll just watch.\n", "Positive"), 
            Example("I'm not interested.\n", "Positive"), Example("I'm allergic to it.\n", "Positive"), 
            Example("I prefer to stay sober.\n", "Positive"), Example("I love weed.\n", "Negative"), 
            Example("I have to focus on something important later.\n", "Positive")])
  print(response.classifications[0].prediction)
  return response.classifications[0].prediction

def partyResponse(msg): 
  response = co.classify(
  model='large',
  inputs=[msg],
  examples=[Example("Yes, let's continue smoking, even though the air is polluted.", "Negative"), Example("It's a good idea for us to stay inside in this polluted air.", "Negative"), 
            Example("Sure, It smells so good.", "Negative"), Example("I'm hesitant to go outside for fresh air, but if you stay, I'll stay.", "Negative"), 
            Example("I'll only go outside for fresh air if you go.", "Negative"), Example("This is so cool, let's stay.", "Negative"), 
            Example("We don't have to protect ourselves from this polluted air.", "Negative"), Example("I don't care about our exposure to the pollution by staying indoors.", "Negative"), 
            Example("No, the air is too dense and I don't enjoy this. ", "Positive"), Example("It smells really bad.", "Positive"), Example("I can't breathe.", "Positive"), 
            Example("This is polluting the air, we shouldn't be breathing this.", "Positive"), Example("I need some fresh air.", "Positive"), Example("There is ", "Positive"), 
            Example("Let's go outside.", "Positive"), Example("The air is contaminated and it's not safe for us to inhale.", "Positive"), 
            Example("The air quality is being compromised.", "Positive"), Example("It's unacceptable that the air we breathe is being polluted like this.", "Positive"), 
            Example("The air is being polluted with harmful substances.", "Positive"), Example("The air we're inhaling is toxic.", "Positive"), 
            Example("This level of air pollution is dangerous.", "Positive"), Example("I am conflicted because I want to stay at the party but it smells bad. I think I will leave for a bit.", "Positive"), 
            Example("I want to stay at the party because I don't want to leave and feel left out. The smoke is bad but I will stay.", "Negative"),
            Example("sure.", "Negative"),Example("not at all!", "Positive")])
  print(response.classifications[0].prediction)
  return response.classifications[0].prediction


def classroomResponse(msg):
  response = co.classify(
  model='large',
  inputs=[msg],
  examples=[Example("There are no consequences to smoking marijuana.", "Negative"), Example("Marijuana is good for you.", "Negative"), 
            Example("There are none, it will make you feel happy.", "Negative"), Example("There are none, it makes me look cool.", "Negative"), 
            Example("There are none, it makes me feel like I fit in.", "Negative"), 
            Example("Respiratory problems: Smoking marijuana can cause inflammation and irritation of the lungs, leading to coughing, wheezing, and bronchitis.\n\n\n", "Positive"), 
            Example("Cardiovascular effects: Marijuana smoke can increase heart rate and blood pressure, which can be harmful for people with existing heart problems.\n\n", "Positive"), 
            Example("Cognitive impairment: Regular marijuana use can impair memory, attention, and learning ability, especially in young people.\n\n", "Positive"), 
            Example("Mental health: Marijuana use has been associated with an increased risk of anxiety, depression, and psychosis, especially in people who have a history of mental health problems.\n\n", "Positive"), 
            Example("Impaired driving: Marijuana use can impair judgment, coordination, and reaction time, which can lead to accidents while driving.\n\n", "Positive"), 
            Example("Addiction: Long-term use of marijuana can lead to addiction, with withdrawal symptoms including irritability, insomnia, and loss of appetite.\n\n", "Positive"), 
            Example("Fetal development: Marijuana use during pregnancy can harm fetal development, leading to low birth weight and cognitive and behavioral problems in children.\n\n", "Positive"), 
            Example("smoking marijuana is bad for the lungs but people like to do it because it makes them look cool", "Positive"), 
            Example("marijuana actually improves mental and physical health", "Negative"),])
  print(response.classifications[0].prediction)
  return (response.classifications[0].prediction)
