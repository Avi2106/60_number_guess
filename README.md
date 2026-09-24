# Number Guessing Repair Lab

This project is an interactive number deduction game using **Pygame**. It introduces students to string-to-integer parsing safety, boundary and input sanitization, dynamic range feedback, and text-input UI widgets within an object-oriented codebase.
---

## What's Provided

A working Number Guessing game with:

- A secret number generated randomly between 1 and 100 on game initialization and resets
- A custom `TextBox` input component handling digit typing, backspace, and active selection states
- Interactive guess submission via the `Return` / `Enter` key or clicking the `SUBMIT` button
- Dynamic hint feedback (`TOO LOW!`, `TOO HIGH!`, or `CORRECT!`) along with an attempt counter
- Win state handling and restart capability via the `R` key

It has **one deliberate bug** and **three optional features** left as tasks to implement. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**
---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

**Controls:** Type digits into the text box and press Return (or click SUBMIT) to guess. Press R to start a new game after winning.


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the empty input crash bug

Submitting without typing any digits causes the game to crash immediately with a ValueError: invalid literal for int() with base 10: ''. In game_engine.submit_guess(), int(self.input_box.text) is called directly without verifying whether self.input_box.text contains any characters. Implement validation to check whether the input text is non-empty before converting it. If empty, prevent the conversion, preserve the attempt count, and update self.feedback_msg to prompt the player to enter a valid number first.

### Task 2: Implement dynamic range hints

Currently, the game only tells the player whether their guess was higher or lower than the target. Enhance game_engine to maintain low_bound (initialized to 1) and high_bound (initialized to 100). Update these bounds after each valid guess and display the refined range on the screen (e.g., "Current Possible Range: 24 - 68") to help the player narrow down their choices.

### Task 3: Implement an attempt history log

Players currently only see the total number of attempts. Implement a visual guess history panel below or beside the feedback box that lists the player's last 5 guesses along with colored arrows or tags indicating whether each past guess was too high or too low.

### Task 4: Implement maximum attempts limit and Game Over state

Right now, players have infinite attempts to guess the number. Add a maximum allowance (e.g., 7 attempts). If the player fails to guess the number within the limit, trigger a GAME_OVER screen revealing the secret number and prompt them to press R to try again
---

## Expected Behavior

- Typing numbers into the text box and pressing Return or clicking SUBMIT registers a guess.
- Submitting an empty input box displays a warning message without crashing the game.
- The game accurately indicates whether the guess is too high or too low, incrementing the attempt count each time.
- Guessing the exact number displays the victory message and unlocks the R key restart option.
---

## Folder Structure

```
number_guess/
├── game/
│   ├── game_engine.py
│   └── text_box.py
├── main.py
└── README.md
```

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
