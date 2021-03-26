import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pickle
from datetime import datetime as dt

st.title('VetsBenefits.net NLP Analysis Tool')

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

#@st.cache
with open('/Users/arcarter/Git_Repos/project_05/df_zipped_post3.p', 'rb') as to_read:
    df = pickle.load(to_read)

#st.write(df_corex_standard.astype('object').head(10))

import pickle
#from get_stats import get_stats
from collections import defaultdict
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
break_line = '<hr style="border:2px solid gray"> </hr>'
#t.title('Beer Classifier')
st.sidebar.markdown("### Background")
st.sidebar.markdown("This projet catalogs ongoing topics of interest from the Veterans Benefits Network (vetsbenefits.net) \
         For more information check out the [GitHub](https://github.com/rhyscarter86)")

st.sidebar.markdown(break_line, unsafe_allow_html = True)
st.sidebar.markdown("# ")
topic0_slide = st.sidebar.slider('Covid', min_value=0.000, max_value=1.000, step=.001) # Getting the input.
topic1_slide = st.sidebar.slider('Disability & Appeals', min_value=0.000, max_value=1.000, step=.001)
topic2_slide = st.sidebar.slider('Mental Health', min_value=0.000, max_value=1.000, step=.001)
topic3_slide = st.sidebar.slider('Aid and Attendance', min_value=0.000, max_value=1.000, step=.001)
topic4_slide = st.sidebar.slider('Sleep', min_value=0.000, max_value=1.000, step=.001)
topic5_slide = st.sidebar.slider('City Living', min_value=0.000, max_value=1.000, step=.001)
topic6_slide = st.sidebar.slider('Waiting & Wait Times', min_value=0.000, max_value=1.000, step=.001)
topic7_slide = st.sidebar.slider('College and Other Expenses', min_value=0.000, max_value=1.000, step=.001)
topic8_slide = st.sidebar.slider('Weather', min_value=0.000, max_value=1.000, step=.001)
topic9_slide = st.sidebar.slider('Cancer and Disease', min_value=0.000, max_value=1.000, step=.001)

#topic3_slide = st.slider('Select amount for Topic 3: Medicare', min_value=0.000, max_value=1.000, step=.001)
#topic4_slide = st.slider('Select amount for Topic 4: Spouses', min_value=0.000, max_value=1.000, step=.001)
#topic5_slide = st.slider('Select amount for Topic 5: Weather', min_value=0.000, max_value=1.000, step=.001)
#topic6_slide = st.slider('Select amount for Topic 6: Events', min_value=0.000, max_value=1.000, step=.001)
#topic7_slide = st.slider('Select amount for Topic 7: Navy', min_value=0.000, max_value=1.000, step=.001)
#topic8_slide = st.sidebar.slider('Select amount for Standard Topic 3: Blood Tests & Implants', min_value=0.000, max_value=1.000, step=.001)
#topic9_slide = st.slider('Select amount for Topic 9: Computer', min_value=0.000, max_value=1.000, step=.001)

st.set_option('deprecation.showPyplotGlobalUse', False)

df = df[(df['Covid_Docs'] >= topic0_slide) & (df['Disability_and_Appeals_Docs'] >= topic1_slide) & (df['Mental_Health_Docs'] >= topic2_slide) & (df['Aid_and_Attendance_Docs'] >= topic3_slide) & (df['Sleep_Docs'] >= topic4_slide) & (df['City_Docs'] >= topic5_slide) & (df['Waiting_Docs'] >= topic6_slide) & (df['College_Kids_Docs'] >= topic7_slide) & (df['Cold_Weather_Docs'] >= topic8_slide) & (df['Cancer_and_Disease_Docs'] >= topic9_slide)] # Filtering the dataframe.
st.dataframe(df[['post_text','post_time','Top Topic']].sort_values(by=['post_time'], ascending = True)) # Displaying the dataframe.

with open('/Users/arcarter/Git_Repos/project_05/combined_df_copy_2020-03-22_23PM.p', 'rb') as to_read:
    combined_df_copy = pickle.load(to_read)

with open('/Users/arcarter/Git_Repos/project_05/df_new_post_crosstab_2020-03-23_01AM.p', 'rb') as to_read:
    df_new_post_crosstab = pickle.load(to_read)

#df_crosstab = pd.crosstab(combined_df_copy['week'], combined_df_copy['original_post'])#.plot(figsize=(12,12), kind='bar', stacked=True)

# fig = df_new_post_crosstab[['week','New_Posts']].plot.bar(x='week',y='New_Posts', figsize=(7,6))
#
# xticks = fig.xaxis.get_major_ticks()
# for i,tick in enumerate(xticks):
#     if i%5 != 0:
#         tick.label1.set_visible(False)
#
# plt.title('New Posts vs. Replies')
# plt.xlabel('Week')
# plt.ylabel('Count')
#
# st.pyplot()

# t.markdown(' ## What Is New?')
# #st.markdown(' ### :point_left: Check the sidebar for more details!')
# #st.markdown(' ### All variables set to default mean values.')
# ogi = st.slider(key='OG', label="Original Gravity", min_value=0, max_value=1.00, step=0.001, value = 0.05)
# fgi = st.slider(key='FG', label="Final Gravity", min_value=1.00, max_value=1.10, step=0.001, value = 1.014)
# abvi = st.slider(key='ABV', label="ABV", min_value=0.0, max_value=15.0, step=0.01, value = 6.23)
# srmi = st.slider(key='SRM', label="SRM", min_value=0.0, max_value= 100.0, step=1.0, value = 13.5)
# ibui = st.slider(key='IBU', label="IBU", min_value=0.0, max_value=120.0, step=1.0, value = 44.0)
# hopi = st.slider(key='hop', label="How Complex is the Hop Profile?", min_value=0.0, max_value=10.0, step=0.25, value = 2.5) * 15
#
# bugui = float(ibui / ((ogi - .999999999) * 1000))
# beer_array = np.array([ogi, fgi, abvi, srmi, ibui, bugui, hopi])
# test_df = df_corex_standard #pd.DataFrame(beer_array, index=['og', 'fg', 'abv', 'srm', 'ibu', 'bugu', 'hopcmp']).T
#

