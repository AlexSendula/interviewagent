import os
import speech_recognition as sr
from elevenlabs import ElevenLabs, play

QUESTIONS = [
    "What is your name?",
    "Can you tell me about yourself?",
    "Why do you want to work here?",
    "Describe a challenging situation you solved.",
    "Where do you see yourself in five years?",
]


def ask_question(client: ElevenLabs, question: str) -> str:
    print(f"Agent: {question}")
    audio_stream = client.generate(text=question)
    play(audio_stream)
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your answer (speak now)...")
        audio_data = recognizer.listen(source)
    try:
        answer = recognizer.recognize_google(audio_data)
        print(f"You: {answer}")
    except sr.UnknownValueError:
        answer = ""
        print("Sorry, I could not understand your response.")
    return answer


def run_interview():
    client = ElevenLabs(api_key=os.environ.get("ELEVEN_API_KEY"))
    responses = []
    for q in QUESTIONS:
        responses.append(ask_question(client, q))
    print("Interview finished. Your answers:")
    for q, a in zip(QUESTIONS, responses):
        print(f"Q: {q}\nA: {a}\n")


if __name__ == "__main__":
    run_interview()
