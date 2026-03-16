import antigravity  # Easter egg!
import time
import random
import sys

def dizzy_stars(duration=3):
    """
    Shows a small ASCII 'dizzy' animation.
    """
    frames = [
        "   *   ",
        "  * *  ",
        " *   * ",
        "  * *  ",
        "   *   "
    ]
    print("\n[ Character is now dizzy... ]")
    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in frames:
            sys.stdout.write(f"\r{frame} (o_O) {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r       (@_@)       \n")

def cartoon_slap():
    """
    Prints a series of comic-style sound effects to simulate a cartoon slap.
    """
    effects = ["THAPP!", "POW!", "BONK!", "WHACK!", "SLAP!", "ZOT!", "KAPOW!"]
    random.shuffle(effects)
    
    print("\n[ Cartoon Action Sequence Begins ]")
    for sound in effects[:4]:
        time.sleep(0.4)
        print(f"*** {sound} ***")
    print("[ Dramatic Silence... ]")
    time.sleep(0.8)

def main():
    # Character names
    p1 = "Sairaj"
    p2 = "Mohit"
    
    print(f"--- A Sunny Day in Cartoon Land (Enhanced) ---")
    time.sleep(1)
    
    scenes = [
        (f"{p1}: Hey {p2}, did you see that giant anvil falling?", 
         f"{p2}: What anvil? I don't see—"),
        (f"{p1}: Is that a piano suspended by a single thread above you?", 
         f"{p2}: A piano? Let me check my schedule..."),
        (f"{p1}: Do you hear that whistling sound getting louder?", 
         f"{p2}: Whistling? It sounds like a falling safe...")
    ]
    
    line1, line2 = random.choice(scenes)
    
    print(line1)
    time.sleep(1.5)
    print(line2)
    time.sleep(1.2)
    
    print(f"{p1}: (Pointing) Look up! It's got your name on it!")
    time.sleep(1)
    
    print(f"{p2}: Oh, I see it now. It's quite shiny for a heavy object.")
    time.sleep(1)
    
    print(f"{p1}: Never mind the physics. I need to test this new slap-o-matic!")
    time.sleep(0.8)
    
    print(f"{p2}: Slap-o-matic? Is that—")
    time.sleep(0.4)
    
    print(f"{p1}: YES!")
    
    # The dramatic slap!
    cartoon_slap()
    
    # Dizzy animation
    dizzy_stars()
    
    print(f"{p2}: (Stumbling) I think I can see my house from here... and several planets.")
    time.sleep(1.5)
    
    print(f"{p1}: Success! The Slap-o-matic 3000 works perfectly.")
    time.sleep(1)
    
    print(f"{p2}: Can we test the 'free vacation' button next time?")
    print("\n--- End of Enhanced Simulation ---")

if __name__ == "__main__":
    main()