#

# ncol = st.sidebar.number_input("Number of dynamic columns", 0, 20, 1)
# cols = st.beta_columns(ncol)
#
# for i, x in enumerate(cols):
#     x.selectbox(f"Input # {i}",[1,2,3], key=i)

#             and his own personal website https://timdooley.com where a write up about this project can be found!")


# st.sidebar.markdown("Try `OG 1.05`, `FG 1.01`, `ABV 4.30`, `SRM 3.0`, `IBU 12`, `Hops 2.00`. Lager/Cream Ale! What would make it an IPA? Bump the SRM up, what happens?")
# st.sidebar.markdown(break_line, unsafe_allow_html = True)
# st.sidebar.markdown("### Key to Sliders")
# # st.sidebar.markdown("Beer is a complex thing! What you see here are more complex numerical ways to think about beer!  \
# #     All quantities are set to the global average of the 27,000 recipes.")
# # st.sidebar.markdown("* Original Gravity: You will sometimes see this on the bottle. It is the amount of sugar that the beer starts with \
# #     before yeast is pitched. You can read about it here [Wiki: Beer Gravity](https://en.wikipedia.org/wiki/Gravity_(alcoholic_beverage)#Original_gravity_(OG);_original_extract_(OE))")
# # st.sidebar.markdown("* Final Gravity: As above but after all is said and done in fermentation. How much sugar is left over? Leave default if not sure.")
# # st.sidebar.markdown("* ABV, Alcohol by Volume. You know this one! Turns out how much alcohol in a beer really matters for style!")
# # st.sidebar.markdown("* SRM, Standard Reference Method. What color is your beer? [Wiki: SRM](https://en.wikipedia.org/wiki/Standard_Reference_Method)")
# # # st.sidebar.image("app_pics/srm_pic.png") # this was for local testing
# # st.sidebar.image("/app/beer_project/web_app/app_pics/srm_pic.png")
# #
# # st.sidebar.markdown("* IBU, International Bittering Units. How bitter is this beer? 0 water to 100+ super bitter. [Wiki: IBU](https://en.wikipedia.org/wiki/Beer_measurement#Bitterness)")
# # st.sidebar.markdown("* Hop Complexity. This ones a bit of a judgement call. On a scale of 0-10, how many different hops go into this beer? Just one? Around 0-3. A bunch, 9-10!")
#
#
# # with open('forest3.pickle', 'rb') as to_read:
# #     forest3 = pickle.load(to_read)
# # with open('forest3op.pickle', 'rb') as to_read:
# #     forest3op = pickle.load(to_read)
# # with open('/app/beer_project/web_app/knn3.pickle', 'rb') as to_read:
# #     knn3 = pickle.load(to_read)
# # # with open('mnb3.pickle', 'rb') as to_read:
# # #    mnb3 = pickle.load(to_read)
# # with open('/app/beer_project/web_app/logr3.pickle', 'rb') as to_read:
# #     logr3 = pickle.load(to_read)
# # with open('/app/beer_project/web_app/xgb3.pickle', 'rb') as to_read:
# #     xgb3 = pickle.load(to_read)
#
# def filterer(test_df):
#
#
# # test_df = get_stats()
# def predictor(test_df):
#     preds = [knn3.predict(test_df)[0], logr3.predict(test_df)[0],
#              xgb3.predict(test_df)[0], xgb3.predict(test_df)[0]] #forest3op.predict(test_df)[0], forest3.predict(test_df)[0] mnb3.predict(test_df)[0],
#     clean_pred = defaultdict(int)
#     for pred in preds:
#         if pred == 'IPA/Pale Ales':
#             clean_pred['IPA/Pale Ales'] += 1
#         elif pred == 'Strong/Dark Ales':
#             clean_pred['Strong/Dark Ales'] += 1
#         elif pred == 'Lager/Cream Ale':
#             clean_pred['Lager/Cream Ale'] += 1
#         else:
#             clean_pred['Other'] += 1
#     res_dic = dict(clean_pred)
#     if 'Lager/Cream Ale' in res_dic.keys():
#         return('Lager/Cream Ale')
#         print('lager!')
#     else:
#         for key, value in res_dic.items():
#             # if key == 'Lager/Cream Ale':
#             #     return('Lager/Cream Ale')
#
#             #     # if value >= 2:
#             #     #break
#             #     # else:
#             #     #     continue
#             # # elif value ==  2: #len(preds) //
#             # #     return("Mmm.. that could be a few things, keep sliding.")
#             # #     break
#             if value >= 2:
#                 return(key)
#             else:
#                 continue
#
# st.markdown("## Oh, I know! You're drinking \n")
# st.markdown("# " + predictor(test_df))
# if predictor(test_df) == 'IPA/Pale Ales':
#     st.image('/app/beer_project/web_app/ipa_img.jpg', use_column_width=True)
# if predictor(test_df) == 'Strong/Dark Ales':
#     st.image('/app/beer_project/web_app/stout_img.jpg', use_column_width=True)
# if predictor(test_df) == 'Lager/Cream Ale':
#     st.image('/app/beer_project/web_app/lager_img.jpg', use_column_width=True)
# # print(res_dic, preds)
