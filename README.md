# 🎮 Week 3, Lesson 2: Build Pong with GitHub Copilot in Agent Mode

## 💻 Step 1: Choose How to Run Your Game

You have two options for running your game. We encourage you to try the local setup for a smoother experience, but you can continue in the browser if you prefer.

### 🖥️ Option 1: Run Locally with VS Code

Want to build a more advanced game on your own computer? Working locally gives you faster performance and full control — a great option for your coding challenge project!
👉 Follow our [📋 Local Setup Guide](local-setup.md) to get started on Windows.

### 🌐 Option 2: Run in the Browser with GitHub Codespaces

If you don't want to set things up locally, you can continue using **GitHub Codespaces** in your browser — just like in previous lessons.

> 💡 *If you're using GitHub Codespaces, you need to add the following lines at the top of your file to enable graphics display in the browser:*

```python
# Only needed if you're running in GitHub Codespaces
import os
os.environ["DISPLAY"] = ":1"
```

---

## 🧠 How This Lesson Works

In this lesson, you’ll build and continuously improve a version of **Pong** using **GitHub Copilot’s chat-based agent** in VS Code.

### To Use GitHub Copilot Chat Agent:

1. Open your project in VS Code
2. Open the Copilot Chat pane (use the sidebar icon or press `Ctrl + '`)
3. Use plain English to describe what you want to build or change
4. Copilot will suggest code or updates directly in your file

You can also right-click inside your file and choose **"Ask Copilot"** to ask questions about your code or request edits.

---

## 🏓 Step 1: Generate a Basic Pong Game

Ask Copilot in the chat:

> **“Create a basic Pong game in Python with Pygame. Include two paddles, a bouncing ball, and keyboard controls for each player.”**

✅ Run the file and confirm it works. You should see a functional Pong game window.

---

## 🛠️ Improve Your Pong Game with Copilot Agent

### 🎨 Step 2: Add Colors and Style

Ask Copilot:

> “Add background color and set different colors for paddles and ball.”

---

### 🧠 Step 3: Add Scoring System

Ask Copilot:

> “Add scoring to the Pong game and display each player’s score on the screen.”

---

### 🧲 Step 4: Make the Ball Faster

Ask Copilot:

> “Increase ball speed slightly every time it hits a paddle.”

---

### ⏱️ Step 5: Add a Countdown Before Start

Ask Copilot:

> “Add a 3-second countdown before the game starts and show it on screen.”

---

### 🖱️ Step 6: Add Menu or Restart Button

Ask Copilot:

> “Create a start screen with a ‘Play’ button and allow the player to restart the game after it ends.”

---

### 🔊 Step 7: Add Sound Effects

> **Note:** Sound effects will only work if you are running VS Code locally. They do not work in GitHub Codespaces.

Ask Copilot:

> “Play a sound when the ball hits a paddle or when someone scores.”

---

## ▶️ Run Your Game

### Option 1: Use the Run Button

* Open `app.py`
* Click the green **Run** button in the top-right of VS Code

### Option 2: Use the Terminal

```bash
cd lesson-2
python app.py
```

---

## 🎮 Want to Build Something Else?

Once you've mastered Pong, try making a new game from scratch with Copilot!
Here are some fun ideas to get you started:

### 🦘 Platformer

Ask Copilot:

> “Create a basic 2D platformer game with a character that can jump and land on platforms.”

Bonus:

* Add enemies, coins, or a scrolling background
* Try levels with increasing difficulty

### 🚗 Racing Game

Ask Copilot:

> “Create a simple top-down racing game where the player avoids obstacles and tracks time.”

### 🐍 Snake Game

Ask Copilot:

> “Make a classic Snake game that grows longer when it eats food.”

### 🎯 Target Clicker

Ask Copilot:

> “Build a clicker game where a target randomly appears and you score by clicking it quickly.”

---

### 💭 Things to Think About

* How could you make this game **two-player**?
* Could you use **images** from your last lesson with Bing Create for your characters or backgrounds?
* How would you create **levels or a win condition**?
* Can you design a game that keeps people coming back — with a high score, unlocks, or fun surprises?

> 🧪 Tip: Challenge yourself to invent your own twist on one of these classics. Copilot can help with every step!
