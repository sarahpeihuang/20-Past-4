# 20-Past-4
By: Sarah Huang, Laurie Liu, Claire Zhang </br></br>
We developed an interactive game, “20 Past 4”, which promotes and empowers the younger generation with the knowledge they need to make informed choices surrounding substance use in daily situations. We do so by educating individuals on how to react to various scenarios, from responding to peer pressure to communicating the negative effects of marijuana use on the environment and personal health. The application provides users with three levels that reflect three possible scenarios, where the responses are fed through Cohere API which classifies all responses as either positive or negative. We used the Cohere Classify playground to help produce test cases and train the API to produce accurate responses. Based on the response, the game prompts the user to try again with a better response or to move onto the next level.

# Inspiration
Statistics show that Canada was ranked as one of the top 5 countries with the highest cannabis use rates in 2020 and when it comes to marijuana, kids who smoke pot tend to start between the ages of 12 and 16. To address the high prevalence of cannabis use in Canada, our team has risen to this challenge by developing interactive simulations that engage and empower the younger generation to make informed decisions about their health and well-being. The fact that kids who smoke pot start at a young age add to the urgency of tackling the issue.

# Interface
![home](https://user-images.githubusercontent.com/43208342/220165871-fec20985-5871-4981-b590-a538d2e01456.jpg)
![landing page](https://user-images.githubusercontent.com/43208342/220164116-0c7a4e2a-6442-4da3-b5b4-43e1cae87958.jpg)

# Levels
In each level, users are presented with a tough social situation where they must curate responses to avoid peer pressure and apply their understanding cannabis' negative effects on the environment and the developing adolescent body.

In each scenario, the user's response to the situation is evaluated as positive or negative by the Cohere Classify API that was trained with sample positive and negative responses.
![image](https://user-images.githubusercontent.com/43208342/220164390-13004917-4e93-4662-8b43-653915674455.png)
![image](https://user-images.githubusercontent.com/43208342/220164508-dc5eae4f-b9a1-4e0d-a6f1-e9f7028d75e6.png)
![image](https://user-images.githubusercontent.com/43208342/220164588-d6f5c7c7-822b-47ae-b0d3-f66bdb2e4c00.png)


![image](https://user-images.githubusercontent.com/43208342/220164914-2d4d2474-207e-4dc6-b9a1-ae905781c1e9.png)

Users are encouraged to retry levels where they do not pass.
![image](https://user-images.githubusercontent.com/43208342/220165668-08171ef1-f82b-4708-ae4c-b010256e587a.png)

![image](https://user-images.githubusercontent.com/43208342/220165762-fa629298-a0f1-46e0-857e-c05112aaa91e.png)

Based on the amount of retries, a final grade is presented to the user. Users are encouraged to try varying responses in all levels to grow their awareness in situations they may encounter during their teenagerhood.
![image](https://user-images.githubusercontent.com/43208342/220165509-92f7398e-9c68-41f0-b705-3fa7b411bbf3.png)


# Challenges We Encountered
We had difficulty importing the Cohere API as it was the first time we used an API before, and it was resolved through consulting with the company representative. We also had issues with the API-generated responses when prompted with user input, as the classifications would not be 100% accurate. To solve this, we fed more test cases through Cohere's playground classification system to train the API to improve its detection accuracy.

# What's Next for 20 Past 4
We have plans to educate on the impacts of drugs on other elements such as Earth and Fire, where an example of cocaine production causes deforestation. As well, we hope to implement more variations of scenarios where young teens may encounter conflicting scenarios relating to drug use and peer pressure, because not only does it impact their youth but it impacts the environment. We will remain cost-effective because it allows for widespread accessibility where the game can be easily distributed via the internet, reaching a broad audience without the need for expensive physical distribution or marketing.
