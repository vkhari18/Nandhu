import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Nandhini", page_icon="❤️", layout="centered")

if "clicked_yes" not in st.session_state:
    st.session_state.clicked_yes = False

# -----------------------------
# Styling (UPDATED background)
# -----------------------------
st.markdown(
    """
    <style>
      /* Attractive background gradient */
      [data-testid="stAppViewContainer"]{
        background:
          radial-gradient(circle at 18% 12%, rgba(255, 0, 128, 0.22), transparent 42%),
          radial-gradient(circle at 82% 18%, rgba(255, 105, 180, 0.26), transparent 46%),
          radial-gradient(circle at 40% 88%, rgba(138, 43, 226, 0.20), transparent 52%),
          radial-gradient(circle at 92% 86%, rgba(255, 20, 147, 0.18), transparent 48%),
          linear-gradient(135deg, #fff0f7 0%, #ffe1f0 35%, #f4dcff 70%, #ffeaf6 100%);
      }

      [data-testid="stHeader"]{
        background: rgba(0,0,0,0);
      }

      .name-title{
        text-align:center;
        color:#ff1493;
        font-size:54px;
        font-weight:900;
        margin:14px 0 2px 0;
        font-family:Georgia, serif;
        text-shadow:3px 3px 6px rgba(255,20,147,0.20);
      }

      .title{
        text-align:center;
        color:#ff1493;
        font-size:40px;
        font-weight:800;
        margin:0 0 8px 0;
        text-shadow:2px 2px 4px rgba(255,20,147,0.20);
      }

      .subtitle{
        text-align:center;
        color:#c71585;
        font-size:18px;
        font-weight:700;
        margin:0 0 18px 0;
      }

      .love-message{
        text-align:center;
        color:#ff1493;
        font-size:34px;
        font-weight:900;
        margin:18px 0 10px 0;
        text-shadow:2px 2px 6px rgba(0,0,0,0.08);
      }

      .love-sub{
        text-align:center;
        color:#7a2c56;
        font-size:22px;
        font-weight:900;
        margin:0 0 18px 0;
      }

      .dialogue{
        text-align:center;
        color:#7a2c56;
        font-size:24px;
        line-height:1.7;
        margin:18px auto 22px auto;
        padding:18px 18px;
        background:rgba(255,255,255,0.86);
        border-radius:14px;
        max-width:720px;
        border-left:6px solid #ff1493;
        box-shadow:0 10px 25px rgba(0,0,0,0.10);
        backdrop-filter: blur(6px);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers
# -----------------------------
@st.cache_data(show_spinner=False)
def gif_to_data_url(gif_path: str) -> str:
    p = Path(gif_path)
    data = p.read_bytes()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:image/gif;base64,{b64}"

def show_gif(gif_path: str, width_px: int = 560):
    try:
        data_url = gif_to_data_url(gif_path)
        st.markdown(
            f"""
            <div style="text-align:center; margin:14px 0;">
              <img src="{data_url}"
                   style="max-width:{width_px}px; width:100%;
                          border-radius:14px;
                          box-shadow:0 10px 25px rgba(0,0,0,0.14);">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except Exception:
        st.error(f"GIF not found: {gif_path}")

def runaway_no_button_component(height: int = 360):
    html = f"""
    <div id="arena" style="
        position: relative;
        width: 100%;
        height: {height}px;
        background: transparent;
        overflow: hidden;
    ">
      <button id="noBtn" style="
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        padding: 10px 28px;
        border-radius: 999px;
        border: 0;
        background: rgba(255,255,255,0.78);
        color: #7a2c56;
        font-size: 16px;
        font-weight: 900;
        cursor: pointer;
        user-select: none;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        backdrop-filter: blur(6px);
      ">No</button>
    </div>

    <script>
      const arena = document.getElementById("arena");
      const btn = document.getElementById("noBtn");

      function placeRandom() {{
        const pad = 10;
        const a = arena.getBoundingClientRect();
        const b = btn.getBoundingClientRect();

        const maxX = a.width - b.width - pad;
        const maxY = a.height - b.height - pad;

        const x = pad + Math.random() * Math.max(1, maxX);
        const y = pad + Math.random() * Math.max(1, maxY);

        btn.style.left = x + "px";
        btn.style.top = y + "px";
        btn.style.transform = "none";
      }}

      function dist(ax, ay, bx, by) {{
        const dx = ax - bx;
        const dy = ay - by;
        return Math.sqrt(dx*dx + dy*dy);
      }}

      arena.addEventListener("mousemove", (e) => {{
        const a = arena.getBoundingClientRect();
        const b = btn.getBoundingClientRect();

        const mx = e.clientX - a.left;
        const my = e.clientY - a.top;

        const bx = (b.left - a.left) + b.width / 2;
        const by = (b.top - a.top) + b.height / 2;

        if (dist(mx, my, bx, by) < 120) {{
          placeRandom();
        }}
      }});

      btn.addEventListener("mouseenter", placeRandom);
      btn.addEventListener("mousedown", (e) => {{ e.preventDefault(); placeRandom(); }});
      btn.addEventListener("click", (e) => {{ e.preventDefault(); placeRandom(); }});

      placeRandom();
    </script>
    """
    components.html(html, height=height + 10)

# -----------------------------
# App UI
# -----------------------------
if not st.session_state.clicked_yes:
    st.markdown('<div class="name-title">Nandhini</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">Will You Be My Valentine?</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Choose your answer</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("YES", type="primary", use_container_width=True):
            st.session_state.clicked_yes = True
            st.rerun()

    runaway_no_button_component(height=380)

else:
    st.markdown('<div class="love-message">I LOVE YOU NANDHINI 💋</div>', unsafe_allow_html=True)
    st.markdown('<div class="love-sub">BEST DECISION EVER MADE 😘</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dialogue">
          "உன் கண்ணுல என் உலகம் இருக்கு,<br>
          உன் புன்னகையில் என் சந்தோஷம் இருக்கு"<br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_gif("love-proposal-ajith-kumar.gif")
    show_gif("ajithgifs-ajithkumar.gif")
    show_gif("gesture-kiss.gif")



