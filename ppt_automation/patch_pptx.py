"""
PowerPoint Auto-Patcher using win32com

Patches generated PPTX to enable autoplay audio and set transition timing
"""

import sys
from pathlib import Path
import tomllib
import win32com.client


def patch_powerpoint(pptx_path: str, durations: list[float]):
    pptx_path = str(Path(pptx_path).resolve())
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    try:
        presentation = ppt.Presentations.Open(pptx_path)
        print(f"Opened presentation: {presentation.Name}, slides: {presentation.Slides.Count}")

        for i in range(1, presentation.Slides.Count + 1):
            slide = presentation.Slides(i)
            slide.SlideShowTransition.EntryEffect = 3956
            slide.SlideShowTransition.Duration = 1.5

            if i - 1 < len(durations):
                audio_duration = durations[i - 1]
                transition_time = audio_duration + 0.5
                slide.SlideShowTransition.AdvanceOnTime = True
                slide.SlideShowTransition.AdvanceTime = transition_time
                print(
                    f"  Slide {i}: Set transition to {transition_time:.2f}s "
                    f"(audio: {audio_duration:.2f}s)"
                )
            else:
                print(f"  Slide {i}: No duration found, skipping timing")
        
            for shape in slide.Shapes:
                if shape.Type == 16:
                    print(f"  Slide {i}: Adding animation to play audio automatically")
                    effect = slide.TimeLine.MainSequence.AddEffect(
                        shape,
                        83,
                        0,
                        0,
                    )
                    effect.Timing.TriggerType = 2
                    shape.AnimationSettings.PlaySettings.HideWhileNotPlaying = True


        presentation.Save()
        presentation.Close()
        print("✓ Patching complete!")

    finally:
        ppt.Quit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python patch_pptx.py <pptx_path>")
        sys.exit(1)

    pptx_path = sys.argv[1]

    BASE_DIR = Path(__file__).parent
    INPUT_DIR = BASE_DIR / "input"

    with open(INPUT_DIR / "presentation.toml", "rb") as f:
        data = tomllib.load(f)

    durations = [slide["duration"] for slide in data["slides"]]

    patch_powerpoint(pptx_path, durations)
