from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List of questions and corresponding answers
questions = [
    {
        "question": "Does your skin feel oily throughout the day?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Does your skin feel tight or flaky after washing?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Is your skin prone to redness or irritation?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Do you notice visible shine on your T-zone?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Does your skin feel rough or show signs of flakiness?",
        "options": ["Yes", "No"]
    },
    {
        "question": "How often do you experience breakouts or acne?",
        "options": ["Always", "Sometimes", "Rarely", "Never"]
    },
    {
        "question": "How often do you wear sunscreen?",
        "options": ["Always", "Sometimes", "Rarely", "Never"]
    },
    {
        "question": "How often do you moisturize your skin?",
        "options": ["Daily", "Occasionally", "Never"]
    },
    {
        "question": "Do you live in a humid or dry climate?",
        "options": ["Humid", "Dry"]
    },
    {
        "question": "How much water do you drink daily?",
        "options": ["Less than 1 liter", "1-2 liters", "More than 2 liters"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/analyze', methods=['POST'])
def analyze():
    answers = request.form.to_dict()
    skin_type, skin_score = analyze_skin_type(answers)
    
    return render_template('analysis.html', skin_type=skin_type, skin_score=skin_score)

def analyze_skin_type(answers):
    skin_score = {"Oily": 0, "Dry": 0, "Sensitive": 0, "Normal": 0}
    
    # Scoring based on answers
    if answers.get('Does_your_skin_feel_oily_throughout_the_day?') == 'Yes':
        skin_score["Oily"] += 1
    if answers.get('Does_your_skin_feel_tight_or_flaky_after_washing?') == 'Yes':
        skin_score["Dry"] += 1
    if answers.get('Is_your_skin_prone_to_redness_or_irritation?') == 'Yes':
        skin_score["Sensitive"] += 1
    if answers.get('Do_you_notice_visible_shine_on_your_T-zone?') == 'Yes':
        skin_score["Oily"] += 1
    if answers.get('Does_your_skin_feel_rough_or_show_signs_of_flakiness?') == 'Yes':
        skin_score["Dry"] += 1
    if answers.get('How_often_do_you_experience_breakouts_or_acne?') in ['Always', 'Sometimes']:
        skin_score["Oily"] += 1
    if answers.get('How_often_do_you_wear_sunscreen?') in ['Rarely', 'Never']:
        skin_score["Sensitive"] += 1
    if answers.get('How_often_do_you_moisturize_your_skin?') == 'Never':
        skin_score["Dry"] += 1
    if answers.get('Do_you_live_in_a_humid_or_dry_climate?') == 'Dry':
        skin_score["Dry"] += 1
    
    # Determine the skin type with the highest score
    skin_type = max(skin_score, key=skin_score.get)

    return skin_type, skin_score

if __name__ == '__main__':
    app.run(debug=True)
