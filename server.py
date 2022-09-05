#!/usr/bin/env python

import streamlit as st
import requests
import sys
import numpy as np
import pandas as pd
import os



st.title('Simple SQL request GUI')
#st.image("https://i.postimg.cc/yN20YX4F/Stories.png", use_column_width=True)

try:
    tables = {'table1': {'column1': ['first', 'second'], 'column2': []}}
    table = st.selectbox("Choose table", tables)
    columns = list(tables[table])#[list(dict.keys())[0] for dict in tables[table]]
    column1 = st.selectbox("choose column1", columns)
    if tables[table][column1] == None:
        value1 = st.text_input("print keywords 1")
    else:
        value1 = st.multiselect("choose column values 1", tables[table][column1])

    column2 = st.selectbox("choose column2", columns)
    if tables[table][column2] == None:
        value2 = st.text_input("print keywords 2")
    else:
        value2 = st.multiselect("choose column values 2", tables[table][column2])




    # sound_provider = st.selectbox("Choose sound API", ('Play.ht','Amazon'))
    # voice_ids, voice_names = read_voices(sound_provider)
    #
    # form_1 = st.form(key='my-form1')
    # st.session_state['story_prompt'] = story_prompt = form_1.selectbox("Choose  your story prompt", var_dict[hero])
    # story_prompt_temp = form_1.text_input("OR Enter your story prompt")
    # if story_prompt_temp != "":
    #     st.session_state['story_prompt'] = story_prompt = story_prompt_temp
    #
    # print('responce' in st.session_state)
    # if 'responce' in st.session_state:
    #
    #     responce = st.session_state['responce']
    #     responce = form_1.text_area('Fairytail about {}:'.format(st.session_state['story_prompt']), responce, height=400)
    #     show_listen = False
    #
    #     if analyse_flag:
    #             st.text(f"sentiment: {st.session_state['sentiment']}")
    #             st.text(f"under 18+: {st.session_state['love_mood']}: {st.session_state['bad_word']}")
    #     print(responce)
    # else:
    #     responce = ""
    #     show_listen = False
    #
    #
    # generate = form_1.form_submit_button('Generate fairytale')
    # voice_name = form_1.selectbox("Choose your story teller", voice_names, index = 3)
    # print(voice_name)
    # col1, col2, col3, col4 = form_1.columns(4)
    # with col1:
    #         listen = form_1.form_submit_button('Listen fairytale')#, disabled=show_listen)
    # # with col2:
    # #         make_images = form_1.form_submit_button('Make images')#, disabled = show_listen)
    # if generate:
    #     print('story prompt: ', story_prompt)
    #     status, resp_raw = send_request("tale", {'prompt': f'{story_prompt}', 'analyse_flag' : analyse_flag})
    #     print("generate")
    #     #print(status, resp_raw)
    #     resp = resp_raw
    #     if status == 0:
    #          responce = st.session_state['responce'] = resp['tale']
    #          for key in ['image_names', 'audio', 'tale_parts']:
    #                  if key in st.session_state:
    #                         st.session_state.pop(key)
    #          #print(responce)
    #          if analyse_flag == True:
    #             st.session_state['sentiment'] = resp['sentiment']
    #             st.session_state['love_mood'], st.session_state['bad_word'] = resp['love_mood'], resp['bad_word']
    #          st.experimental_rerun()
    #     else:
    #          st.text(f"tale wasn't created")
    #
    # # if make_images:
    # #     image_names, parts = get_images_tale(responce, hero)
    # #     st.session_state['image_names'], st.session_state['tale_parts'] = image_names, parts
    # #     #parts = get_images_tale(responce, command)
    # #
    # # if 'image_names' in st.session_state:
    # #     table = st.columns(len(st.session_state['image_names']))
    # #     for i in range(len(st.session_state['image_names'])):
    # #         with table[i]:
    # #             st.image(st.session_state['image_names'][i])
    # # if ('image_names' in  st.session_state) and ('responce' in  st.session_state) and ('tale_parts' in st.session_state) :
    # #     data = create_pdf(st.session_state['story_prompt'], st.session_state['tale_parts'], st.session_state['image_names'])
    # #     st.download_button(
    # #         "⬇️ Download Tale",
    # #         data=data,
    # #         file_name="tale.pdf",
    # #         mime="application/octet-stream",
    # #     )
    # #     print("pdf")
    # # else:
    # #     print("no pdf")
    # if listen:
    #     status, audio = send_request("audio",  {'tale': f'{responce}', 'voice': f'{voice_name}', 'sound_provider': 'Amazon'})
    #     #print(status, audio)
    #     if status == 0:
    #         print(audio)
    #         st.session_state['audio'] = audio
    #     else:
    #         st.text(f"audio for {voice_name} wasn't created")
    # if 'audio' in st.session_state:
    #     form_1.audio(st.session_state['audio'] )


except Exception as e:
    st.success(f'Something Went Wrong! {e}')   





