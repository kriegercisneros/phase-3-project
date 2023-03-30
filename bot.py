def run_bot(user_id, session_id, persona = None):
    '''this is where i write my logic to test if we have a persona selected'''
    if(persona=="Spanish Language"):
        from spanish_language import run_spanish_persona
        run_spanish_persona(user_id, session_id)
    elif(persona =="English Language"):
        from english_language import run_english_language
        run_english_language(user_id, session_id)
    elif(persona =="Chinese Persona"):
        from chinese_language_bot import run_chinese_persona
        run_chinese_persona(user_id, session_id)
    elif(persona=="Akan Language"):
        from akan_language import run_akan_persona
        run_akan_persona(user_id, session_id)
    elif(persona==None):
        option=input('''
                    What Bot Language Persona would you like to chat with?
                    1)English
                    2)Spanish
                    3)Simplified Chinese
                    4)Akan
        ''')
        if(option=="1"):
            from english_language import run_english_language
            run_english_language(user_id, session_id)
        elif(option == "2"):
            from spanish_language import run_spanish_persona
            run_spanish_persona(user_id, session_id)
        elif(option == "3"):
            from chinese_language_bot import run_chinese_persona
            run_chinese_persona(user_id, session_id) 
        elif(option == "4"):
            from akan_language import run_akan_persona
            run_akan_persona(user_id, session_id)

# run_bot(1,1, "Spanish Language")
