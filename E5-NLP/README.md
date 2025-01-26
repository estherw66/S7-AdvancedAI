# NLP - Exercise

## Description
You should now have a basic theoretical understanding of the elements in an NLP pipeline. And you should have some practice with several tutorials treating these new topics and methods.

By cleverly:

chaining general (large) language models,
(fine-tuned) specialized models,
add vector databases,
define multiple agents
integrate tool usage,
...you can automate many complicated language rich tasks.

Your task:

Choose a task that a LLM cannot do out-of-the box
Design a system that performs this activity, using LLMs.
Demonstrate this activity (on a web-page or in a video)
The landscape of LLMs and frameworks to work with them is in constant flux. It is interesting for you and me, to find your own framework that fits your need. For instance with LangChain you can interface with many local, free (using e.g. ollama), and also paid API LLM models. You don't need an openAI key for this project (but if you have one, you can use it of course). But there are many other, newer, frameworks to work with.

 

### Deliverables

Describe clearly what problem you want to solve using a design challenge format:
Design a `form of solution` to enable `users` in `context` to `perform activity` with `target performance`.
Describe your design for solving it, e.g. an diagram on how you chain models, vector stores, plugins etc, together to solve your problem.
A link/HTML/PDF of your (colab) notebook or code files, make sure to document the code and explain your own steps.
If you deploy your (Streamlit) app link to the app, or create a short video of the working app.
 

### Complexity

The focus of this assignment is not about model accuracy, or quality of the output or functionality, though it is good to reflect on how you think the system performs.
We expect to see a prototype of a system that does more than simply call a prompted LLM. It is complex enough if you use an LLM in combination with vector databases, agents, and/or tool usage towards the predefined meaningful goal.

## Feedback:
Hello Esther, thanks for your submission. You use both a summarizer and a encoder-decoder translation model to work with text in a PDF. You've worked this into a working streamlit prototype. You've shown enough practical use with modern NLP pipelines. Nice job.