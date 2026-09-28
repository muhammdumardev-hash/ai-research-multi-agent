import time
from datetime import datetime

import streamlit as st

from crew import create_research_crew


# ---------------------------------------------------------------- page setup
st.set_page_config(
    page_title="Research Desk · AI Multi-Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------- styling
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Manrope:wght@400;500;600&display=swap');

:root {
    --bg: #F4F6FB;
    --surface: #FFFFFF;
    --ink: #101828;
    --muted: #667085;
    --line: #E4E7EF;
    --accent: #3D5AFE;
    --accent-soft: #E8ECFF;
    --ok: #12B76A;
}

html, body, [class*="css"], .stApp {
    font-family: 'Manrope', sans-serif;
    color: var(--ink);
}
.stApp { background: var(--bg); }

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.block-container { padding-top: 2.2rem; padding-bottom: 4rem; max-width: 1080px; }

h1, h2, h3, h4 { font-family: 'Sora', sans-serif; letter-spacing: -0.02em; color: var(--ink); }

/* ---- hero */
.hero {
    background: linear-gradient(135deg, #101828 0%, #1D2B64 100%);
    border-radius: 22px;
    padding: 2.6rem 2.6rem 2.4rem;
    margin-bottom: 1.6rem;
    color: #fff;
}
.hero h1 {
    color: #fff;
    font-size: 2.5rem;
    line-height: 1.15;
    margin: 0 0 .7rem 0;
    font-weight: 700;
}
.hero p {
    color: #C7D0F0;
    font-size: 1.05rem;
    max-width: 620px;
    margin: 0;
    line-height: 1.6;
}

/* ---- pipeline steps */
.pipeline {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: .8rem;
    margin: 0 0 1.6rem 0;
}
@media (max-width: 900px) { .pipeline { grid-template-columns: repeat(2, 1fr); } }
.step {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 1rem 1.1rem;
}
.step .icon { font-size: 1.4rem; }
.step .name { font-family: 'Sora', sans-serif; font-weight: 600; margin-top: .35rem; }
.step .desc { color: var(--muted); font-size: .88rem; margin-top: .15rem; }

/* ---- input */
div[data-testid="stTextInput"] div[data-baseweb="input"],
div[data-testid="stTextInput"] div[data-baseweb="base-input"] {
    background: #FFFFFF !important;
    border-radius: 12px !important;
}
div[data-testid="stTextInput"] div[data-baseweb="input"] {
    border: 1.5px solid var(--line) !important;
}
div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--accent-soft);
}
div[data-testid="stTextInput"] input {
    background: #FFFFFF !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    caret-color: #000000;
    border: none !important;
    box-shadow: none !important;
    padding: .85rem 1rem;
    font-size: 1.02rem;
}
div[data-testid="stTextInput"] input::placeholder {
    color: #667085 !important;
    -webkit-text-fill-color: #667085 !important;
    opacity: 1 !important;
}

/* ---- buttons */
.stButton > button, .stDownloadButton > button {
    border-radius: 11px;
    border: 1.5px solid var(--line);
    background: var(--surface);
    color: var(--ink);
    font-weight: 600;
    padding: .55rem 1.1rem;
    transition: border-color .15s, background .15s;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    border-color: var(--accent);
    color: var(--accent);
    background: var(--accent-soft);
}
.stButton > button[kind="primary"] {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
}
.stButton > button[kind="primary"]:hover {
    background: #2F48D6;
    border-color: #2F48D6;
    color: #fff;
}

/* ---- stats */
.stat {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: .9rem 1.1rem;
}
.stat .label { color: var(--muted); font-size: .82rem; }
.stat .value { font-family: 'Sora', sans-serif; font-size: 1.45rem; font-weight: 600; }

/* ---- report */
.report {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 2rem 2.4rem;
    line-height: 1.75;
}
.report h1, .report h2, .report h3 { margin-top: 1.4em; }

/* ---- sidebar */
section[data-testid="stSidebar"] { background: var(--surface); border-right: 1px solid var(--line); }
.hist-item { padding: .55rem .7rem; border-radius: 10px; font-size: .9rem; }
.hist-item small { color: var(--muted); display: block; }

/* ---- tabs */
button[data-baseweb="tab"] { font-weight: 600; }

