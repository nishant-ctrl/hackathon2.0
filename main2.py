import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition","Customer Support"])

#Main Page
if(app_mode=="Home"):
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.jpeg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)

#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))
        if(format(class_name[result_index])=='Apple___Apple_scab'):
            st.success("Treat leaves on the tree immediately before the leaves fall with a nitrogenous fertiliser to speed up leaf breakdown.Mulch the leaf litter after the leaves fall. ...Combine leaf mulching with the ground application of a nitrogenous fertiliser.")
        elif(format(class_name[result_index])=='Apple___Black_rot'):
            st.success("Remove dead or diseased limbs and mummified fruit, and dispose of them by burning or burying. You can also prune out cankers at least 15 inches below the basal end.")  
        elif(format(class_name[result_index])=='Apple___Cedar_apple_rust'):
            st.success("Fungicides with the active ingredient Myclobutanil are most effective in preventing rust. Copper and sulfur products can be used as well.")  
        elif(format(class_name[result_index])=='Apple___healthy'):
            st.success("The Plant is Healthy.No Cure Required")
        elif(format(class_name[result_index])=='Blueberry___healthy'):
            st.success("The Plant is Healthy.No Cure Required")
        elif(format(class_name[result_index])=='Cherry_(including_sour)___Powdery_mildew'):
            st.success("Use fungicides at the right intervals, starting when the petals fall and continuing until the pits harden. Rotate between fungicide classes to reduce the risk of resistance. ")
        elif(format(class_name[result_index])=='Cherry_(including_sour)___healthy'):
            st.success("The Plant is Healthy.No Cure Required")
        elif(format(class_name[result_index])=='Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot'):
            st.success("Use corn varieties that are resistant to GLS, which are available from seed companies. Plant corn at the beginning of the rainy season to reduce the disease's impact on yield.")
        elif(format(class_name[result_index])=='Corn_(maize)___Common_rust_'):
            st.success("Rotate crops with non-cereal crops every 2–3 years. Remove weeds that are Oxalis spp.")
        elif(format(class_name[result_index])=='Corn_(maize)___Northern_Leaf_Blight'):
            st.success("Avoid planting corn in low-lying, shaded areas with poor drainage and high humidity. These conditions can lead to serious leaf diseases.")
        elif(format(class_name[result_index])=='Corn_(maize)___healthy'):
            st.success("The Plant id Healthy. No Cure Required")
        elif(format(class_name[result_index])=='Grape___Black_rot'):
            st.success("Remove mummified fruit, dead trees, dead or dying infected limbs. Prune out cankers to greatly reduce the amount of available inoculum. For homeowners, black rot can be controlled by starting a full-rate protectant spray program early in the season with copper-based products, lime-sulfur or Daconil.")
        elif(format(class_name[result_index])=='Grape___Esca_(Black_Measles)'):
            st.success("Avoid pruning during heavy rainfall, and use alternative methods like double or delayed pruning.sanitary practices can reduce or eliminate pre-planting infections.")
        elif(format(class_name[result_index])=='Grape___Leaf_blight_(Isariopsis_Leaf_Spot)'):
            st.success("consider using lemongrass essential oil, which has been shown to reduce the severity of these diseases. Additionally, it is important to remove and destroy infected berries, leaves, and trunks, while also protecting prune wounds to prevent further infection. Regular monitoring and sanitation practices can also aid in disease prevention.")
        elif(format(class_name[result_index])=='Grape___healthy'):
            st.success("The Plant is Healthy.No Cure Required")
        elif(format(class_name[result_index])=='Tomato___healthy'):
            st.success("The plant is Healthy.No cure Required")
        elif(format(class_name[result_index])=='Tomato___Tomato_mosaic_virus'):
            st.success("Remove infected plants: Promptly remove plants that show symptoms of the virus, as they can infect nearby plants. ")
        elif(format(class_name[result_index])=='Tomato___Tomato_Yellow_Leaf_Curl_Virus'):
            st.success("Spray with insecticides: Spray plants with insecticides like azadirachtin (neem), pyrethrin, or insecticidal soap. You can also try spraying with Cypermethrin (0.01%) or Dimethoate (0.1%) every seven days. ")
        elif(format(class_name[result_index])=='Tomato___Target_Spot'):
            st.success("Apply fungicides like chlorothalonil, copper oxychloride, mancozeb, azoxystrobin, pyraclostrobin, boscalid, or acibenzolar-S-methyl before symptoms appear, and then at regular intervals. ")
        elif(format(class_name[result_index])=='Tomato___Spider_mites Two-spotted_spider_mite'):
            st.success("Apply a light coating of sulfur dust 2 to 3 weeks after planting to prevent infestations and stop fungus. ")
        elif(format(class_name[result_index])=='Tomato___Septoria_leaf_spot'):
            st.success("applications of copper-based products registered for use on tomato, especially during warm, wet periods.")
        elif(format(class_name[result_index])=='Strawberry___healthy'):
            st.success("The plant is Healthy.No cure Required")
        elif(format(class_name[result_index])=='Strawberry___Leaf_scorch'):
            st.success("Since this fungal pathogen overwinters on the fallen leaves of infected plants, proper garden sanitation is key. This includes the removal of infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants")
        elif(format(class_name[result_index])=='Tomato___Bacterial_spot'):
            st.success("A plant with bacterial spot cannot be cured. Remove symptomatic plants from your garden or greenhouse to prevent the spread of bacteria to healthy plants. Burn (where allowed by local ordinance), bury or hot compost the affected plants, and DO NOT eat symptomatic fruit.")
        elif(format(class_name[result_index])=='Tomato___Early_blight'):
            st.success("Remove infected leaves during the growing season and remove all infected plant parts at the end of the season. Apply a synthetic fungicide or an organic fungicide (fixed copper) according to label directions, early in the season, when symptoms appear to slow the spread of the disease.")
        elif(format(class_name[result_index])=='Tomato___Late_blight'):
            st.success("Late blight is controlled by eliminating cull piles and volunteer potatoes, using proper harvesting and storage practices, and applying fungicides when necessary. Air drainage to facilitate the drying of foliage each day is important.")
        elif(format(class_name[result_index])=='Tomato___Leaf_Mold'):
            st.success("TFor plants growing under cover, increase ventilation and, if possible, the space between plants. Try to avoid wetting the leaves when watering plants, especially when watering in the evening, Copper-based fungicides can be used to control diseases on tomatoes.")
        elif(format(class_name[result_index])=='Orange__Haunglongbing(Citrus_greening)'):
            st.success("The best way to prevent the introduction of citrus greening is to prevent the introduction of the Asian citrus psyllid. Currently, intensive chemical control is the primary management tool to reduce populations, but this strategy is costly and increasingly ineffective.")
        elif(format(class_name[result_index])=='Peach___Bacterial_spot'):
            st.success("Good tree vigor should be maintained by proper pruning, judicious application of fertilizer, and watering when necessary. Excess nitrogen may aggravate the disease. Planting susceptible trees in close proximity to one another can contribute to the buildup of the disease.")
        elif(format(class_name[result_index])=='Peach___healthy'):
            st.success("The Plant is Healthy. No cure Required.")
        elif(format(class_name[result_index])=='Pepper,bell__Bacterial_spot'):
            st.success("For a preventative purpose, use pathogen-free seed and transplants. Rotate with non-host plants to avoid carryover of the pathogen on volunteers and crop residue. Do not rotate pepper with tomato, eggplant, or potato, and do not grow these crops together. Avoid overhead irrigation.")
        elif(format(class_name[result_index])=='Pepper,bell__healthy'):
            st.success("The Plant is Healthy. No cure required")
        elif(format(class_name[result_index])=='Potato___Early_blight'):
            st.success("Measures for controlling and preventing blights typically involve the destruction of the infected plant parts; use of disease-free seed or stock and resistant varieties; crop rotation; pruning and spacing of plants for better air circulation; controlling pests that carry the fungus from plant to plant; avoidance of overhead watering and working among wet plants")
        elif(format(class_name[result_index])=='Potato___Late_blight'):
            st.success("If there is visible late blight infestation it is recommended to apply fungicides with a spore-killing effect (fluazinam-containing fungicides, Ranman Top) mainly.")
        elif(format(class_name[result_index])=='Potato___healthy'):
            st.success("The Plant is Healthy. No cure required")
        elif(format(class_name[result_index])=='Raspberry___healthy'):
            st.success("The Plant is Healthy. No cure required")
        elif(format(class_name[result_index])=='Soybean___healthy'):
            st.success("The Plant is Healthy. No cure required")
        elif(format(class_name[result_index])=='Squash___Powdery_mildew'):
            st.success("Powdery mildew fungicide: Use sulfur-containing organic fungicides as both preventive and treatment for existing infections")
        else:
            st.success("No Result Found")    
elif(app_mode=="Customer Support"):
    st.header("Customer Support")
    st.markdown("""
                Name : xxxxxxxxxx.

                Mobile : +91 9999999999.

                Email : example@abc.com
                
                """)