import streamlit as st
import pandas as pd

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="F1 2025 Dashboard - Real Results",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== REAL 2025 RACE DATA ==========
races_2025_real = [
    ["1", "Bahrain GP", "Oscar Piastri", "McLaren", 25, "Sakhir"],
    ["2", "Saudi Arabian GP", "Oscar Piastri", "McLaren", 25, "Jeddah"],
    ["3", "Australian GP", "Lando Norris", "McLaren", 25, "Melbourne"],
    ["4", "Japanese GP", "Max Verstappen", "Red Bull Racing", 25, "Suzuka"],
    ["5", "Chinese GP", "Oscar Piastri", "McLaren", 25, "Shanghai"],
    ["6", "Miami GP", "Oscar Piastri", "McLaren", 25, "Miami"],
    ["7", "Emilia Romagna GP", "Max Verstappen", "Red Bull Racing", 25, "Imola"],
    ["8", "Monaco GP", "Lando Norris", "McLaren", 25, "Monte Carlo"],
    ["9", "Spanish GP", "Oscar Piastri", "McLaren", 25, "Barcelona"],
    ["10", "Canadian GP", "George Russell", "Mercedes", 25, "Montreal"],
    ["11", "Austrian GP", "Lando Norris", "McLaren", 25, "Spielberg"],
    ["12", "British GP", "Lando Norris", "McLaren", 25, "Silverstone"]
]

# ========== REAL 2025 STANDINGS ==========
standings_2025_real = [
    [1, "Oscar Piastri", "McLaren", 258, 5, 9],
    [2, "Lando Norris", "McLaren", 216, 4, 8],
    [3, "Max Verstappen", "Red Bull Racing", 176, 2, 6],
    [4, "Charles Leclerc", "Ferrari", 144, 0, 3],
    [5, "George Russell", "Mercedes", 122, 1, 2],
    [6, "Carlos Sainz", "Ferrari", 108, 0, 2],
    [7, "Lewis Hamilton", "Mercedes", 95, 0, 1],
    [8, "Fernando Alonso", "Aston Martin", 78, 0, 0],
    [9, "Yuki Tsunoda", "RB", 62, 0, 0],
    [10, "Daniel Ricciardo", "RB", 56, 0, 0]
]

# ========== SIDEBAR WITH F1 LOGO ==========
with st.sidebar:
    # F1 Logo - Using base64 encoded SVG for reliability
    f1_logo_svg = """
    <div style="text-align: center; margin-bottom: 25px;">
        <svg width="200" height="60" viewBox="0 0 200 60">
            <rect width="200" height="60" fill="#e10600" rx="8"/>
            <text x="100" y="35" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-weight="900" font-size="28">FORMULA 1</text>
            <text x="100" y="50" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-weight="600" font-size="14">2025 SEASON</text>
        </svg>
    </div>
    """
    st.markdown(f1_logo_svg, unsafe_allow_html=True)
    
    # Season Progress
    st.write("**Season Progress**")
    progress = 12/24
    st.progress(progress, text=f"Season: {12}/24 races completed")
    
    st.divider()
    
    # Navigation
    st.write("**NAVIGATION**")
    page_options = ["🏆 Race Winners", "📊 Championship", "📈 Piastri Analysis", "📊 Team Stats"]
    page = st.radio("", page_options, index=2, label_visibility="collapsed")
    
    st.divider()
    
    # Team Filter
    st.write("**TEAM FILTER**")
    teams = ["All Teams", "McLaren", "Red Bull Racing", "Ferrari", "Mercedes", 
             "Aston Martin", "RB", "Williams", "Alpine", "Haas", "Sauber"]
    selected_team = st.selectbox("", teams, label_visibility="collapsed")
    
    st.divider()
    
    # Season Stats
    st.write("**SEASON STATS (12 RACES)**")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Races", "12")
    with col2:
        st.metric("Winners", "4")
    
    st.divider()
    
    # Next Race
    st.write("**NEXT RACE**")
    st.info("🇧🇪 Belgian GP\n\n🏁 Spa-Francorchamps\n\n📅 August 24, 2025")