/* ---- force a readable light look even when Streamlit/browser theme is dark */
.stApp, section[data-testid="stSidebar"] { color-scheme: light; background-color: var(--bg); }
section[data-testid="stSidebar"] { background-color: var(--surface) !important; }
.stApp p, .stApp label, .stApp li, .stApp span, .stApp h1, .stApp h2,
.stApp h3, .stApp h4, .stApp div[data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] * { color: var(--ink); }
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] *,
.stApp .step .desc, .stApp .stat .label { color: var(--muted) !important; }
.stApp .hero h1 { color: #fff !important; }
.stApp .hero p { color: #C7D0F0 !important; }
.stApp .stButton > button[kind="primary"],
.stApp .stButton > button[kind="primary"] * { color: #fff !important; }
.stApp .stButton > button:not([kind="primary"]) { background: var(--surface); }
.stApp div[data-testid="stTextInput"] input,
.stApp textarea { background: var(--surface) !important; color: var(--ink) !important; }
.stApp div[data-testid="stExpander"], .stApp details { background: var(--surface); border-color: var(--line); }
.stApp div[data-testid="stVerticalBlockBorderWrapper"] { background: var(--surface); }

@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------- state
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "history" not in st.session_state:
    st.session_state.history = []  # list of dicts: topic, report, seconds, time
if "active" not in st.session_state:
    st.session_state.active = None  # index into history

EXAMPLES = [
    "Impact of generative AI on education",
    "Future of renewable energy in Pakistan",
    "AI in early cancer detection",
    "Cybersecurity threats in 2026",
]


def set_topic(value: str):
    st.session_state.topic = value


def result_to_text(result) -> str:
    for attr in ("raw", "final_output"):
        value = getattr(result, attr, None)
        if isinstance(value, str) and value.strip():
            return value
    return str(result)


# ------------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### 🔬 Research Desk")
    st.caption("Four agents research, verify, analyze and write your report.")
    st.divider()

    st.markdown("**Past reports**")
    if not st.session_state.history:
        st.caption("Your finished reports will show up here.")
    else:
        for i in range(len(st.session_state.history) - 1, -1, -1):
            item = st.session_state.history[i]
            label = item["topic"] if len(item["topic"]) <= 34 else item["topic"][:32] + "…"
            if st.button(label, key=f"hist_{i}", use_container_width=True):
                st.session_state.active = i
            st.caption(f"{item['time']} · {item['seconds']:.0f}s")

        st.divider()
        if st.button("Clear history", use_container_width=True):
            st.session_state.history = []
            st.session_state.active = None
            st.rerun()

# ---------------------------------------------------------------------- hero
st.markdown(
    """
<div class="hero">
    <h1 style="color:#FFFFFF !important; -webkit-text-fill-color:#FFFFFF;">Turn any topic into a<br>verified research report.</h1>
    <p style="color:#C7D0F0 !important; -webkit-text-fill-color:#C7D0F0;">Type a topic and a team of AI agents will gather sources, check the facts,
    analyze the findings and write the final report for you.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="pipeline">
    <div class="step"><div class="icon">🔎</div><div class="name">Research</div>
        <div class="desc">Collects information on your topic</div></div>
    <div class="step"><div class="icon">✅</div><div class="name">Verify</div>
        <div class="desc">Checks claims and sources</div></div>
    <div class="step"><div class="icon">📊</div><div class="name">Analyze</div>
        <div class="desc">Finds patterns and key insights</div></div>
    <div class="step"><div class="icon">✍️</div><div class="name">Write</div>
        <div class="desc">Produces the final report</div></div>
</div>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------- input
st.text_input(
    "Research topic",
    key="topic",
    placeholder="e.g. Impact of generative AI on education",
    label_visibility="collapsed",
)

st.caption("Try one of these:")
cols = st.columns(len(EXAMPLES))
for col, example in zip(cols, EXAMPLES):
    col.button(example, key=f"ex_{example}", on_click=set_topic, args=(example,), use_container_width=True)

start = st.button("Start research", type="primary")

# ----------------------------------------------------------------------- run
if start:
    topic = st.session_state.topic.strip()
    if not topic:
        st.warning("Enter a research topic first.")
        st.stop()

    started = time.time()
    try:
        with st.status("Research team is working…", expanded=True) as status:
            st.write("🔎 Researcher is gathering information")
            st.write("✅ Verifier, Analyst and Writer will follow in order")
            st.caption("This usually takes a few minutes. Keep this tab open.")

            crew = create_research_crew(topic)
            result = crew.kickoff()

            status.update(label="Research complete", state="complete", expanded=False)

        seconds = time.time() - started
        st.session_state.history.append(
            {
                "topic": topic,
                "report": result_to_text(result),
                "seconds": seconds,
                "time": datetime.now().strftime("%d %b, %H:%M"),
            }
        )
        st.session_state.active = len(st.session_state.history) - 1
        st.toast("Report is ready", icon="✅")

    except Exception as e:
        st.error(f"Research failed: {e}")
        st.info("Check your API keys and internet connection, then try again.")

# ------------------------------------------------------------------- results
active = st.session_state.active
if active is not None and active < len(st.session_state.history):
    item = st.session_state.history[active]
    report = item["report"]
    words = len(report.split())
    read_min = max(1, round(words / 220))

    st.markdown("---")
    st.markdown(f"## {item['topic']}")

    c1, c2, c3 = st.columns(3)
    for col, label, value in (
        (c1, "Words", f"{words:,}"),
        (c2, "Reading time", f"{read_min} min"),
        (c3, "Time taken", f"{item['seconds']:.0f} s"),
    ):
        col.markdown(
            f'<div class="stat"><div class="label">{label}</div><div class="value">{value}</div></div>',
            unsafe_allow_html=True,
        )

    st.write("")
    tab_report, tab_raw = st.tabs(["Report", "Plain text"])

    with tab_report:
        with st.container(border=True):
            st.markdown(report)

    with tab_raw:
        st.text_area("Copy the text", report, height=420, label_visibility="collapsed")

    file_name = "_".join(item["topic"].lower().split())[:50] or "report"
    d1, d2, _ = st.columns([1, 1, 3])
    d1.download_button(
        "Download .md",
        report,
        file_name=f"{file_name}.md",
        mime="text/markdown",
        use_container_width=True,
    )
    d2.download_button(
        "Download .txt",
        report,
        file_name=f"{file_name}.txt",
        mime="text/plain",
        use_container_width=True,
    )
