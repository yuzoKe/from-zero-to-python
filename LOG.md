# 📓 From Zero to Python — Learning Journal
This is my personal record of daily learning. Each day includes a short summary of what I worked on, what I learned, and what I plan to improve. Mistakes included. Growth guaranteed.

---

# 📘 Dev Log - Day 1 — Task Manager (Lists, Input/Output)
📅 Date: 27/06/2025
📁 Project: days/day01_task_manager/task_manager.py

## 📌 Focus:
* Learn basic list operations
* Use input() to interact with the user
* Practice loops with for and enumerate()
* Implement simple conditionals with if and else

## 🔍 What I learned:
* How to create and update lists in Python using .append() and .pop()
* How to loop over elements with indexes using enumerate()
* How to safely remove an item from a list by validating the index
* That input() always returns a string — so converting to int is essential when working with numbers
* The use of \n to jump a line

## ⚠️ Challenges:
Understanding zero-based indexing and how to adjust it when displaying options to users

## 🧠 Reflections:
This was my first real Python script and it felt great to see a working CLI program. It's simple, but functional. I already started thinking about making it "tangible" and saving data to a file.

---

# 📘 Dev Log - Day 2 — GUI Task Manager (First time with Tkinter!)
📅 Date: 29/06/2025
📁 Project: days/day02_gui_task_manager/

## 📌 What I tried to do:
* Make a visual version of yesterday's task manager
* Learn about windows and buttons (Tkinter)
* Figure out how to save tasks so they don't disappear

## 🔍 What I actually learned:
* Classes are confusing but useful: Still don't fully get self but I see it organizes code better
* Tkinter basics: Made a window with buttons! Took forever to figure out pack()
* Saving data: Used JSON - basically a text file that looks like Python dictionaries
* Buttons do things: Connecting command=function_name was magical when it worked

## 😅 Honest struggles:
* Spent 2 hours trying to understand why my button wasn't working
* Classes vs functions - still mixing them up
* Error messages everywhere until I added try/except (copied from examples)
* The code is mostly working but I don't understand every single line

## 🎉 Cool things that worked:
* You can actually check off tasks!
* Tasks keep saved when you close the program (mind blown)
* Delete button works (with confirmation so I don't delete by accident)
* Changed colors to make it look less ugly

## 🤔 Things I copy-pasted and need to understand better:
* The scrollbar part (it works but... how?)
* Lambda functions - used them but still googling what they do
* Some of the layout code
* Error handling - I know it's important but added it blindly

## 🧠 Honest reflection:
This feels like a huge jump from yesterday! The GUI actually looks like a real program. Got help from AI/tutorials for the complex parts, but I typed every line and tested everything. Still have no idea how some parts work, but how I said, I believe in learning by doing.
The best part: when I showed it to my family, they said "wow, you made that?!", felt good.

## 🎯 Tomorrow I want to:
* Actually understand what self means
* Add simple features without copying code
* Try colors or fonts
* Read more about classes

---

# 📘 Dev Log — Day 03

## 💻 What I did today

Today I had to step out of my regular Python learning routine to solve a real-world task for my store.

I built a **complete loyalty system in VBA** for Excel to automatically manage loyalty discounts based on the number of cuticle nippers customers bring in. Until now, this was done manually with physical cards. Now the system:

- **Applies a R$10 discount for every 12 nippers** automatically.
- Carries over any extra nippers as balance toward the next discount.
- Identifies the customer by phone number and **updates or creates records instantly**.
- Automatically **logs every interaction in a historical sheet**, with no need for prior registration.

## ⚙️ Why it matters

Even though I didn’t write Python today, this was still a **big step in becoming a better developer**.

I had to:
- Create a custom data structure (`Type`) in VBA.
- Write logic to calculate balances and conditional discounts.
- Automate worksheet searches and dynamic data updates.
- Think about UX and how it fits into the real workflow of my team.

All of these are key developer skills — even if the syntax wasn’t Python, the mindset was.

## 🧠 Reflection

Today reminded me that **being a programmer is not about the language — it's about solving problems**. Whether it’s Python, VBA, or anything else, coding becomes real when it’s used to help someone or automate something that matters.

---

# 📄 Day 4 – Azure Document Intelligence (Prebuilt Receipts)

Today I explored a new topic outside of core Python:  
I used Azure AI Document Intelligence Studio to analyze and extract data from receipt images.

## 🔍 What I did:
- Created a new Azure Document Intelligence resource.
- Uploaded a sample receipt image.
- Used a prebuilt model to extract merchant name, date, items, and total.
- Generated Python code to parse receipt data.

## 📦 Technologies:
- Azure Document Intelligence SDK (prebuilt model)
- Python 3.8+
- OCR and key-value extraction

## 📁 Output:
The model parsed structured data from a scanned receipt image and returned fields with confidence scores.

## 📝 Notes:
This exercise is based on the official Microsoft Learn path:  
[Quickstart: Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api)
