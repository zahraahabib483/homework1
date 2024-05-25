import json
import os

def read_questions_from_json(file_path):
    """اقرأ الأسئلة والأجوبة من ملف JSON."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return [(item['question'], item['answer']) for item in data]

def ask_questions(questions):
    """اطرح الأسئلة على المستخدم وجمع الإجابات."""
    correct_answers = 0
    for question, correct_answer in questions:
        user_answer = input(f"{question}? ").strip()
        if user_answer == correct_answer:
            correct_answers += 1
    return correct_answers

def save_results_to_json(file_path, username, score, total_questions):
    """احفظ اسم المستخدم والنتيجة في ملف بصيغة JSON."""
    result = {
        "username": username,
        "score": score,
        "total_questions": total_questions
    }

    if not os.path.isfile(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([result], file, ensure_ascii=False, indent=4)
    else:
        try:
            with open(file_path, 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                data.append(result)
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([result], file, ensure_ascii=False, indent=4)

def main():
    questions_file = 'questions.json'
    questions = read_questions_from_json(questions_file)
    
    username = input("أدخل اسم المستخدم: ").strip()
    correct_answers = ask_questions(questions)
    total_questions = len(questions)
    
    print(f"{username}, لقد أجبت بشكل صحيح على {correct_answers} من أصل {total_questions} سؤال.")
    
    results_file = 'results.json'
    save_results_to_json(results_file, username, correct_answers, total_questions)

if __name__ == "__main__":
    main()
