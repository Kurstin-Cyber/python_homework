import traceback



try:
    with open('diary.txt', 'a') as file:
        is_first_prompt = True
        while True:
            if is_first_prompt:
                msg = "What happened today? "
            else:
                msg = "What else? "
            
            user_input = input(msg)
        

            is_first_prompt = False
            if user_input == "done for now":
                file.write(user_input + "\n")
                break
            else:
                file.write(user_input + "\n")

except BaseException as e:
    print("An exception occurred.", type(e).__name__)
    traceback.print_exc()   
            


        
            
      
        


