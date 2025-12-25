# Chatterbox Turbo – Local TTS (WSL + CUDA)

This project runs **Chatterbox Turbo TTS** locally using **GPU acceleration (CUDA)**.
Text is converted into speech audio entirely on my machine (no API calls).

---

## High-level Overview

- Uses a **pretrained TTS model** hosted on Hugging Face
- Model weights are downloaded once using a **Hugging Face `read token`**
- Inference runs **locally on the GPU**
- Output is a `.wav` file written to disk

Pipeline (simplified):

```

Text → tokenizer → neural network (GPU) → waveform → WAV file

````

---

## Environment

- OS: WSL (Ubuntu)
- Python: 3.11
- GPU: CUDA-enabled (verified via `torch.cuda.is_available()`)

---

## Dependencies

Installed using `uv` (not pip or conda):

```toml
dependencies = [
  "chatterbox-tts>=0.1.6",
  "onnx<1.17.0",
  "torch>=2.6.0",
  "torchaudio>=2.6.0",
]
````

### Why `onnx<1.17.0` is pinned

```bash
  File "/home/clif/projects/chatterbox-project/.venv/lib/python3.11/site-packages/ml_dtypes/__init__.py", line 71, in __getattr__
    raise AttributeError(f'cannot import name {name!r} from {__name__!r}')
AttributeError: cannot import name 'float4_e2m1fn' from 'ml_dtypes'. Did you mean: 'float8_e4m3fn'?
```

* Newer `onnx` depends on a newer `ml_dtypes`
* `s3tokenizer` (a transitive dependency) expects symbols not present in newer versions
* Resulted in runtime error:

  ```
  AttributeError: cannot import name 'float4_e2m1fn' from ml_dtypes
  ```
* Pinning `onnx` resolves the mismatch

---

## Hugging Face `Read Token` (Important)

```bash
  File "/home/clif/projects/chatterbox-project/.venv/lib/python3.11/site-packages/huggingface_hub/utils/_headers.py", line 159, in get_token_to_send
    raise LocalTokenNotFoundError(
huggingface_hub.errors.LocalTokenNotFoundError: Token is required (`token=True`), but no token found. You need to provide a token or be logged in to Hugging Face with `hf auth login` or `huggingface_hub.login`. See https://huggingface.co/settings/tokens
```

* Required **only once** to download pretrained weights
* Token is stored locally at:

  ```
  ~/.cache/huggingface/token
  ```
* The token is **not** committed to git
* If the cache is lost, just log in again `uv run hf auth login` and re-download from here `https://huggingface.co/settings/tokens`

No inference calls go through Hugging Face after download.

---

## Source Code Patch (Watermark Bug)

The upstream `chatterbox` code assumes the `perth` watermark dependency exists.
In this environment it did not, causing runtime errors.

```bash
  File "/home/clif/projects/chatterbox-project/.venv/lib/python3.11/site-packages/chatterbox/tts_turbo.py", line 130, in __init__
    self.watermarker = perth.PerthImplicitWatermarker()
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'perth' has no attribute 'PerthImplicitWatermarker'
```

### Fix applied

In `chatterbox/tts_turbo.py`, watermarking was made optional.

**Fixed (safe):**

```python
        self.watermarker = None

if self.watermarker is not None:
    wav = self.watermarker.apply_watermark(wav, sample_rate=self.sr)
return torch.from_numpy(wav).unsqueeze(0)
```

This allows TTS to work without watermarking.

---

## File Output (WSL → Windows)

Audio is written to the Windows filesystem via:

```
/mnt/c/Users/<username>/Desktop/output.wav
```

Ensure the path exists. Writing to WSL filesystem also works.

---

## Minimal Example

```python
import torchaudio as ta
from chatterbox.tts_turbo import ChatterboxTurboTTS

model = ChatterboxTurboTTS.from_pretrained(device="cuda")

text = "Hello, this is a test for PowerPoint presentation."

wav = model.generate(text)

ta.save("/mnt/c/Users/cclif/Desktop/output.wav", wav, model.sr)
```

---

## Notes for Future Me

* SSD noise during inference is normal (GPU power / coil whine)
* Warnings about LoRA / diffusers are non-fatal
* If something breaks, check **dependency versions first**
* This project runs fully offline after initial model download

---

## Reproducibility Guarantee

This project is reproducible as long as:
- `uv.lock` is preserved
- Python 3.11 is used
- CUDA-compatible GPU is available

To reproduce the known-good environment:

```bash
uv sync
```