print("--- WELCOME TO CRESCENT QUEST ---")
name = input("Enter your hacker name: ")
print(f"Welcome {name}! Your mission is to earn 9,300 stars for a MacBook Neo.")

print("\nYou open your phone and find Hack Club Crescent.")
choice = input("Do you want to (1) Spend 1 hour coding or (2) Go watch TikTok? Type 1 or 2: ")

if choice == "1":
    print("\n[SUCCESS] You wrote a Python game entirely on your phone!")
    print("You earned your very first project stars. Keep shipping! 🚀")
elif choice == "2":
    print("\n[GAME OVER] You got stuck scrolling for 4 hours. No stars earned today!")
else:
    print("\n[ERROR] The system glitched out. Run the script and try again!")
