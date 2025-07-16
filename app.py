
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import base64 
##############################################
##############################################
def Fibbonacci(N):
    #################################################
    ########## Fibbonacci Numbers ###################
    #################################################
    F = [0,1]
    for i in range(N):
      F.append(F[-1]+F[-2])
    #################################################
    ############## Centroid Finder ##################
    #################################################
    I = [[0,0],[0,0],[0,0]]
    for j in range(3,N):
      pivot = (j-2)%4
      if pivot == 1:
        X_flag, Sign_Flag = True, True
      elif pivot == 2:
        X_flag, Sign_Flag = False, True
      elif pivot == 3:
        X_flag, Sign_Flag = True, False 
      elif pivot == 0:
        X_flag, Sign_Flag = False, False
      ############################################
      x_temp,y_temp = I[j-1][0], I[j-1][1]
      if Sign_Flag == True and X_flag == True:
        x_temp += F[j-2]
      elif Sign_Flag == True and X_flag == False:
        y_temp += F[j-2] 
      elif Sign_Flag == False and X_flag == True:
        x_temp -= F[j-2]
      elif Sign_Flag == False and X_flag == False:
        y_temp -= F[j-2]
      ##########################################
      I.append([x_temp,y_temp])
    ###############################################
    ############  Curve Formation #################
    ###############################################
    F,C   = F[1:], I[1:]
    P,X,Y  = [[0,0]],list(),list()
    Angle  = [[1,91],[91,181],[181,271],[271,361]] 
    for i in range(len(C)):
        ###  angle aliner ###
        pivot_a = i%4
        AnR     = Angle[pivot_a]
        r       = F[i]
        ### x,y alignment ###
        x_align, y_align = C[i][0],C[i][1]
        for j in range(AnR[0],AnR[1]):
            x_temp = r*np.cos(np.deg2rad(j))
            y_temp = r*np.sin(np.deg2rad(j))
            
            P.append([x_temp,y_temp])
            X.append(x_temp + x_align)
            Y.append(y_temp + y_align)
    ############################################
    ############  Length finder ################
    ############################################ 
    L = 0     
    for k in range(len(F)):
        r_temp = F[k]
        L += np.pi*(r_temp/2)
    return P,X,Y,L 
#################################################################
################# Background image selection ####################
#################################################################
### Function to convert local image to base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

### Provide your local image path (e.g., Indian flag)
local_image_path = "MK.jpg"  # or "flag.png"

### Get base64 string
base64_img = get_base64_image(local_image_path)

### Inject custom CSS with base64-encoded image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
#################################################################
#################################################################
st.title("🧮 SS AI Lab's Mathematical Assistant")
operation = st.radio("✅ Choose the operation:", ["Addition", "Subtraction", "Multiplication", "Division", "Fibbonacci Curve"])

################################################################
if operation == "Addition":
    num1 = st.number_input("Enter the Value of A", format="%.2f")
    num2 = st.number_input("Enter the Value of B", format="%.2f")
    result = num1 + num2
elif operation == "Subtraction":
    num1 = st.number_input("Enter the Value of A", format="%.2f")
    num2 = st.number_input("Enter the Value of B", format="%.2f")
    result = num1 - num2
elif operation == "Multiplication":
    num1 = st.number_input("Enter the Value of A", format="%.2f")
    num2 = st.number_input("Enter the Value of B", format="%.2f")
    result = num1 * num2
elif operation == "Division":
    num1 = st.number_input("Enter the Value of A", format="%.2f")
    num2 = st.number_input("Enter the Value of B", format="%.2f")
    result = num1 / num2 if num2 != 0 else "❌ Cannot divide by zero" 
elif operation == "Fibbonacci Curve":
    N = st.number_input("Enter the number of terms (N)", min_value=1, max_value=100, value=6, step=1)
    P,X,Y,L = Fibbonacci(N)
    # result = f"Fibbonacci Curve Length: {L:.2f} units" 


if st.button("Calculate"):
    if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
        st.success(f"Result: {result}")
    elif operation == "Fibbonacci Curve":
        fig, ax = plt.subplots()
        ax.plot(X,Y, label="sin(x)", color='navy')
        ax.set_title("Fibbonacci Curve")
        ax.set_xlabel("X-axis (one unit)")
        ax.set_ylabel("Y-axis (one unit)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)
    # st.success(f"Result: {result}")
####################################################
####################################################
