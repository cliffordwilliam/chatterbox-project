import torchaudio as ta
from chatterbox.tts_turbo import ChatterboxTurboTTS

model = ChatterboxTurboTTS.from_pretrained(device="cuda")

text = "Hello, this is a test for PowerPoint presentation."

wav = model.generate(text)

ta.save("/mnt/c/Users/cclif/Desktop/output.wav", wav, model.sr)