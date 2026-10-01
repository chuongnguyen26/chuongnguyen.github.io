#!/usr/bin/env python3
"""Generate Chuong_Nguyen_Resume.pdf — clean, readable, space-efficient layout."""

from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Chuong_Nguyen_Resume.pdf"

BODY = 9.5
SMALL = 8.5
SECTION = 10
NAME = 16
LINE = 11.5  # minimum line height — prevents overlapping text


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(format="letter", unit="pt")
        self.set_auto_page_break(auto=True, margin=36)
        self.set_margins(48, 36, 48)

    def section(self, title: str):
        self.ln(8)
        self.set_font("Helvetica", "B", SECTION)
        self.set_text_color(40, 40, 40)
        self.cell(0, LINE, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y = self.get_y()
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.5)
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(5)
        self.set_text_color(0, 0, 0)

    def entry(self, title: str, date: str, bullets: list[str] | None = None, subtitle: str | None = None):
        """Job/role block: title + right-aligned date, optional subtitle and bullets."""
        self.ln(5)
        width = self.w - self.l_margin - self.r_margin
        date_col = max(self.get_string_width(date) + 10, 78)

        self.set_font("Helvetica", "B", BODY)
        title_fits = self.get_string_width(title) <= width - date_col - 8

        if title_fits:
            self.set_x(self.l_margin)
            self.cell(width - date_col, LINE, title)
            self.set_font("Helvetica", "", SMALL)
            self.cell(date_col, LINE, date, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        else:
            self.set_x(self.l_margin)
            self.multi_cell(0, LINE, title, align="L")
            self.set_font("Helvetica", "", SMALL)
            self.cell(0, LINE - 1, date, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        if subtitle:
            self.set_x(self.l_margin)
            self.set_font("Helvetica", "I", BODY)
            self.multi_cell(0, LINE, subtitle, align="L")

        if bullets:
            for text in bullets:
                self.bullet(text)

    def bullet(self, text: str):
        indent = 12
        self.set_x(self.l_margin + indent)
        self.set_font("Helvetica", "", BODY)
        self.cell(6, LINE, chr(183))
        self.multi_cell(self.w - self.l_margin - self.r_margin - indent - 6, LINE, text, align="L")
        self.ln(1)

    def text_line(self, text: str, style: str = "", size: float = BODY):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", style, size)
        self.multi_cell(0, LINE, text, align="L")
        self.ln(1)

    def skill_line(self, label: str, text: str):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", BODY)
        lw = self.get_string_width(label + " ")
        self.cell(lw, LINE, label + " ")
        self.set_font("Helvetica", "", BODY)
        self.multi_cell(self.w - self.l_margin - self.r_margin - lw, LINE, text, align="L")
        self.ln(1)

    def publication(self, year: str, authors: str, title: str, venue: str, name: str = "C Nguyen"):
        def write(style: str, text: str):
            self.set_font("Helvetica", style, BODY)
            first_word = text.split(" ", 1)[0]
            if self.get_x() + self.get_string_width(first_word) > self.w - self.r_margin:
                self.ln(LINE)
            self.write(LINE, text)

        self.set_x(self.l_margin)
        write("B", f"[{year}] ")
        for i, part in enumerate(authors.split(name)):
            if i:
                write("B", name)
            write("", part)
        write("", ". ")
        write("I", title)
        write("", f". {venue}.")
        self.ln(LINE + 5)


def build():
    pdf = ResumePDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", NAME)
    pdf.cell(0, 18, "Chuong Nguyen", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", SMALL)
    pdf.multi_cell(
        0,
        LINE,
        "chuongn194@gmail.com | chn021@ucsd.edu | github.com/chuongnguyen26 | "
        "linkedin.com/in/chuong-nguyen-profile",
    )
    pdf.ln(4)

    pdf.section("Education")
    pdf.entry(
        "University of California, San Diego - B.S. Computer Science",
        "Sep 2022 - Jun 2026",
        subtitle="Degree conferred June 2026 | GPA: 3.803",
    )

    pdf.section("Research Publications")
    pdf.text_line("Co-first authors marked with *. My name is in bold.", "I", SMALL)

    publications = [
        (
            "2026",
            "X Pi*, Q Yang*, C Nguyen*, H Shen",
            "Bridge Human Interpretation and Machine Representation With Explicit "
            "Specification For Qualitative Data Analysis In LLM Era",
            "International Conference on Machine Learning (ICML) 2026 - Position Paper (Poster) (arXiv:2601.11739)",
        ),
        (
            "2026",
            "T Smith*, C Nguyen*, Q Yang, O Bandopadhyay, Y Su, N Polikarpova, X Pi",
            "QualAlign: Benchmarking Automated Qualitative Coding Against Human Schemas",
            "Conference on Language Modeling (COLM) 2026",
        ),
        (
            "2025",
            "X Pi*, Q Yang*, C Nguyen*",
            "LOGOS: LLM-driven End-to-End Grounded Theory Development and Schema Induction "
            "for Qualitative Research",
            "arXiv preprint arXiv:2509.24294",
        ),
        (
            "2024",
            "A Smithwick*, C Nguyen*, E Gorial*, N Tran*, AM Flores, INS Munyaka",
            '"Parent seeking Roblox Safety Help": Comparing Parental Roblox Concerns to '
            "Roblox Offerings",
            "IEEE ISTAS 2024, pp. 1-9",
        ),
    ]
    for year, authors, title, venue in publications:
        pdf.publication(year, authors, title, venue)

    pdf.section("Research Experience")
    pdf.entry(
        "Research Assistant, HDSI - UC San Diego",
        "Apr 2025 - Present",
        bullets=[
            "LLMs, agentic frameworks, and data mining for qualitative research; grounded theory, schema induction, and human-aligned reasoning.",
            "Co-authored ICML 2026 position paper and COLM 2026 paper on LLM-assisted qualitative analysis.",
            "Fine-tuned LLMs with SFT/GRPO; explored test-time scaling and process reward models.",
        ],
    )
    pdf.entry(
        "Research Assistant, Ujima Lab - UC San Diego",
        "Sep 2023 - Oct 2024",
        bullets=[
            "Beauty Filter: analyzed filter-driven facial enhancements and cultural bias; migrated landmark analysis to a remote server.",
            "Smart Mirror: Raspberry Pi + DeepFace/Retina for real-time facial analysis in a public art installation.",
            'Co-authored "Parent seeking Roblox Safety Help" (IEEE ISTAS 2024); topic modeling on 10,000+ Reddit posts and survey of 100 participants.',
        ],
    )
    pdf.entry(
        "Early Research Scholars Program - UC San Diego",
        "Sep 2023 - Jun 2024",
        subtitle="Roblox Safety (IEEE ISTAS); Hate-Crime news pipeline (ERSP)",
        bullets=[
            "Topic modeling on 10,000+ Reddit posts; surveyed 100 participants on parental concerns.",
            "Built scraping pipeline with SerpAPI, NewsPlease, DBSCAN, MeanShift, and OpenAI API.",
        ],
    )

    pdf.section("Project Experience")
    pdf.entry(
        "Software Developer, Zooseeker",
        "Apr 2024 - Jun 2024",
        bullets=[
            "Database schema, Android UI revamp, and documentation for a zoo navigation app.",
        ],
    )
    pdf.entry(
        "ACM AI - UC San Diego",
        "Oct 2022 - Jan 2023",
        subtitle="Credit Card Fraud Detector",
        bullets=[
            "Compared KNN, RF, decision trees, SVM, and logistic regression; built and demoed a fraud detection web app.",
        ],
    )

    pdf.section("Skills")
    pdf.skill_line(
        "Technical:",
        "Python, Java, C++, PyTorch, TensorFlow, scikit-learn, Pandas, NumPy, OpenCV, SQL, Git, Linux, LaTeX, Streamlit",
    )
    pdf.skill_line(
        "Research:",
        "NLP & LLMs, RAG, RL, agentic frameworks, deep research, data mining, qualitative methods, computer vision",
    )
    pdf.skill_line("Languages:", "English, Vietnamese")

    pdf.section("Awards & Leadership")
    for item in [
        "Provost Honors - UC San Diego",
        "Machine Learning Specialization - Coursera",
        "Volunteer Youth Leader - Vietnamese Eucharistic Youth Movement (2022 - Present)",
        "Peer Mentor - UCSD Mentor Collective (2024)",
    ]:
        pdf.bullet(item)

    pdf.output(str(OUTPUT))
    print(f"Wrote {OUTPUT} ({len(pdf.pages)} page(s))")


if __name__ == "__main__":
    build()
