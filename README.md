# Interview Agent

This repository contains a simple example of using the [ElevenLabs](https://elevenlabs.io/) API to ask interview questions with a synthetic voice. The user replies using their microphone and the script transcribes the answer using `SpeechRecognition`.

## Requirements

- Python 3.11+
- `ffmpeg` installed (for audio playback using `ffplay`). On macOS you can install it with Homebrew:
  ```bash
  brew install ffmpeg
  ```
- `portaudio` to record from the microphone (install with `brew install portaudio` on macOS).
- An ElevenLabs API key set in the environment variable `ELEVEN_API_KEY`.

Install Python dependencies:

```bash
pip install elevenlabs==1.0.4 SpeechRecognition pyaudio
```

## Running

Execute the script and follow the prompts:

```bash
python interview_agent.py
```

The agent will ask a series of interview questions out loud. After each question, speak your answer into the microphone. The script will print the recognized text on the console.
