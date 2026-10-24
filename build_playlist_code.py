import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GIT_DIR = ROOT / ".course-source.git"
OUT = ROOT / "LARAVEL_PLAYLIST_CODE.md"

TITLES = {
    1: "Laravel Tutorial for Beginners #1 - Introduction & Setup",
    2: "Laravel Tutorial for Beginners #2 - Routes & Views",
    3: "Laravel Tutorial for Beginners #3 - Route Wildcards & Data",
    4: "Laravel Tutorial for Beginners #4 - Blade Directives",
    5: "Laravel Tutorial for Beginners #5 - Layouts & Slots",
    6: "Laravel Tutorial for Beginners #6 - Components, Attributes & Props",
    7: "Laravel Tutorial for Beginners #7 - Adding CSS & Tailwind",
    8: "Laravel Tutorial for Beginners #8 - Migrations",
    9: "Laravel Tutorial for Beginners #9 - Eloquent Models",
    10: "Laravel Tutorial for Beginners #10 - Model Factories",
    11: "Laravel Tutorial for Beginners #11 - Seeders",
    12: "Laravel Tutorial for Beginners #12 - MVC & Controllers",
    13: "Laravel Tutorial for Beginners #13 - More on Controllers",
    14: "Laravel Tutorial for Beginners #14 - Named Routes",
    15: "Laravel Tutorial for Beginners #15 - Pagination",
    16: "Laravel Tutorial for Beginners #16 - Foreign Keys (part 1)",
    17: "Laravel Tutorial for Beginners #17 - Foreign Keys (part 2)",
    18: "Laravel Tutorial for Beginners #18 - Making a Web Form",
    19: "Laravel Tutorial for Beginners #19 - Handling POST Requests",
    20: "Laravel Tutorial for Beginners #20 - Showing Form Errors",
    21: "Laravel Tutorial for Beginners #21 - DELETE Requests",
    22: "Laravel Tutorial for Beginners #22 - Flash Messages",
    23: "Laravel Tutorial for Beginners #23 - Route Model Binding",
}

LANGS = {
    ".php": "php",
    ".blade.php": "blade",
    ".css": "css",
    ".js": "javascript",
    ".json": "json",
}


def git(*args):
    return subprocess.check_output(
        ["git", f"--git-dir={GIT_DIR}", *args], cwd=ROOT
    ).decode("utf-8", errors="replace")


def code_language(path):
    if path.endswith(".blade.php"):
        return "blade"
    suffix = Path(path).suffix
    return LANGS.get(suffix, "text")


def included(path):
    if path in {"routes/web.php", "resources/views/welcome.blade.php"}:
        return True
    if path.endswith((".php", ".blade.php", ".css", ".js")):
        return True
    if path in {"composer.json", "package.json", "postcss.config.js", "tailwind.config.js"}:
        return True
    return False


changes = {}
for lesson in range(1, 24):
    if lesson == 1:
        names = git("diff", "--name-only", "main", "lesson-1").splitlines()
        # The first lesson's source branch is a full framework scaffold. Keep the
        # files directly used for the first landing-page walkthrough.
        names = [p for p in names if p in {
            "routes/web.php", "resources/views/welcome.blade.php"
        }]
    elif lesson == 8:
        # The upstream repository has no lesson-8 branch. Lesson-9 contains the
        # first committed migrations snapshot; this is the only migration file
        # assigned to lesson 8, and is identified as reconstructed below.
        names = [
            "database/migrations/2024_10_12_124138_create_ninjas_table.php"
        ]
    elif lesson == 9:
        names = git("diff", "--name-only", "lesson-7", "lesson-9").splitlines()
        names = [p for p in names if p not in {
            "database/migrations/2024_10_12_124138_create_ninjas_table.php"
        }]
    else:
        previous = f"lesson-{lesson - 1}"
        current = f"lesson-{lesson}"
        names = git("diff", "--name-only", previous, current).splitlines()

    changes[lesson] = sorted(p for p in names if included(p))

parts = [
    "<!-- Source basis: the instructor's public repository https://github.com/iamshaunjp/laravel-11-for-beginners, using its lesson branch snapshots. These source snapshots are not a frame-by-frame transcription of the videos; video-only terminal commands and code that cannot be confirmed from the source are omitted. The repository has no `lesson-8` branch; its ninja migration below is placed in Lesson 8 based on the course sequence and first available snapshot (`lesson-9`). -->",
    "",
]

for lesson in range(1, 24):
    snapshot = "lesson-9 (reconstructed; no lesson-8 branch)" if lesson == 8 else f"lesson-{lesson}"
    parts.append(f"### Lesson {lesson} — {TITLES[lesson]}")
    parts.append("")
    if lesson == 8:
        parts.append("<!-- Reconstructed from the first available migration snapshot on lesson-9. -->")
        parts.append("")
    files = changes[lesson]
    if not files:
        parts.append("<!-- No changed source files in the instructor's matching repository snapshot. -->")
        parts.append("")
        continue
    for path in files:
        parts.append(f"**File:** `{path}`")
        parts.append(f"```{code_language(path)}")
        content = git("show", f"{snapshot.split()[0]}:{path}")
        parts.append(content.rstrip("\n"))
        parts.append("```")
        parts.append("")

OUT.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
