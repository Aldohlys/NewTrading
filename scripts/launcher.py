"""Tkinter launcher for the trading-analysis .bat files in this directory.

Auto-discovers every *.bat (except Launcher_Trading.bat itself), shows one row
per script.

Argument handling:
- If a .bat contains a `REM @args: NAME1 NAME2 [optional1] ...` line, the
  launcher renders one labeled entry box per token. Tokens in [brackets] are
  optional; required tokens are bare. Missing required entries are flagged.
- Otherwise, if the .bat references %1/%*/%~n, a single generic entry is shown.

On Run, all non-empty entry values are concatenated with spaces and passed to
the .bat in a new console window so its output and trailing `pause` still work.
"""
from __future__ import annotations

import re
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

SCRIPTS_DIR = Path(__file__).resolve().parent
ARG_MARKER = re.compile(r"%(?:\*|~?[0-9])")
ARGS_DECL = re.compile(r"^\s*REM\s+@args:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
ARG_TOKEN = re.compile(r"\[([^\]]+)\]|(\S+)")
SKIP = {"Launcher_Trading.bat"}


def parse_args_decl(text: str) -> list[tuple[str, bool]] | None:
    """Return [(name, required), ...] from a `REM @args:` line, or None."""
    m = ARGS_DECL.search(text)
    if not m:
        return None
    tokens: list[tuple[str, bool]] = []
    for opt, req in ARG_TOKEN.findall(m.group(1)):
        if opt:
            tokens.append((opt, False))
        elif req:
            tokens.append((req, True))
    return tokens


def inspect_bat(bat_path: Path) -> list[tuple[str, bool]] | bool:
    """Return arg spec list, True for generic-args, False for no-args."""
    try:
        text = bat_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    spec = parse_args_decl(text)
    if spec is not None:
        return spec
    return bool(ARG_MARKER.search(text))


def discover() -> list[tuple[Path, list[tuple[str, bool]] | bool]]:
    bats = sorted(p for p in SCRIPTS_DIR.glob("*.bat") if p.name not in SKIP)
    return [(p, inspect_bat(p)) for p in bats]


def run_bat(bat_path: Path, entries: list[tuple[str, bool, tk.Entry]]) -> None:
    parts: list[str] = []
    missing: list[str] = []
    for name, required, entry in entries:
        val = entry.get().strip()
        if not val:
            if required:
                missing.append(name)
            continue
        parts.append(val)
    if missing:
        messagebox.showwarning(
            "Missing arguments",
            f"{bat_path.name} requires: {', '.join(missing)}",
        )
        return
    args_str = " ".join(parts)
    cmd = f'start "{bat_path.stem}" cmd /c ""{bat_path}" {args_str}"'
    subprocess.Popen(cmd, shell=True, cwd=str(SCRIPTS_DIR))


def build_ui() -> None:
    root = tk.Tk()
    root.title("Trading launcher")
    root.geometry("760x640")

    header = ttk.Label(
        root,
        text=f"Scripts in {SCRIPTS_DIR}",
        padding=(10, 8),
        font=("Segoe UI", 9, "italic"),
    )
    header.pack(fill="x")

    container = ttk.Frame(root, padding=8)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, highlightthickness=0)
    scroll = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    rows = ttk.Frame(canvas)
    rows.bind(
        "<Configure>",
        lambda _e: canvas.configure(scrollregion=canvas.bbox("all")),
    )
    canvas.create_window((0, 0), window=rows, anchor="nw")
    canvas.configure(yscrollcommand=scroll.set)
    canvas.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    bold = ("Segoe UI", 9, "bold")
    italic = ("Segoe UI", 9, "italic")

    for bat_path, spec in discover():
        row = ttk.Frame(rows, padding=(0, 4))
        row.pack(fill="x", expand=True)

        ttk.Label(row, text=bat_path.stem, width=18, anchor="w").pack(side="left")

        entries: list[tuple[str, bool, tk.Entry]] = []
        if isinstance(spec, list):
            for name, required in spec:
                cell = ttk.Frame(row)
                cell.pack(side="left", padx=(0, 6))
                lbl_font = bold if required else italic
                ttk.Label(cell, text=name, font=lbl_font).pack(anchor="w")
                e = ttk.Entry(cell, width=14)
                e.pack()
                entries.append((name, required, e))
        elif spec is True:
            cell = ttk.Frame(row)
            cell.pack(side="left", padx=(0, 6))
            ttk.Label(cell, text="args", font=italic).pack(anchor="w")
            e = ttk.Entry(cell, width=30)
            e.pack()
            entries.append(("args", False, e))

        btn = ttk.Button(
            row,
            text="Run",
            width=8,
            command=lambda p=bat_path, es=entries: run_bat(p, es),
        )
        btn.pack(side="right", anchor="s")

    legend = ttk.Label(
        root,
        text="Bold = required, italic = optional. Each Run opens a new console window.",
        padding=(10, 6),
        foreground="#666",
    )
    legend.pack(fill="x", side="bottom")

    root.mainloop()


if __name__ == "__main__":
    build_ui()
