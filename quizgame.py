questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which language is used to build websites?",
            "options": ["A. HTML", "B. Python", "C. C++", "D. Java"],
            "answer": "A"
        },
        {
            "question": "Who wrote 'Harry Potter'?",
            "options": ["A. J.R.R. Tolkien", "B. J.K. Rowling", "C. Mark Twain", "D. Charles Dickens"],
            "answer": "B"
        }
]
score=0
for items in questions:
        print(items["question"])
        for options in items["options"]:
            print(options)
        print("type your answer")
        answer=input("A/B/C/D: ").upper()
        if answer==items["answer"]:
                print("correct answer!")
                score=score+1
        else:
            print(f"wrong!!!correct answer is {items["answer"]}")

