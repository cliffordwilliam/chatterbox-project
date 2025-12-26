import torchaudio as ta
from chatterbox.tts_turbo import ChatterboxTurboTTS

model = ChatterboxTurboTTS.from_pretrained(device="cuda")

text = "Hi there, Sarah here from MochaFone calling you back [chuckle], have you got one minute to chat about the billing issue?"

wav = model.generate(text)

ta.save("/mnt/c/Users/cclif/Desktop/output.wav", wav, model.sr)