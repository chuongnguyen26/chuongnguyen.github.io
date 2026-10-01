#!/usr/bin/env python3
"""Generate Chuong_Nguyen_CV.pdf — full academic CV (the resume is the short version)."""

from fpdf.enums import XPos, YPos

from build_resume import BODY, LINE, NAME, ROOT, SMALL, ResumePDF

OUTPUT = ROOT / "Chuong_Nguyen_CV.pdf"
ME = "Chuong Nguyen"


def subheading(pdf: ResumePDF, text: str):
    pdf.ln(3)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "BI", BODY)
    pdf.cell(0, LINE, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)


def build():
    pdf = ResumePDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", NAME)
    pdf.cell(0, 18, ME, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", SMALL)
    pdf.multi_cell(
        0,
        LINE,
        "chuongn194@gmail.com | chn021@ucsd.edu | chuongnguyen26.github.io/chuongnguyen.github.io\n"
        "github.com/chuongnguyen26 | linkedin.com/in/chuong-nguyen-profile",
    )
    pdf.ln(4)

    pdf.section("Research Interests")
    pdf.text_line(
        "Large language models; LLM reasoning through human-inspired approaches; agentic frameworks; "
        "data mining; LLM-assisted qualitative data analysis; context awareness, agent learning and "
        "navigation, and forecasting."
    )

    pdf.section("Education")
    pdf.entry(
        "University of California, San Diego",
        "Sep 2022 - Jun 2026",
        subtitle="B.S. in Computer Science, Department of Computer Science & Engineering | GPA: 3.803",
    )

    pdf.section("Publications")
    pdf.text_line("* denotes co-first authors.", "I", SMALL)

    subheading(pdf, "Conference Papers")
    for year, authors, title, venue in [
        (
            "2026",
            "Xinyu Pi*, Qisen Yang*, Chuong Nguyen*, Hua Shen",
            "Position: Bridge Human Interpretation and Machine Representation With Explicit "
            "Specification For Qualitative Data Analysis In LLM Era",
            "International Conference on Machine Learning (ICML), Position Paper Track, 2026. arXiv:2601.11739",
        ),
        (
            "2026",
            "Taggert Smith*, Chuong Nguyen*, Qisen Yang, Oishani Bandopadhyay, Yaru Su, "
            "Nadia Polikarpova, Xinyu Pi",
            "QualAlign: Benchmarking Automated Qualitative Coding Against Human Schemas",
            "Conference on Language Modeling (COLM), 2026. openreview.net/forum?id=FaPyCwiiTo",
        ),
        (
            "2024",
            "Andrew Smithwick*, Chuong Nguyen*, Emily Gorial*, Natasha Tran*, A. M. Flores, "
            "Imani N. S. Munyaka",
            '"Parent seeking Roblox Safety Help": Comparing Parental Roblox Concerns to Roblox Offerings',
            "IEEE International Symposium on Technology and Society (ISTAS), pp. 1-9, 2024",
        ),
    ]:
        pdf.publication(year, authors, title, venue, name=ME)

    subheading(pdf, "Preprints")
    pdf.publication(
        "2025",
        "Xinyu Pi*, Qisen Yang*, Chuong Nguyen*",
        "LOGOS: LLM-driven End-to-End Grounded Theory Development and Schema Induction "
        "for Qualitative Research",
        "arXiv preprint arXiv:2509.24294, 2025",
        name=ME,
    )

    pdf.section("Current Projects")
    for item in [
        "Episteme: deep research system (manuscript in preparation).",
        "Coreference resolution (in progress).",
    ]:
        pdf.bullet(item)

    pdf.section("Presentations")
    for item in [
        "Poster: QualAlign: Benchmarking Automated Qualitative Coding Against Human Schemas. "
        "COLM 2026, San Francisco, CA, Oct 2026.",
        '"Parent seeking Roblox Safety Help". Early Research Scholars Program Symposium, UC San Diego, 2024.',
        "Credit Card Fraud Detector. ACM AI Symposium, UC San Diego, 2023.",
    ]:
        pdf.bullet(item)

    pdf.section("Research Experience")
    pdf.entry(
        "Research Assistant, Prof. Zhiting Hu's Group - HDSI, UC San Diego",
        "Apr 2025 - Present",
        subtitle="Mentors: Xinyu (Frederick) Pi and Qiyue Gao (PhD students)",
        bullets=[
            "Conduct research on large language models, agentic frameworks, and data mining for qualitative "
            "research, including grounded theory development, schema induction, and human-aligned reasoning.",
            "Fine-tuned LLMs with SFT and GRPO; explored test-time scaling and process reward models.",
            "Co-first author on an ICML 2026 position paper, a COLM 2026 paper (QualAlign), and the LOGOS preprint.",
        ],
    )
    pdf.entry(
        "Research Assistant, Ujima Lab - UC San Diego",
        "Sep 2023 - Oct 2024",
        subtitle="Advisor: Prof. Imani Munyaka",
        bullets=[
            "Beauty Filter: analyzed facial enhancements from three filter applications (Snatched, Blochi Gora, "
            "Baby Girl) to investigate cultural biases in appearance modification; migrated the facial landmark "
            "analysis pipeline to a remote server for parallel processing at scale.",
            "Smart Mirror: implemented DeepFace and Retina for facial recognition and racial classification on a "
            "Raspberry Pi smart mirror, delivering real-time analysis for a public art installation on racial bias.",
            'Roblox Safety: co-first author on "Parent seeking Roblox Safety Help" (IEEE ISTAS 2024).',
        ],
    )
    pdf.entry(
        "Early Research Scholars Program (ERSP) - UC San Diego",
        "Sep 2023 - Jun 2024",
        bullets=[
            "Conducted topic modeling on 10,000+ Reddit posts and surveyed 100 participants to identify four "
            "primary parental concerns on Roblox; proposed actionable platform-safety recommendations.",
            "Built a hate-crime news pipeline with SerpAPI, NewsPlease, DBSCAN, MeanShift, and the OpenAI API.",
        ],
    )

    pdf.section("Project Experience")
    pdf.entry(
        "Software Developer, Zooseeker",
        "Apr 2024 - Jun 2024",
        bullets=[
            "Designed and implemented the database schema for a zoo navigation Android application.",
            "Revamped the Android UI and maintained project documentation for the development team.",
        ],
    )
    pdf.entry(
        "ACM AI - UC San Diego",
        "Oct 2022 - Jan 2023",
        subtitle="Credit Card Fraud Detector",
        bullets=[
            "Compared KNN, Random Forest, Decision Tree, SVM, and Logistic Regression for fraud detection.",
            "Built and presented a fraud detection web application at the ACM AI symposium.",
        ],
    )

    pdf.section("Teaching & Mentoring")
    pdf.entry("Peer Mentor, UCSD Mentor Collective", "2024")

    pdf.section("Honors & Awards")
    for item in [
        "Provost Honors - UC San Diego",
        "Machine Learning Specialization - Coursera",
    ]:
        pdf.bullet(item)

    pdf.section("Leadership & Service")
    pdf.entry(
        "Volunteer Youth Leader, Vietnamese Eucharistic Youth Movement",
        "2022 - Present",
        bullets=["Teach and mentor young children in the youth program."],
    )

    pdf.section("Skills")
    pdf.skill_line("Programming:", "Python, Java, C++, SQL")
    pdf.skill_line(
        "ML & Data:",
        "PyTorch, TensorFlow, scikit-learn, Pandas, NumPy, OpenCV, Streamlit",
    )
    pdf.skill_line(
        "Research:",
        "NLP & LLMs, LLM fine-tuning (SFT, GRPO), RAG, reinforcement learning, agentic frameworks, "
        "data mining, topic modeling, qualitative methods, computer vision",
    )
    pdf.skill_line("Tools:", "Git, Linux, LaTeX")
    pdf.skill_line("Languages:", "English, Vietnamese")

    pdf.output(str(OUTPUT))
    print(f"Wrote {OUTPUT} ({len(pdf.pages)} page(s))")


if __name__ == "__main__":
    build()
