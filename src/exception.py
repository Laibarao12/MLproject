from src.logger import logging
import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # This _ mean info we have skiped first two info and focusing on thired 
    # this third one give the info here the erroer occusred aand at which line  and file
    error_message = "Error occured in pyton script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # fixed: super.__init__ → super().__init__()
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

    # This mean to raise custom error of our woen like 
    # age cant be neagtive 

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)
