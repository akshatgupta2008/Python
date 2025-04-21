import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Quiz App")
        self.master.geometry("500x400")
        self.score = 0
        self.lives = 3
        self.current_q_index = 0

        self.questions = {1: 'What is the chemical symbol for gold?', 2: 'Which planet is known as the Red Planet?', 3: 'What is the capital of Australia?', 4: 'Which language is used for web apps?', 5: 'What is the square root of 64?', 6: "Who wrote 'Romeo and Juliet'?", 7: 'What is the largest ocean on Earth?', 8: 'Which country hosted the 2021 Olympics?', 9: 'What is the boiling point of water in Celsius?', 10: 'What does CPU stand for?', 11: 'Which gas do plants absorb from the atmosphere?', 12: 'What is the longest river in the world?', 13: 'Who painted the Mona Lisa?', 14: 'What is the largest planet in our solar system?', 15: 'Which organ purifies blood in the human body?', 16: 'In which year did World War II end?', 17: 'What is the hardest natural substance on Earth?', 18: 'Which country is known as the Land of the Rising Sun?', 19: 'How many continents are there on Earth?', 20: 'Who invented the telephone?', 21: 'What is the currency of Japan?', 22: "Which element has the chemical symbol 'O'?", 23: 'What is the smallest prime number?', 24: 'What is the capital city of Canada?', 25: 'What is H2O more commonly known as?', 26: 'How many players are there in a football team on the field?', 27: 'Which language has the most native speakers?', 28: 'What is the name of the galaxy we live in?', 29: 'Who discovered penicillin?', 30: 'What is the chemical formula for table salt?', 31: 'Which continent is the Sahara Desert located in?', 32: 'What is the speed of light?', 33: 'What color is chlorophyll?', 34: 'Which is the largest mammal?', 35: 'Who is known as the father of computers?', 36: 'Which is the most populated country?', 37: 'Which gas is essential for us to breathe?', 38: 'What is the main ingredient in bread?', 39: 'What is the main language spoken in Brazil?', 40: 'What is the freezing point of water?', 41: 'Which month has 28 or 29 days?', 42: 'Which part of the plant conducts photosynthesis?', 43: 'Which instrument measures temperature?', 44: 'What is 7 x 8?', 45: 'What is the capital of France?', 46: 'What is the powerhouse of the cell?', 47: 'How many legs does a spider have?', 48: 'What does WWW stand for?', 49: 'What is 100 divided by 5?', 50: 'Who is the CEO of Tesla?', 51: 'Which planet has rings?', 52: 'What is the capital of Germany?', 53: 'How many bones are in the human body?', 54: 'Which programming language is known for its snake logo?', 55: 'What is the color of the sun?', 56: 'Which vitamin is produced when sunlight hits the skin?', 57: 'Which animal is known as the ship of the desert?', 58: 'What does ATM stand for?', 59: 'How many hours are there in a day?', 60: 'Which organ helps in breathing?', 61: 'What is the capital of the USA?', 62: 'Which country has the Taj Mahal?', 63: 'Which fruit keeps the doctor away?', 64: 'Which planet is closest to the sun?', 65: 'Which festival is known as the festival of lights?', 66: 'Which color symbolizes peace?', 67: 'What is the value of pi up to 2 decimal places?', 68: 'Which insect produces honey?', 69: 'What is the first element on the periodic table?', 70: 'How many colors are there in a rainbow?', 71: 'Which country is famous for pizza?', 72: 'What does NASA stand for?', 73: 'What is the national flower of India?', 74: 'Which animal is known as the king of the jungle?', 75: 'How many seconds are in a minute?', 76: 'What is the capital of Italy?', 77: 'Which bird can mimic human speech?', 78: 'What is a polygon with 6 sides called?', 79: 'What is the main source of energy for the Earth?', 80: 'Which continent has the most countries?', 81: "Which gas makes up most of the Earth's atmosphere?", 82: 'What is the color of an emerald?', 83: 'What is the capital of Russia?', 84: 'What do bees collect from flowers?', 85: 'What is the biggest island in the world?', 86: 'Which sense is associated with the nose?', 87: 'What is the currency of the United Kingdom?', 88: 'What do you call molten rock after it has erupted?', 89: 'How many letters are there in the English alphabet?', 90: 'Which planet is known for its Great Red Spot?', 91: 'Which festival is celebrated on December 25?', 92: 'How many digits are there in binary language?', 93: 'What is a young cat called?', 94: 'What is the symbol for iron in the periodic table?', 95: 'Which famous scientist developed the theory of relativity?', 96: 'What is the name of the tallest mountain in the world?', 97: 'What is the largest organ of the human body?', 98: 'Which planet is known as the Earth’s twin?', 99: 'Which unit is used to measure electric current?', 100: 'Which company created the iPhone?'}

        self.options = {1: ["A. Pb", "B. Au", "C. Zn", "D. Fe"],
    2: ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"],
    3: ["A. Canberra", "B. Toronto", "C. Mexico", "D. Beijing"],
    4: ["A. Python", "B. HTML", "C. Java", "D. C++"],
    5: ["A. 6", "B. 7", "C. 8", "D. 9"],
    6: ["A. J.K. Rowling", "B. Shakespeare", "C. Dickens", "D. Tolkien"],
    7: ["A. Indian", "B. Arctic", "C. Atlantic", "D. Pacific"],
    8: ["A. China", "B. Japan", "C. Brazil", "D. USA"],
    9: ["A. 50", "B. 90", "C. 100", "D. 110"],
    10: ["A. Central Processing Unit", "B. Computer Processor Unit", "C. Core Processor Unit", "D. Central Power Unit"],
    11: ["A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"],
    12: ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
    13: ["A. Van Gogh", "B. Da Vinci", "C. Picasso", "D. Rembrandt"],
    14: ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
    15: ["A. Liver", "B. Heart", "C. Lungs", "D. Kidney"],
    16: ["A. 1940", "B. 1945", "C. 1950", "D. 1939"],
    17: ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
    18: ["A. China", "B. Japan", "C. Korea", "D. Thailand"],
    19: ["A. 5", "B. 6", "C. 7", "D. 8"],
    20: ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Isaac Newton"],
    21: ["A. Yuan", "B. Dollar", "C. Yen", "D. Won"],
    22: ["A. Hydrogen", "B. Oxygen", "C. Ozone", "D. Helium"],
    23: ["A. 0", "B. 1", "C. 2", "D. 3"],
    24: ["A. Ottawa", "B. Toronto", "C. Vancouver", "D. Montreal"],
    25: ["A. Salt", "B. Ice", "C. Water", "D. Air"],
    26: ["A. 9", "B. 10", "C. 11", "D. 12"],
    27: ["A. English", "B. Mandarin", "C. Hindi", "D. Spanish"],
    28: ["A. Andromeda", "B. Milky Way", "C. Sombrero", "D. Whirlpool"],
    29: ["A. Louis Pasteur", "B. Isaac Newton", "C. Alexander Fleming", "D. Marie Curie"],
    30: ["A. HCl", "B. NaCl", "C. KCl", "D. CaCl2"],
    31: ["A. Asia", "B. South America", "C. Africa", "D. Australia"],
    32: ["A. 3x10^8 m/s", "B. 3x10^6 m/s", "C. 1.5x10^8 m/s", "D. 300 m/s"],
    33: ["A. Red", "B. Blue", "C. Green", "D. Yellow"],
    34: ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Orca"],
    35: ["A. Charles Babbage", "B. Bill Gates", "C. Steve Jobs", "D. Alan Turing"],
    36: ["A. USA", "B. China", "C. India", "D. Russia"],
    37: ["A. Nitrogen", "B. Oxygen", "C. Helium", "D. Hydrogen"],
    38: ["A. Rice", "B. Milk", "C. Wheat", "D. Corn"],
    39: ["A. Spanish", "B. English", "C. Portuguese", "D. French"],
    40: ["A. 0°C", "B. 32°C", "C. 100°C", "D. -1°C"],
    41: ["A. February", "B. March", "C. January", "D. June"],
    42: ["A. Stem", "B. Root", "C. Leaf", "D. Flower"],
    43: ["A. Barometer", "B. Thermometer", "C. Altimeter", "D. Speedometer"],
    44: ["A. 54", "B. 56", "C. 64", "D. 49"],
    45: ["A. Berlin", "B. Rome", "C. Madrid", "D. Paris"],
    46: ["A. Nucleus", "B. Chloroplast", "C. Mitochondria", "D. Ribosome"],
    47: ["A. 6", "B. 8", "C. 10", "D. 12"],
    48: ["A. World Wide Web", "B. Web Wide World", "C. Wide Web World", "D. World Web Wide"],
    49: ["A. 15", "B. 20", "C. 25", "D. 30"],
    50: ["A. Jeff Bezos", "B. Elon Musk", "C. Tim Cook", "D. Mark Zuckerberg"],
    51: ["A. Mars", "B. Saturn", "C. Jupiter", "D. Neptune"],
    52: ["A. Berlin", "B. Munich", "C. Hamburg", "D. Frankfurt"],
    53: ["A. 202", "B. 206", "C. 210", "D. 208"],
    54: ["A. Java", "B. C++", "C. Python", "D. PHP"],
    55: ["A. Yellow", "B. Orange", "C. White", "D. Red"],
    56: ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
    57: ["A. Camel", "B. Donkey", "C. Horse", "D. Cow"],
    58: ["A. Automated Teller Machine", "B. Automatic Token Machine", "C. Auto Transfer Money", "D. Advanced Transfer Machine"],
    59: ["A. 12", "B. 24", "C. 60", "D. 100"],
    60: ["A. Liver", "B. Kidney", "C. Lungs", "D. Heart"],
    61: ["A. New York", "B. Washington D.C.", "C. Los Angeles", "D. Chicago"],
    62: ["A. Pakistan", "B. India", "C. Nepal", "D. Bangladesh"],
    63: ["A. Banana", "B. Mango", "C. Apple", "D. Orange"],
    64: ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"],
    65: ["A. Holi", "B. Diwali", "C. Eid", "D. Christmas"],
    66: ["A. Red", "B. Green", "C. White", "D. Blue"],
    67: ["A. 3.14", "B. 3.13", "C. 3.15", "D. 3.12"],
    68: ["A. Ant", "B. Bee", "C. Butterfly", "D. Spider"],
    69: ["A. Oxygen", "B. Hydrogen", "C. Helium", "D. Carbon"],
    70: ["A. 5", "B. 6", "C. 7", "D. 8"],
    71: ["A. Germany", "B. France", "C. Italy", "D. Spain"],
    72: ["A. National Air and Space Association", "B. National Aeronautics and Space Administration", "C. North American Space Agency", "D. New Aeronautics Space Association"],
    73: ["A. Lotus", "B. Rose", "C. Jasmine", "D. Lily"],
    74: ["A. Tiger", "B. Lion", "C. Elephant", "D. Cheetah"],
    75: ["A. 60", "B. 70", "C. 80", "D. 90"],
    76: ["A. Milan", "B. Venice", "C. Rome", "D. Naples"],
    77: ["A. Crow", "B. Parrot", "C. Sparrow", "D. Eagle"],
    78: ["A. Pentagon", "B. Hexagon", "C. Heptagon", "D. Octagon"],
    79: ["A. Wind", "B. Moon", "C. Sun", "D. Stars"],
    80: ["A. Asia", "B. Africa", "C. Europe", "D. North America"],
    81: ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
    82: ["A. Blue", "B. Red", "C. Green", "D. Yellow"],
    83: ["A. St. Petersburg", "B. Moscow", "C. Sochi", "D. Novosibirsk"],
    84: ["A. Nectar", "B. Honeydew", "C. Pollen", "D. Sugar"],
    85: ["A. Australia", "B. Greenland", "C. Madagascar", "D. Borneo"],
    86: ["A. Taste", "B. Smell", "C. Hearing", "D. Sight"],
    87: ["A. Pound", "B. Euro", "C. Dollar", "D. Franc"],
    88: ["A. Magma", "B. Lava", "C. Slag", "D. Rock"],
    89: ["A. 25", "B. 26", "C. 27", "D. 28"],
    90: ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
    91: ["A. Easter", "B. Halloween", "C. Christmas", "D. Thanksgiving"],
    92: ["A. 1", "B. 2", "C. 4", "D. 10"],
    93: ["A. Puppy", "B. Calf", "C. Kitten", "D. Chick"],
    94: ["A. Fe", "B. Ir", "C. In", "D. I"],
    95: ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Stephen Hawking"],
    96: ["A. K2", "B. Everest", "C. Kanchenjunga", "D. Lhotse"],
    97: ["A. Skin", "B. Liver", "C. Brain", "D. Lungs"],
    98: ["A. Mercury", "B. Mars", "C. Venus", "D. Jupiter"],
    99: ["A. Watt", "B. Ampere", "C. Ohm", "D. Volt"],
    100: ["A. Google", "B. Microsoft", "C. Apple", "D. Samsung"],
}

        self.answers = {1: 'B', 2: 'D', 3: 'A', 4: 'B', 5: 'C', 6: 'B', 7: 'D', 8: 'B', 9: 'C', 10: 'A', 11: 'C', 12: 'A', 13: 'B', 14: 'D', 15: 'C', 16: 'A', 17: 'D', 18: 'A', 19: 'C', 20: 'B', 21: 'D', 22: 'B', 23: 'B', 24: 'A', 25: 'C', 26: 'C', 27: 'B', 28: 'C', 29: 'A', 30: 'C', 31: 'C', 32: 'D', 33: 'B', 34: 'C', 35: 'A', 36: 'B', 37: 'A', 38: 'C', 39: 'B', 40: 'C', 41: 'D', 42: 'A', 43: 'A', 44: 'C', 45: 'B', 46: 'D', 47: 'C', 48: 'C', 49: 'A', 50: 'C', 51: 'D', 52: 'C', 53: 'B', 54: 'A', 55: 'B', 56: 'D', 57: 'C', 58: 'B', 59: 'C', 60: 'B', 61: 'A', 62: 'C', 63: 'B', 64: 'D', 65: 'A', 66: 'B', 67: 'C', 68: 'C', 69: 'A', 70: 'B', 71: 'D', 72: 'A', 73: 'B', 74: 'A', 75: 'C', 76: 'B', 77: 'D', 78: 'C', 79: 'B', 80: 'C', 81: 'D', 82: 'A', 83: 'C', 84: 'C', 85: 'D', 86: 'B', 87: 'A', 88: 'B', 89: 'D', 90: 'D', 91: 'C', 92: 'B', 93: 'A', 94: 'B', 95: 'A', 96: 'C', 97: 'C', 98: 'B', 99: 'A', 100: 'D'}

        self.question_ids = random.sample(list(self.questions.keys()), len(self.questions))

        self.question_label = tk.Label(master, text="", wraplength=400, font=('Helvetica', 14))
        self.question_label.pack(pady=20)

        self.option_vars = []
        self.selected_option = tk.StringVar()
        for i in range(4):
            rb = tk.Radiobutton(master, variable=self.selected_option, value='', text='', font=('Helvetica', 12), anchor='w')
            rb.pack(fill='x', padx=50, pady=2)
            self.option_vars.append(rb)

        self.submit_btn = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_btn.pack(pady=10)

        self.status_label = tk.Label(master, text=f"Score: {self.score} | Lives: {self.lives}", font=('Helvetica', 12))
        self.status_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.lives == 0 or self.current_q_index == len(self.question_ids):
            self.end_quiz()
            return

        q_id = self.question_ids[self.current_q_index]
        self.current_question_id = q_id
        self.question_label.config(text=self.questions[q_id])
        options = self.options[q_id]
        self.selected_option.set(None)
        for i, opt in enumerate(options):
            self.option_vars[i].config(text=opt, value=opt[0])

        self.status_label.config(text=f"Score: {self.score} | Lives: {self.lives}")

    def submit_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Select Option", "Please select an answer!")
            return

        correct_ans = self.answers[self.current_question_id]
        if selected == correct_ans:
            self.score += 1
            messagebox.showinfo("Correct!", "Good job! That's the right answer.")
        else:
            self.lives -= 1
            messagebox.showerror("Incorrect", f"Wrong answer! Correct was: {correct_ans}")

        self.current_q_index += 1
        self.next_question()

    def end_quiz(self):
        percentage = (self.score / len(self.questions)) * 100
        msg = f"Quiz Over!\nFinal Score: {self.score}/{len(self.questions)}\nPercentage: {percentage:.2f}%"
        messagebox.showinfo("Result", msg)
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

