## This is a supposed views.py file for a django project to suit this task
## I have buit one locally with crud functionalities for extracted 
## questions on my system
## I should make it live but time may not permit



from django.shortcuts import render
from django.shortcuts import render, redirect
import pdfplumber
import re
from .models import Question #Asuming we have question models in the database or models.py

def home(request):
    def extract_text_from_pdf(pdf_path):
        """Extracts raw text from each page of the PDF."""
        text_content = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text_content.append(page.extract_text())
        return "\n".join(text_content)

    def parse_questions_from_text(text):
        """Parses questions and options from the extracted text."""
        question_blocks = re.split(r"\n\d+\.\s", text)[1:]  # Split by numbered questions

        parsed_questions = []
        for block in question_blocks:
            # Extract the main question
            main_question_match = re.search(r"^(.*?)(?:\n|$)", block)
            main_question = main_question_match.group(1).strip() if main_question_match else None

            # Extract options A through D (and possibly E)
            options = {}
            for option_label in ['A', 'B', 'C', 'D', 'E']:
                option_match = re.search(rf"{option_label}\.\s+(.*?)(?:\n[A-E]\.|$)", block)
                if option_match:
                    options[option_label.lower()] = option_match.group(1).strip()

            parsed_questions.append({
                "question_main": main_question,
                "options": options
            })

        return parsed_questions

    # Run the process
    pdf_path = "accounting.pdf"  # Path to the PDF file
    text = extract_text_from_pdf(pdf_path)
    questions = parse_questions_from_text(text)
    for i in questions:
        Question.objects.create(
            question_main=i['question_main'],
            a=i['options']['a'],
            b=i['options']['b'],
            c=i['options']['c'],
            d=i['options']['d'],

        )

    context = {'questions': questions}
    return render(request, 'index.html', context)

