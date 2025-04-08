import streamlit as st
import pickle
import pandas as pd

# Load saved models
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('ordinal_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Location dictionary
location = {0: 'Abdalpur', 1: 'Adarsha Nagar', 2: 'Agarpara', 3: 'Airport', 4: 'Alipore', 5: 'Amtala', 6: 'Ariadaha', 7: 'Ashokgarh', 8: 'Aurobindo Park', 9: 'Badartala', 10: 'Baghajatin', 11: 'Baghbazar', 12: 'Bagmari', 13: 'Bagnan', 14: 'Bagpota', 15: 'Baguiati', 16: 'Baguihati', 17: 'Baishnabghata Patuli Township,', 18: 'Baithakkhana', 19: 'Ballygunge', 20: 'Bamangachhi', 21: 'Bamunpara', 22: 'Bangaon', 23: 'Bansdroni', 24: 'Bantala', 25: 'Barabazar Market', 26: 'Baranagar', 27: 'Barasat', 28: 'Barisha', 29: 'Barrackpore', 30: 'Baruipur', 31: 'Baruipur P', 32: 'Basirhat', 33: 'Behala', 34: 'Belgachia', 35: 'Belghoria', 36: 'Beliaghata', 37: 'Beniapukur', 38: 'Beniatola', 39: 'Berunanpukhuria', 40: 'Bhatenda', 41: 'Bhatpara', 42: 'Bhowanipore', 43: 'Bijoygarh', 44: 'Bira', 45: 'Birati', 46: 'Bishnupur', 47: 'Bow Barracks', 48: 'Bow Bazaar', 49: 'Bramhapur', 50: 'Budge Budge', 51: 'Champahati', 52: 'Chandpara', 53: 'Chinar Park', 54: 'Chitpur', 55: 'Chowbaga', 56: 'College Square', 57: 'Cossipore', 58: 'Dakshin Gobindopur', 59: 'Dakshineswar', 60: 'Dhakuria', 61: 'Diamond Harbour', 62: 'Doperia Village', 63: 'Dum Dum', 64: 'Dum Dum Cantonment', 65: 'Dunlop', 66: 'Duttapukur', 67: 'East Kolkata Township', 68: 'Elgin', 69: 'Entally', 70: 'Fatepur', 71: 'Ganguly Bagan', 72: 'Garden Reach', 73: 'Garfa', 74: 'Garia', 75: 'Gariahat', 76: 'Garulia', 77: 'Gobra', 78: 'Golf Green', 79: 'Habra', 80: 'Halisahar', 81: 'Haltu', 82: 'Hanspukuria', 83: 'Hedua', 84: 'Hridaypur', 85: 'Hussainpur', 86: 'Ichapur', 87: 'Jadavpur', 88: 'Jagatipota', 89: 'Jodhpur Park', 90: 'Joka', 91: 'Jorabagan', 92: 'Jorasanko', 93: 'Jugberia', 94: 'Kabardanga', 95: 'Kaikhali', 96: 'Kalagachhia', 97: 'Kalighat', 98: 'Kalikapur', 99: 'Kalyan Nagar', 100: 'Kalyani', 101: 'Kamalgazi', 102: 'Kamardanga', 103: 'Kamdahari', 104: 'Kanchrapara Loco', 105: 'Kankurgachi', 106: 'Kasba', 107: 'Kashipur', 108: 'Kazipara', 109: 'Keshtopur', 110: 'Khardah', 111: 'Khariberia', 112: 'Khidirpur', 113: 'Kokapur', 114: 'Kolkata', 115: 'Kolutolla', 116: 'Krishnanagar', 117: 'Kustia', 118: 'Lake Gardens', 119: 'Lake Town', 120: 'Machuabazar', 121: 'Madhyamgram', 122: 'Maheshtala', 123: 'Maidan', 124: 'Malancha Mahi Nagar', 125: 'Malickpur', 126: 'Maniktala', 127: 'Metiabruz', 128: 'Mohispota', 129: 'Mominpore', 130: 'Mukundapur', 131: 'Nabapally', 132: 'Naihati', 133: 'Naoabad', 134: 'Narayantala', 135: 'Narendrapur', 136: 'Natagarh', 137: 'Natunhat', 138: 'Nayabad', 139: 'Nazirabad', 140: 'Netaji Nagar', 141: 'New Alipore', 142: 'New Barrakpur', 143: 'New Town', 144: 'Nimta', 145: 'North Dum Dum', 146: 'Paikpara', 147: 'Pailan', 148: 'Palta', 149: 'Pancha Sayar', 150: 'Panchpota', 151: 'Panihati', 152: 'Pansila', 153: 'Park Street Area', 154: 'Paschim Barisha', 155: 'Paschim Putiary', 156: 'Patipukur', 157: 'Picnic Garden', 158: 'Purba Barisha', 159: 'Purba Putiary', 160: 'Raghunathpur', 161: 'Rahara', 162: 'Raja Bazar', 163: 'Rajabagan', 164: 'Rajarhat', 165: 'Rajpur', 166: 'Rajpur Sonarpur', 167: 'Ramchandrapur', 168: 'Rania', 169: 'Regent Park', 170: 'Ruiya', 171: 'Saha Para', 172: 'Salt Lake City', 173: 'Santoshpur', 174: 'Sarada Pally', 175: 'Sarsuna', 176: 'Sewli Telinipara', 177: 'Shobhabazar', 178: 'Shyambazar', 179: 'Shyamnagar', 180: 'Sinthi', 181: 'Sodepur', 182: 'South Dum Dum', 183: 'Sovabazar', 184: 'Srirampur', 185: 'Tagore Park', 186: 'Tala', 187: 'Talbanda', 188: 'Taltala', 189: 'Tangra', 190: 'Taratala', 191: 'Thakuranir Chak', 192: 'Thakurpukur', 193: 'Tiljala', 194: 'Tollygunge', 195: 'Topsia', 196: 'Ultadanga', 197: 'Uttarbhag', 198: 'VIP Nagar', 199: 'Vedic Village', 200: 'Ward No 113'}

location_list = list(location.values())

# App title and intro
st.set_page_config(page_title="Kolkata House Price Predictor")
st.title("🏙️ Kolkata House Price Prediction")
st.markdown("Estimate your property price based on **BHK**, **Location**, **Square Footage**, and **Price per Sq.Ft**.")

# User inputs
bhk = st.slider("Number of Bedrooms (BHK)", 1, 20, 3)
location_input = st.selectbox("Select Location", sorted(location_list))
total_sqft = st.number_input("Total Area (in Sq.Ft)", min_value=100.0, max_value=10000.0, value=1400.0, step=50.0)
price_per_sqft = st.number_input("Price per Sq.Ft (in ₹)", min_value=500.0, max_value=15000.0, value=3210.0, step=100.0)

# Predict button
if st.button("Predict Price"):
    # Prepare input
    input_df = pd.DataFrame([[bhk, location_input, total_sqft, price_per_sqft]], 
                            columns=['BHK', 'Location', 'Total_Sq.ft', 'Price_per_sq.ft'])

    # Encode and scale
    input_df['Location'] = encoder.transform(input_df[['Location']])
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]

    st.success(f"💰 Estimated House Price: ₹ {prediction:,.2f}")
    st.markdown("📍 *This is an estimate.*")