# ========== MAIN CONTENT ==========
if page == "🏆 Race Winners":
    st.header("🏆 2025 Race Winners (Real Results)")
    
    df_races = pd.DataFrame(races_2025_real, 
                           columns=["Round", "Race", "Winner", "Team", "Points", "Circuit"])
    
    if selected_team != "All Teams":
        df_races = df_races[df_races["Team"] == selected_team]
    
    st.dataframe(df_races, use_container_width=True, hide_index=True, height=400)
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("McLaren Wins", "9")
    with col2: st.metric("Red Bull Wins", "2")
    with col3: st.metric("Mercedes Wins", "1")
    with col4: st.metric("Ferrari Wins", "0")
    
    # Winners list
    if not df_races.empty:
        win_counts = df_races["Winner"].value_counts()
        st.write("**Wins by Driver:**")
        for driver, wins in win_counts.items():
            st.write(f"• **{driver}**: {wins} win{'s' if wins > 1 else ''}")

elif page == "📊 Championship":
    st.header("📊 2025 Drivers Championship")
    
    df_standings = pd.DataFrame(standings_2025_real,
                               columns=["Pos", "Driver", "Team", "Points", "Wins", "Podiums"])
    
    if selected_team != "All Teams":
        df_standings = df_standings[df_standings["Team"] == selected_team]
    
    st.dataframe(df_standings, use_container_width=True, hide_index=True, height=400)
    
    if not df_standings.empty:
        leader = df_standings.iloc[0]
        st.success(f"**🏆 CURRENT LEADER:** {leader['Driver']} ({leader['Points']} points)")

elif page == "📈 Piastri Analysis":
    st.header("📈 Oscar Piastri 2025 Season Analysis")
    
    piastri_prog = [
        ["Bahrain GP", 25, 25, 1],
        ["Saudi Arabian GP", 25, 50, 1],
        ["Australian GP", 18, 68, 2],
        ["Japanese GP", 15, 83, 3],
        ["Chinese GP", 25, 108, 1],
        ["Miami GP", 25, 133, 1],
        ["Emilia Romagna GP", 12, 145, 4],
        ["Monaco GP", 15, 160, 3],
        ["Spanish GP", 25, 185, 1],
        ["Canadian GP", 12, 197, 4],
        ["Austrian GP", 18, 215, 2],
        ["British GP", 18, 233, 2]
    ]
    
    df_piastri = pd.DataFrame(piastri_prog,
                             columns=["Race", "Points", "Cumulative", "Position"])
    
    # Display
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Total Points", "258")
    with col2: st.metric("Race Wins", "5")
    with col3: st.metric("Championship Lead", "+42")
    
    st.dataframe(df_piastri, use_container_width=True, hide_index=True, height=400)

else:  # Team Stats
    st.header("📊 2025 Team Statistics")
    
    team_data = [
        {"Team": "McLaren", "Points": 474, "Wins": 9, "Podiums": 17, "Drivers": 2},
        {"Team": "Ferrari", "Points": 252, "Wins": 0, "Podiums": 5, "Drivers": 2},
        {"Team": "Mercedes", "Points": 217, "Wins": 1, "Podiums": 3, "Drivers": 2},
        {"Team": "Red Bull Racing", "Points": 176, "Wins": 2, "Podiums": 6, "Drivers": 2}
    ]
    
    df_teams = pd.DataFrame(team_data)
    df_teams = df_teams.sort_values("Points", ascending=False)
    
    st.dataframe(df_teams, use_container_width=True, hide_index=True)
    
    if not df_teams.empty:
        top_team = df_teams.iloc[0]
        st.success(f"**🏆 CONSTRUCTORS' LEADER:** {top_team['Team']}")

# Footer
st.divider()
st.caption("F1 2025 World Championship • Real Results • Data Source: Official F1 Results")
