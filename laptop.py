
import streamlit as st
import sklearn
import streamlit as st
import qrcode
import tempfile
from PIL import Image

# Title of the app
st.title("Laptop Budget Prediction for Students/Working Professionals")
st.subheader("Confused in budget for your ideal laptop? It's all for you!")


# Initializing dictionaries for various labels
brand_encoding_dict = {'Acer': 0,
        'Alurin': 1,
        'Apple': 2,
        'Asus': 3,
        'Deep Gaming': 4,
        'Dell': 5,
        'Denver': 6,
        'Dynabook Toshiba': 7,
        'Gigabyte': 8,
        'HP': 9,
        'Innjoo': 10,
        'Jetwing': 11,
        'LG': 12,
        'Lenovo': 13,
        'MSI': 14,
        'Medion': 15,
        'Microsoft': 16,
        'Millenium': 17,
        'PcCom': 18,
        'Primux': 19,
        'Prixton': 20,
        'Razer': 21,
        'Realme': 22,
        'Samsung': 23,
        'Thomson': 24,
        'Toshiba': 25,
        'Vant': 26}

model_encoding_dict = {'100e': 0,
        '100w': 1,
        '14S': 2,
        '14w': 3,
        '15S': 4,
        '15U70N': 5,
        '17': 6,
        '250': 7,
        '255': 8,
        '300w': 9,
        '470': 10,
        'A7': 11,
        'AURELION': 12,
        'AZIR': 13,
        'Aero': 14,
        'Akoya': 15,
        'Alpha': 16,
        'Alurin': 17,
        'Aorus': 18,
        'Aspire': 19,
        'BR': 20,
        'Beast': 21,
        'Blade': 22,
        'Book': 23,
        'Book Prime': 24,
        'Bravo': 25,
        'Chromebook': 26,
        'Classmate Pro': 27,
        'ConceptD': 28,
        'Creator': 29,
        'Crosshair': 30,
        'Cyborg': 31,
        'Delta': 32,
        'Deputy': 33,
        'E410': 34,
        'E510': 35,
        'Edge': 36,
        'Electronics': 37,
        'EliteBook': 38,
        'Enduro': 39,
        'Envy': 40,
        'Erazer': 41,
        'ExpertBook': 42,
        'Extensa': 43,
        'F415': 44,
        'F415EA': 45,
        'F515': 46,
        'Flex': 47,
        'Flex Advance': 48,
        'G5': 49,
        'G7': 50,
        'GL65': 51,
        'GL75': 52,
        'Galaxy Book': 53,
        'Go': 54,
        'Gram': 55,
        'IdeaPad': 56,
        'Ioxbook': 57,
        'Katana': 58,
        'LOQ': 59,
        'Latitude': 60,
        'Legion': 61,
        'Leopard': 62,
        'M515': 63,
        'M515UA': 64,
        'MacBook Air': 65,
        'MacBook Pro': 66,
        'Macbook': 67,
        'Modern': 68,
        'Moove': 69,
        'N1510': 70,
        'Neo': 71,
        'Netbook Pro': 72,
        'Nitro': 73,
        'Notebook': 74,
        'Nubian': 75,
        'Omen': 76,
        'P1411': 77,
        'P1511': 78,
        'Pavilion': 79,
        'Portégé': 80,
        'Precision': 81,
        'Predator': 82,
        'Prestige': 83,
        'ProArt': 84,
        'ProBook': 85,
        'Pulse': 86,
        'ROG': 87,
        'Raider': 88,
        'Revolt': 89,
        'Satellite Pro': 90,
        'Spectre': 91,
        'Stealth': 92,
        'Summit': 93,
        'Surface Go': 94,
        'Surface Laptop': 95,
        'Surface Pro': 96,
        'Swift': 97,
        'TUF': 98,
        'Tecra': 99,
        'Thin': 100,
        'ThinkBook': 101,
        'ThinkPad': 102,
        'Titan': 103,
        'TravelMate': 104,
        'U4': 105,
        'Ultra': 106,
        'V14': 107,
        'V15': 108,
        'V17': 109,
        'V330': 110,
        'Vector': 111,
        'Victus': 112,
        'VivoBook': 113,
        'Voom': 114,
        'Vostro': 115,
        'WS63': 116,
        'XPS': 117,
        'Yoga': 118,
        'Zbook': 119,
        'ZenBook': 120}

