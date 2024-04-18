import streamlit as st
import streamlit.components.v1 as com
import random
import numpy as np 

smiley = chr(0x1F600)
#st.title("Your wellcome" + smiley)

com.html(""" <html>
  <head>
<style>
.animated_rainbow_2 {
    font-size = 42px;
    font-family: cursive;
    text-align :left;
    padding:1px;
    height: 100px;
    -webkit-animation: animatedBackground_b 3s linear infinite alternate;
}

@keyframes animatedBackground_b{
    0% {color: #ff8b00;}
    10% {color: #e8ff00}
    20% {color: #5dff00}
    30% {color: #00ff2e}
    40% {color: #00ffb9}
    50% {color: #00b9ff}
    60% {color: #002eff}
    70% {color: #5d00ff}
    80% {color: #e800ff}
    90% {color: #ff008b}
    100% {color: #ff0000}
}
</style>
  </head>
  
   <p class="animated_rainbow_2"> <font size =10> you are Wellcome, let's play delat game !  &#128512</font></p>
   <title> this is a title </title>
</body> 
</html>
""")




















formbtn = st.button("if you are ready to play 🤔 click me ")
st.snow()

if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False

if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True

    
    st.subheader(" Info game")
    # name = st.text_input("Name")
    with st.form(key = 'user_info'):
        st.write('User Information')
        ag= st.text_input(label="input your name please")
        ag_= st.number_input(label="input a non null number  🔢 ",value=0)
        a=ag
        count=0
        while a==ag :
            np.random.seed(ag_)
            a=np.random.randint(1, 10)
            a2=np.random.randint(1, 10)
            b=a2+a
            d=a*a2
        if (len(ag)!= 0):
            if(ag_):
                st.write('can you solve this delat equation :green 🤔?')
                st.write("x^2 + ",b,"x +",d)

        age = st.number_input(label="Entre one solution please  ", value=0)
        age2 = st.number_input(label="Entre the seconde one  ", value=0)
        #color = st.color_picker('Pick A Color', '#00f900')
        
    
        submit_form = st.form_submit_button(label="If you want to play again 🥰 refresh the page \n or click to have your result", help="Click to register!")
    
        # Checking if all the fields are non empty
        if submit_form:
            
    
            if age2 and age :
                # add_user_info(id, name, age, email, phone, gender)
                if age == a2 :
                    value=age
                    if age2==a:
                        st.write(f"You are genis:blue #128521[{ag}]",':winking face:')
                        st.balloons()
                       
                    #st.session_state.formbtn_state= True
                    else: 
                        st.write("Sorry 1 answer is wrong",'🙁')
                        count=count+1
                        st.session_state.formbtn_state=True
                elif age==a:
                    value=age
            
                    if age2==a2:
                        st.balloons()
                        st.write(f"You are genis:blue[{ag}]",'😉')
                    #st.session_state.formbtn_state=True
                    else: 
                        st.write("Sorry 1 answer is wrong ", '🙁')
                        count=count+1
                    
            elif count !=1 & count !=0 :
                st.write("Sorry your 2 answers are wrong",'🙁')
                st.session_state.formbtn_state=True
            else:
                st.warning("Please fill all the fields")