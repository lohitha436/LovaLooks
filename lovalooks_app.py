import streamlit as st
import random

# --- Streamlit Page Config (MUST be first command) ---
st.set_page_config(page_title="LovaLooks - Outfit Advisor", page_icon="🧥")

# --- Header ---
st.title("🧥 LovaLooks - Outfit Advisor")
st.markdown("Smarter outfit suggestions, tailored just for you!")

# --- Sidebar Inputs ---
st.sidebar.header("📝 Your Preferences")
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Non-Binary"])
venue = st.sidebar.selectbox("Venue", ["Beach", "Office", "Restaurant", "Park", "College"])
purpose = st.sidebar.selectbox("Purpose", ["Casual", "Formal", "Party", "Date"])
time_of_day = st.sidebar.radio("Time of Day", ["Day", "Night"])
season = st.sidebar.selectbox("Season", ["Summer", "Winter", "Rainy", "Spring"])
age_group = st.sidebar.selectbox("Age Group", ["Teen (13-19)", "Young Adult (20-35)", "Adult (36-55)", "Senior (55+)"])

if st.sidebar.button("Suggest Outfit"):  # Button for triggering result
    # --- Outfit Suggestions DB ---
    outfit_db = {
        "Female": {
            "Beach": {"Day": ["👗 Pastel sundress", "🩱 Flowy skirt with crop top"], "Night": ["👚 Maxi dress", "🧘 Boho pants with tank top"]},
            "Office": {"Day": ["👔 Blazer with trousers", "👩‍💼 Formal dress"], "Night": ["👗 Button shirt and pencil skirt"]},
            "Restaurant": {"Day": ["🧥 Wrap dress", "👗 Floral co-ord set"], "Night": ["👘 Satin blouse and trousers", "👗 Midi dress"]},
            "College": {"Day": ["👖 Jeans with pastel tee", "👚 Casual shirt with skirt"], "Night": ["🧥 Hoodie and joggers"]},
            "Park": {"Day": ["🩳 Dungaree with tee", "👕 Loose shirt and shorts"], "Night": ["🧥 Cardigan over maxi dress"]},
        },
        "Male": {
            "Beach": {"Day": ["👕 Oversized tee and shorts", "👔 Printed shirt with linen pants"], "Night": ["👕 Half-sleeve shirt and cargos"]},
            "Office": {"Day": ["👔 Formal shirt and trousers", "🧥 Blazer set"], "Night": ["👕 Collared shirt and chinos"]},
            "Restaurant": {"Day": ["👔 Linen shirt and jeans"], "Night": ["👕 Dark shirt and tapered pants"]},
            "College": {"Day": ["👕 Graphic tee and jeans", "👔 Checked shirt with cargos"], "Night": ["🧥 Bomber jacket look"]},
            "Park": {"Day": ["🧘 Athleisure set", "👕 Cotton shirt and shorts"], "Night": ["🧥 Hoodie and joggers"]},
        },
        "Non-Binary": {
            "Beach": {"Day": ["👕 Open shirt with tank and shorts", "🧥 Kaftan"], "Night": ["🧘 Boho pants and mesh top"]},
            "Office": {"Day": ["🧥 Relaxed suit", "🧥 Long coat with slacks"], "Night": ["👔 Chic minimal shirt and trousers"]},
            "Restaurant": {"Day": ["👗 Jumpsuit", "🧥 Vest and palazzos"], "Night": ["🧥 Layered flowy outfit"]},
            "College": {"Day": ["👖 Loose pants and tee", "👕 Denim co-ord"], "Night": ["🧥 Oversized hoodie"]},
            "Park": {"Day": ["🩳 Dungarees", "👕 Oversized top"], "Night": ["🧥 Cropped hoodie and pants"]},
        }
    }

    # --- Color Tone Logic ---
    tone_suggestions = {
        "Summer": "Pastel",
        "Winter": "Dark",
        "Spring": "Coral",
        "Rainy": "Earthy",
    }
    suggested_tone = tone_suggestions.get(season, "Neutral")

    # --- Fetch Outfit Suggestion ---
    selected_outfit = random.choice(outfit_db[gender][venue][time_of_day])

    # --- Display Result ---
    st.subheader("👗 Suggested Outfit")
    st.markdown(f"You could try: **{selected_outfit}** in **{suggested_tone.lower()} tones** for a {purpose.lower()} look in {season.lower()}.")

    # --- Fashion Fact ---
    fashion_facts = [
        "Wearing pastel shades in summer helps reflect sunlight and stay cool.",
        "Layering is key in transitional seasons like spring and fall!",
        "Accessories like scarves or belts can transform any outfit.",
        "Monochrome outfits make you appear taller and more put-together.",
        "Oversized fits are trending across all genders!",
    ]
    st.info("💡 " + random.choice(fashion_facts))
else:
    st.markdown("<p style='text-align:center;'>Choose your preferences from the sidebar and click 'Suggest Outfit' to get started! 🎯</p>", unsafe_allow_html=True)