cpu_encoding_dict = {'AMD 3015Ce': 0,
        'AMD 3015e': 1,
        'AMD 3020e': 2,
        'AMD Athlon': 3,
        'AMD Radeon 5': 4,
        'AMD Radeon 9': 5,
        'AMD Ryzen 3': 6,
        'AMD Ryzen 5': 7,
        'AMD Ryzen 7': 8,
        'AMD Ryzen 9': 9,
        'Apple M1': 10,
        'Apple M1 Pro': 11,
        'Apple M2': 12,
        'Apple M2 Pro': 13,
        'Intel Celeron': 14,
        'Intel Core M3': 15,
        'Intel Core i3': 16,
        'Intel Core i5': 17,
        'Intel Core i7': 18,
        'Intel Core i9': 19,
        'Intel Evo Core i5': 20,
        'Intel Evo Core i7': 21,
        'Intel Evo Core i9': 22,
        'Intel Pentium': 23,
        'Mediatek MT8183': 24,
        'Microsoft SQ1': 25,
        'Qualcomm Snapdragon 7': 26,
        'Qualcomm Snapdragon 8': 27}

gpu_encoding_dict = {'610 M': 0,
        'A 370M': 1,
        'A 730M': 2,
        'GTX 1050': 3,
        'GTX 1070': 4,
        'GTX 1650': 5,
        'GTX 1660': 6,
        'MX 130': 7,
        'MX 330': 8,
        'MX 450': 9,
        'MX 550': 10,
        'P 500': 11,
        'RTX 2050': 12,
        'RTX 2060': 13,
        'RTX 2070': 14,
        'RTX 2080': 15,
        'RTX 3000': 16,
        'RTX 3050': 17,
        'RTX 3060': 18,
        'RTX 3070': 19,
        'RTX 3080': 20,
        'RTX 4050': 21,
        'RTX 4060': 22,
        'RTX 4070': 23,
        'RTX 4080': 24,
        'RTX 4090': 25,
        'RTX A1000': 26,
        'RTX A2000': 27,
        'RTX A3000': 28,
        'RTX A5500': 29,
        'RX 6500M': 30,
        'RX 6700M': 31,
        'RX 6800S': 32,
        'RX 7600S': 33,
        'Radeon Pro 5300M': 34,
        'Radeon Pro 5500M': 35,
        'Radeon Pro RX 560X': 36,
        'Radeon RX 6600M': 37,
        'T 1000': 38,
        'T 1200': 39,
        'T 2000': 40,
        'T 500': 41,
        'T 550': 42,
        'T 600': 43}

touch_encoding_dict = {'No': 0, 'Yes': 1}

storage_encoding_dict = {'SSD': 0, 'eMMC': 1}


# Define options for user input

brands = ['Acer',
        'Alurin',
        'Apple',
        'Asus',
        'Deep Gaming',
        'Dell',
        'Denver',
        'Dynabook Toshiba',
        'Gigabyte',
        'HP',
        'Innjoo',
        'Jetwing',
        'LG',
        'Lenovo',
        'MSI',
        'Medion',
        'Microsoft',
        'Millenium',
        'PcCom',
        'Primux',
        'Prixton',
        'Razer',
        'Realme',
        'Samsung',
        'Thomson',
        'Toshiba',
        'Vant']
