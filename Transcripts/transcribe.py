"""
Transcribe Big Picture Trading videos.

Usage:
    python transcribe.py <video_id> <date>

Example:
    python transcribe.py 1189778472 20260506

Expects an audio file named: audio_<date>.mp4 (or .m4a) in the current directory.
Produces: wherestrade_<date>_transcript.txt
"""

import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

from faster_whisper import WhisperModel


def find_audio_file(date: str) -> Path:
    """Look for audio_<date>.mp4 / .m4a / other common extensions."""
    candidates = [
        f"audio_{date}.mp4",
        f"audio_{date}.m4a",
        f"audio_{date}.webm",
        f"audio_{date}.opus",
    ]
    for name in candidates:
        p = Path(name)
        if p.exists():
            return p
    raise FileNotFoundError(
        f"No audio file found for date {date}. "
        f"Expected one of: {', '.join(candidates)}"
    )


def main():
    # Windows consoles default to cp1252; Whisper occasionally emits curly
    # quotes / em-dashes / non-Latin glyphs that crash a raw print(). The
    # .txt file is already UTF-8; force stdout/stderr to match so the live
    # progress stream survives any segment Whisper produces.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    if len(sys.argv) != 3:
        print("Usage: python transcribe.py <video_id> <date>")
        print("Example: python transcribe.py 1189778472 20260506")
        sys.exit(1)

    video_id = sys.argv[1]
    date = sys.argv[2]

    audio_file = find_audio_file(date)
    output_file = f"wherestrade_{date}_transcript.txt"

    print(f"Video ID: {video_id}")
    print(f"Date: {date}")
    print(f"Audio file: {audio_file}")
    print(f"Output: {output_file}\n")

    print("Loading model...")
    model = WhisperModel(
        "large-v3",
        device="cpu",
        compute_type="int8",
        cpu_threads=8,
    )

    print(f"Transcribing {audio_file}...")
    start = time.time()

    segments, info = model.transcribe(
        str(audio_file),
        language="en",
        initial_prompt=(
            "Trading commentary discussing SPY, QQQ, IWM, VIX, options, puts, calls, "
            "strikes, vega, theta, gamma, skew, IV, S&P 500, Nasdaq, Russell, Fed, "
            "FOMC, earnings, support, resistance, breakout, fib retracement, "
            "Patrick Ceresna, Big Picture Trading."
        ),
        vad_filter=True,
        beam_size=5,
    )

    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})")
    print(f"Audio duration: {info.duration:.1f}s\n")

    with open(output_file, "w", encoding="utf-8") as f:
        # Write header with metadata
        f.write(f"# Where is the Trade — {date}\n")
        f.write(f"# Video ID: {video_id}\n")
        f.write(f"# Source: https://player.vimeo.com/video/{video_id}\n")
        f.write(f"# Audio duration: {info.duration:.1f}s\n\n")

        for seg in segments:
            mm = int(seg.start // 60)
            ss = int(seg.start % 60)
            line = f"[{mm:02d}:{ss:02d}] {seg.text.strip()}\n"
            f.write(line)
            f.flush()  # write progressively to disk
            print(line, end="", flush=True)

    elapsed = time.time() - start
    print(f"\nDone in {elapsed/60:.1f} min — saved to {output_file}")


if __name__ == "__main__":
    main()
