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

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__) 
    stack_trace = list()
    for trace in traceback:
        stack_trace.append(f'File : {trace[0]} , Line :{trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__})")
        message = str(e)
        if message:
            print(f'Exception message: {message}')
        print(f'Stack trace: {stack_trace}')
            
      
        