models = ['100e',
        '100w',
        '14S',
        '14w',
        '15S',
        '15U70N',
        '17',
        '250',
        '255',
        '300w',
        '470',
        'A7',
        'AURELION',
        'AZIR',
        'Aero',
        'Akoya',
        'Alpha',
        'Alurin',
        'Aorus',
        'Aspire',
        'BR',
        'Beast',
        'Blade',
        'Book',
        'Book Prime',
        'Bravo',
        'Chromebook',
        'Classmate Pro',
        'ConceptD',
        'Creator',
        'Crosshair',
        'Cyborg',
        'Delta',
        'Deputy',
        'E410',
        'E510',
        'Edge',
        'Electronics',
        'EliteBook',
        'Enduro',
        'Envy',
        'Erazer',
        'ExpertBook',
        'Extensa',
        'F415',
        'F415EA',
        'F515',
        'Flex',
        'Flex Advance',
        'G5',
        'G7',
        'GL65',
        'GL75',
        'Galaxy Book',
        'Go',
        'Gram',
        'IdeaPad',
        'Ioxbook',
        'Katana',
        'LOQ',
        'Latitude',
        'Legion',
        'Leopard',
        'M515',
        'M515UA',
        'MacBook Air',
        'MacBook Pro',
        'Macbook',
        'Modern',
        'Moove',
        'N1510',
        'Neo',
        'Netbook Pro',
        'Nitro',
        'Notebook',
        'Nubian',
        'Omen',
        'P1411',
        'P1511',
        'Pavilion',
        'Portégé',
        'Precision',
        'Predator',
        'Prestige',
        'ProArt',
        'ProBook',
        'Pulse',
        'ROG',
        'Raider',
        'Revolt',
        'Satellite Pro',
        'Spectre',
        'Stealth',
        'Summit',
        'Surface Go',
        'Surface Laptop',
        'Surface Pro',
        'Swift',
        'TUF',
        'Tecra',
        'Thin',
        'ThinkBook',
        'ThinkPad',
        'Titan',
        'TravelMate',
        'U4',
        'Ultra',
        'V14',
        'V15',
        'V17',
        'V330',
        'Vector',
        'Victus',
        'VivoBook',
        'Voom',
        'Vostro',
        'WS63',
        'XPS',
        'Yoga',
        'Zbook',
        'ZenBook']

cpus = ['AMD 3015Ce',
        'AMD 3015e',
        'AMD 3020e',
        'AMD Athlon',
        'AMD Radeon 5',
        'AMD Radeon 9',
        'AMD Ryzen 3',
        'AMD Ryzen 5',
        'AMD Ryzen 7',
        'AMD Ryzen 9',
        'Apple M1',
        'Apple M1 Pro',
        'Apple M2',
        'Apple M2 Pro',
        'Intel Celeron',
        'Intel Core M3',
        'Intel Core i3',
        'Intel Core i5',
        'Intel Core i7',
        'Intel Core i9',
        'Intel Evo Core i5',
        'Intel Evo Core i7',
        'Intel Evo Core i9',
        'Intel Pentium',
        'Mediatek MT8183',
        'Microsoft SQ1',
        'Qualcomm Snapdragon 7',
        'Qualcomm Snapdragon 8']

ram_options = [16,8,20,4,12,6]  # RAM options in GB

storage_options = [512,1000,256,128,2000,500,64,32,240]  # Storage in GB (SSD/HDD)

gpus = ['610 M',
        'A 370M',
        'A 730M',
        'GTX 1050',
        'GTX 1070',
        'GTX 1650',
        'GTX 1660',
        'MX 130',
        'MX 330',
        'MX 450',
        'MX 550',
        'P 500',
        'RTX 2050',
        'RTX 2060',
        'RTX 2070',
        'RTX 2080',
        'RTX 3000',
        'RTX 3050',
        'RTX 3060',
        'RTX 3070',
        'RTX 3080',
        'RTX 4050',
        'RTX 4060',
        'RTX 4070',
        'RTX 4080',
        'RTX 4090',
        'RTX A1000',
        'RTX A2000',
        'RTX A3000',
        'RTX A5500',
        'RX 6500M',
        'RX 6700M',
        'RX 6800S',
        'RX 7600S',
        'Radeon Pro 5300M',
        'Radeon Pro 5500M',
        'Radeon Pro RX 560X',
        'Radeon RX 6600M',
        'T 1000',
        'T 1200',
        'T 2000',
        'T 500',
        'T 550',
        'T 600']

storage_types = ['SSD', 'eMMC']

touch_options = ['No', 'Yes']

# Input fields from user
brand = st.selectbox('Choose Laptop Brand:', brands)
model = st.selectbox('Choose Laptop Model:', models)
cpu = st.selectbox('Choose CPU (Processor):', cpus)
ram = st.selectbox('Choose RAM (in GB):', ram_options)
storage = st.selectbox('Choose Storage (in GB):', storage_options)
gpu = st.selectbox('Choose GPU:', gpus)
storage_type = st.selectbox('Choose Storage Type (SSD/HDD):', storage_types)
touch = st.selectbox('Do you want a touchscreen? (Yes/No):', touch_options)



