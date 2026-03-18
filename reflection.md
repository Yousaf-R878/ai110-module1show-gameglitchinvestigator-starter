# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The first time I ran the game it looked like a typical number guesser. The game consists of 3 difficulties: easy, medium, and hard, each giving you less a different number of guesses and number range in order to guess the right number. The game also allows you to get hints telling you if the secret, aka the number to guess, is higher or lower than your current guess. The game also allows you to restart the game whenever you'd like.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  Bugs:(even attempts)
    - Number of attempts left is 1 yet the game says it is over
    - You can change the difficulty yet the range doesnt change for the game text 
      (ie. the games text always shows "Guess a number between 1 and 100. Attempts left: 6")
    - dispite different number ranges, the secret can be outside of said ranges 
      (ie. the range could be 1-50 with a secret of 75)
    - Attempts left seems to be 1 less than attempts allowed whenever refreshing the page, however this isnt the case whenever hitting the New Game button
    - When the game ends, either from winning or losing, the New Game button gives a new secret, refreshes the attempts but you're not able to actually submit attempts
    - The hints tell you to go higher when you should go lower and vice versa
    - In the developer debug info, the history list only starts updating aftet the second guess (ie. if you guess 80, it wont show up right away, but if you guess 90, 80 will show up, then after the next guess 90, and so on)



2 Bugs to fix: 
 - You can change the difficulty yet the range doesnt change for the game text (ie. the games text always shows "Guess a number between 1 and 100. Attempts left: 6")
 - dispite different number ranges, the secret can be outside of said ranges (ie. the range could be 1-50 with a secret of 75)
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I explained to the AI that the text would not show the right range for the difficulty. As a result, it explained that ranges had been hardcoded into the text, and that swapping the numbers for the 'low' and 'high' variables which we recieve from the "get_range_for_difficulty" function. Thus this fixed the issue

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I explained to the AI that there was an issue with the secret being out of range for the respective difficulty ranges (ie. you could have a secret of 99 when the specified range is 1-20). The fix that the AI suggested was editing 'random.randint(1, 100)' to 'random.randint(low, high)' which would essentially make it so that it takes into account low and high for the difficulty when creating a new secret. 
    
This solution however, is misleading because it doesn't fully address the issue. The same issue persists if I just switch the difficulty of the game without clicking "New Game." This fix only fixed the problem by setting the right secret when "New Game" was pressed. 
    
I explained this issue to the AI and it said that the issue stemmed from a different part of the code which only generates a new secret if one doesn't already exist in the session state. This means that the secret persists for the entire session and is never regenerated on difficulty change. 
    
Explaining this to the agent, it decided to store the active difficulty in the session state and regenerate the secret whenever it changes. 

In order to verify the fix worked, I had the agent create a test and I also tried to generate the same scenario which led me to this issue(the old secret being out of range of the new difficulty). However, the secret changed every time the difficulty changed and was always within range.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided when a bug was really fixed when
  - it would pass my pytests
  - i wasnt able to recreate the bug in the running app, even with edge case scenarios
  - the logic for the fix within the code made sense as for why it fixed the bug.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a manual test for the scenario when the scecret was out of the range for a difficulty. For each difficulty, I checked if the scecret was in range after starting a new game, and that verified that the bug was fixed. However, I noticed that the scecret could be out of range when switching between difficulties, which led to the second bug fix. It showed me how the secret was actually handled and helped me learn about streamlit's state handling.

- Did AI help you design or understand any tests? How?

AI did help me understand tests that it was creating. For the secret being out of range scenario, I had it generate test cases for the second bug but also had it describe what the test actually did so that I could verify that the test was functional. I also intentially threw a bug into the test to verify its functionality, and tested it against the old logic. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The original app would only generate if one didn't already exist in the session state or if a new game was ran using the "New Game" button

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?'

Session state is just a way to make data not disappear. For example, using streamlit is like using a whiteboard where whenever you interact with the whiteboard, it gets erased and redrawn. State is like a piece of paper that doesnt get erased whenever the board does. This allows data to persist on your application. 

A rerun is you manually telling the board to be erased and redrawn. Its good to be used when you want a state change to be reflected immediately.

- What change did you make that finally gave the game a stable secret number?

I made sure that when a secret was generated, it would be based off of the range of the difficulty. Additionally, I made it so that a secret was also regenerated whenever the difficulty was changed.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I want to keep using Claude's planning feature which helps me see extactly what it plans on doing, allowing me to catch bugs or issues before code is even written.

- What is one thing you would do differently next time you work with AI on a coding task?

I would ask AI more questions to see if the code it generated truly fixes the bug I was targeting.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project helped me see that AI generated code isn't always the most reliable, and that it's up to you as a developer to ensure that AI generates fully functional and robust code.
