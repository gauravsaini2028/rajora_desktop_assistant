Week 1 Research: Existing AI Desktop Agents

1. Open Interpreter

Introduction:

Open Interpreter is an opensource AI assistant that allows a Large Language Model (LLM) to perform tasks directly on a our computer by generating and executing Python code. Unlike a normal chatbot that only provides answers or instructions, Open Interpreter can actually complete tasks such as organizing files, analyzing data, generating reports.

A simple way to understand it is to think of it as an AI programmer working on our computer. Instead of telling you how to solve a problem, it writes and executes code to solve it.

How It Works:

The workflow is simple:

* The user gives a command in natural language.
* The AI understands the task.
* It generates Python code.
* The code is executed on the local machine.
* The result is returned to the user.

For example, if we ask, "Rename all PDF files in my Downloads folder", Open Interpreter can generate the required Python code, execute it, and rename the files automatically.

Strengths:

* Can automate a wide variety of tasks using Python libraries.
* Saves time by performing work instead of only explaining it.
* Modular and easily extendable using existing Python packages.
* Often shows generated code before execution, making the process transparent.

Limitations:

* Executing AI generated code can be risky without proper confirmation.
* GUI interaction is limited compared to vision based desktop agents.
* Some generated code may behave differently across operating systems.

Relevance to our project:

Although Rajora AI focuses more on screen understanding and desktop automation than code execution, Open Interpreter provides valuable design ideas. It highlights the importance of modular architecture, transparency, and user confirmation before performing sensitive actions. These principles will help in making Rajora AI safer and easier to maintain.

Key Learning:

Open Interpreter shows that AI assistants should move beyond conversation and actually perform useful tasks, while ensuring safety and keeping users informed.

2. Claude Computer Use

Introduction:

Claude Computer Use is a capability developed by Anthropic that allows an AI model to control a computer like a human. Instead of generating Python code, it understands screenshots, identifies interface elements, and interacts with applications using mouse clicks and keyboard input.

It is one of the closest real world examples to the Rajora AI Desktop Assistant.

How It Works:

Claude follows a continuous cycle:

1. Capture the screen.
2. Understand what is visible.
3. Decide the next action.
4. Click, type, or scroll.
5. Capture the screen again and repeat.

For example, if we asked to search for AI internships, Claude can open a browser, navigate to a website, type the search query, and display the results without needing a dedicated API.

Strengths:

* Works with almost any desktop application.
* Uses computer vision to understand buttons, menus, forms, and dialogs.
* Can adapt if the interface changes or unexpected popups appear.

Limitations:

* Slower because every action requires another screenshot and reasoning step.
* Incorrect actions can affect later decisions.
* Requires confirmation before performing sensitive operations.

Relevance to our project:

Claude Computer Use is the biggest inspiration for our project. Our current prototype already captures screenshots and uses a vision model to understand the screen. In future weeks, Rajora AI will extend this by adding mouse, keyboard, browser, and file automation.

The most important idea we can adopt is the 'Observe - Think - Act' cycle, where the AI verifies each action before moving to the next step.

Key Learning:

Claude Computer Use demonstrates that AI can automate desktop applications by understanding graphical interfaces rather than relying only on APIs. It also highlights the importance of continuous observation, user control, and safe execution.

Conclusion:

Both Open Interpreter and Claude Computer Use represent different approaches to AI powered computer automation. Open Interpreter focuses on solving problems through Python code execution, while Claude Computer Use relies on computer vision and desktop interaction.

Rajora AI Desktop Assistant will combine ideas from both systems. It will use vision(already into implementation) to understand the screen, plans actions intelligently, and will later automate desktop tasks while maintaining transparency, safety, and user control.