# creating passing values
brand = brand_encoding_dict[brand]
model = model_encoding_dict[model]
cpu = cpu_encoding_dict[cpu]
gpu = gpu_encoding_dict[gpu]
touch = touch_encoding_dict[touch]
storage_type = storage_encoding_dict[storage_type]





import pickle

file_path = './model.pkl'

# Open the file in binary read mode ('rb')
with open(file_path, 'rb') as f:
    # Load the content of the pickle file into a Python object
    data = pickle.load(f)


###############################################


# Pricing plans
plans = {
    "Rs 25": (20, "20 predictions"),
    "Rs 50": (50, "50 predictions"),
    "Rs 100": (float('inf'), "unlimited predictions for a month")
}
###############################################

# Initialize session states at the beginning of the script
if not st.session_state.get('payment_initiated', False):
    st.write("Payment has not been initiated.")

if "payment_initiated" not in st.session_state:
    st.session_state.payment_initiated = False
if "free_predictions" not in st.session_state:
    st.session_state.free_predictions = 3
if "predictions_left" not in st.session_state:
    st.session_state.predictions_left = 3
if "plan" not in st.session_state:
    st.session_state.plan = None
if "predictions_used" not in st.session_state:
    st.session_state.predictions_used = 0




# Predict budget based on the input
def predict_budget(brand, model, cpu, ram, storage, gpu, storage_type, touch):
    v = data.predict([[brand, model, cpu, ram, storage, gpu, storage_type, touch]])
    return v[0]


##########################################

def generate_qr_code():
    img = Image.open("./codeqr.jpeg")
    return img


def display_payment_qr(plan_name, amount):
    if amount == 25:
        amount = 25
    elif amount == 50:
        amount = 50
    else :
        amount = 5000
    st.write(f"**Plan Selected: {plan_name}**")
    st.write(f"**Amount: ₹{amount}**")
    st.write("Scan the QR code below to complete the payment:")
    qr_image = generate_qr_code()
    payment_successful = True
    st.image(qr_image)

    st.session_state.predictions_left = amount
    # for price, details in plans.items():
    #         if st.button(f"Buy {details[1]} for {price}"):
    #             st.session_state.payment_initiated = True
    #             display_payment_qr(price, int(price.split()[1]))
    

    st.write("**After completing the payment, click the button below:**")
    if st.button("Verify Payment"):
        print(st.session_state.predictions_left)
        st.session_state.predictions_left = amount
        # Dummy payment verification (replace with actual API call)
        
        payment_successful = True  # Replace with real verification logic
        if payment_successful:
            st.session_state.payment_initiated = True
            st.session_state.plan = plan_name
            
            print(amount)
            st.success(f"Payment successful! You now have {amount}.")
            print(st.session_state.predictions_left)
        else:
            st.error("Payment verification failed. Please try again.")
        
        


# Display free predictions info or package selection
if st.session_state.predictions_left > 0:
    st.info(f"You have {st.session_state.predictions_left} free predictions left.")
else:
    if not st.session_state.payment_initiated:
        st.warning("Free predictions exhausted! Please choose a package to continue.")
        st.subheader("Choose a Package:")
        for price, details in plans.items():
            if st.button(f"Buy {details[1]} for {price}"):
                st.session_state.payment_initiated = True
                display_payment_qr(price, int(price.split()[1]))
    else:
        st.info("Complete your payment to activate the selected plan.")


##################




# Create a button that shows the estimated price when clicked

# Button to calculate the estimated price
if st.button('Calculate Estimated Price'):
    if st.session_state.predictions_left > 0:
        st.session_state.predictions_left -= 1
        st.session_state.predictions_used += 1
        estimated_price = predict_budget(brand, model, cpu, ram, storage, gpu, storage_type, touch) * 84.43
        st.write(f"## Estimated Laptop Price: ₹{estimated_price:.2f}")
        st.write("*This is an estimate based on the selected specifications. Prices may vary depending on location and market conditions.*")
    else:
        st.warning("You need to buy a package to continue predicting.")

####################################