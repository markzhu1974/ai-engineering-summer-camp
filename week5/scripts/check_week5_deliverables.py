from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_PATHS = [
    ROOT / "kicad_project",
    ROOT / "gerber",
    ROOT / "screenshots",
    ROOT / "rl_pcb_workspace",
    ROOT / "reports" / "kicad_report_template.md",
    ROOT / "reports" / "rl_pcb_report_template.md",
    ROOT / "reports" / "final_week5_report_template.md",
]


def main():
    print("Week5 deliverable structure check")
    print("=" * 40)
    for path in EXPECTED_PATHS:
        status = "OK" if path.exists() else "MISSING"
        print(f"{status}: {path.relative_to(ROOT)}")

    kicad_files = [
        path for path in (ROOT / "kicad_project").glob("*.kicad_*")
        if path.name != ".gitkeep"
    ]
    gerber_files = [
        path for path in (ROOT / "gerber").glob("*")
        if path.name != ".gitkeep"
    ]
    screenshots = [
        path for path in (ROOT / "screenshots").glob("*")
        if path.name != ".gitkeep"
    ]

    print("\nContent check")
    print("=" * 40)
    print(f"KiCad source files: {len(kicad_files)}")
    print(f"Gerber folder files: {len(gerber_files)}")
    print(f"Screenshot files: {len(screenshots)}")

    if not kicad_files:
        print("TODO: Add KiCad project files to kicad_project/")
    if not gerber_files:
        print("TODO: Export Gerber/Drill files to gerber/")
    if not screenshots:
        print("TODO: Add screenshots to screenshots/")


if __name__ == "__main__":
    main()
