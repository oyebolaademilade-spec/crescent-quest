print("--- WELCOME TO THE ULTIMATE CRESCENT QUEST ---")
name = input("Enter your hacker name: ")
score = 0

print(f"\nWelcome {name}! Your goal is to make the right choices and score 30 points.")

# Round 1
print("\n[ROUND 1] You want to build an app for Hack Club Crescent.")
choice1 = input("Do you (1) Code it on your phone or (2) Skip it to watch TV? (Type 1 or 2): ")
if choice1 == "1":
    print("Great choice! You learned how to use GitHub Mobile.")
    score += 10
else:
    print("You missed the deadline.")

# Round 2
print("\n[ROUND 2] Your code has a bug and the server gives a 503 error.")
choice2 = input("Do you (1) Give up or (2) Refresh and check the code? (Type 1 or 2): ")
if choice2 == "2":
    print("Awesome! The server came back online.")
    score += 10
else:
    print("You lost motivation.")

# Round 3
print("\n[ROUND 3] The checklist asks for a terminal screenshot.")
choice3 = input("Do you (1) Upload an online compiler screenshot or (2) Close the tab? (Type 1 or 2): ")
if choice3 == "1":
    print("Perfect! The automated scanner approved your image.")
    score += 10
else:
    print("Project left incomplete.")

# Endings
print(f"\n--- GAME OVER, {name.upper()} ---")
print(f"Your Final Score: {score}/30 points")

if score == 30:
    print("🏆 PERFECT ENDING: You are a dedicated mobile hacker! Next stop: MacBook Neo!")
elif score > 0:
    print("👍 GOOD ENDING: You made it through, but missed a few points. Keep practicing!")
else:
    print("💀 BAD ENDING: You didn't ship anything today. Try again tomorrow!")

